#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


SITES = {
    "coupang": "https://www.coupang.com/",
    "gmarket": "https://www.gmarket.co.kr/",
    "musinsa": "https://www.musinsa.com/",
    "oliveyoung": "https://www.oliveyoung.co.kr/",
}

AGENTS = [
    "Googlebot",
    "OAI-SearchBot",
    "GPTBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-SearchBot",
    "Claude-User",
]

PLATFORM_SOURCES = {
    "openai": "https://developers.openai.com/api/docs/bots",
    "google_crawlers": "https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers",
    "google_merchant": "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing",
    "anthropic": "https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler",
}


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title_parts: list[str] = []
        self.meta: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.json_ld_blocks: list[str] = []
        self.in_json_ld = False
        self.current_script: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            self.meta.append(attrs_dict)
        elif tag == "link":
            self.links.append(attrs_dict)
        elif tag == "script" and attrs_dict.get("type", "").lower() == "application/ld+json":
            self.in_json_ld = True
            self.current_script = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_json_ld:
            block = "".join(self.current_script).strip()
            if block:
                self.json_ld_blocks.append(block)
            self.in_json_ld = False
            self.current_script = []

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_json_ld:
            self.current_script.append(data)


@dataclass
class FetchResult:
    url: str
    final_url: str | None
    status: int | None
    headers: dict[str, str]
    body: str
    error: str | None


def fetch(url: str, timeout: float = 20.0) -> FetchResult:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.7,en;q=0.6",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read(2_000_000)
            charset = response.headers.get_content_charset() or "utf-8"
            return FetchResult(
                url=url,
                final_url=response.geturl(),
                status=response.status,
                headers=dict(response.headers.items()),
                body=raw.decode(charset, errors="replace"),
                error=None,
            )
    except urllib.error.HTTPError as exc:
        raw = exc.read(500_000)
        charset = exc.headers.get_content_charset() or "utf-8"
        return FetchResult(
            url=url,
            final_url=exc.geturl(),
            status=exc.code,
            headers=dict(exc.headers.items()),
            body=raw.decode(charset, errors="replace"),
            error=f"HTTPError: {exc.code} {exc.reason}",
        )
    except Exception as exc:  # noqa: BLE001 - evidence capture must record network failures.
        return FetchResult(
            url=url,
            final_url=None,
            status=None,
            headers={},
            body="",
            error=f"{type(exc).__name__}: {exc}",
        )


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def extract_sitemaps(robots_body: str) -> list[str]:
    urls: list[str] = []
    for line in robots_body.splitlines():
        if line.lower().startswith("sitemap:"):
            url = line.split(":", 1)[1].strip()
            if url:
                urls.append(url)
    return urls


def extract_json_ld_types(blocks: list[str]) -> list[str]:
    types: list[str] = []

    def collect(value: object) -> None:
        if isinstance(value, dict):
            raw_type = value.get("@type")
            if isinstance(raw_type, str):
                types.append(raw_type)
            elif isinstance(raw_type, list):
                types.extend(str(item) for item in raw_type)
            for nested in value.values():
                collect(nested)
        elif isinstance(value, list):
            for item in value:
                collect(item)

    for block in blocks:
        try:
            collect(json.loads(block))
        except json.JSONDecodeError:
            continue
    return sorted(set(types))


def first_meta(meta: list[dict[str, str]], key: str, value: str) -> str | None:
    for item in meta:
        if item.get(key, "").lower() == value.lower():
            return item.get("content") or None
    return None


def first_link(links: list[dict[str, str]], rel: str) -> str | None:
    for item in links:
        rels = {part.lower() for part in item.get("rel", "").split()}
        if rel.lower() in rels and item.get("href"):
            return item["href"]
    return None


def robots_policy(robots_url: str, robots_body: str, target_url: str) -> dict[str, object]:
    parser = urllib.robotparser.RobotFileParser()
    parser.set_url(robots_url)
    parser.parse(robots_body.splitlines())
    return {agent: parser.can_fetch(agent, target_url) for agent in AGENTS}


def classify_site(evidence: dict[str, object]) -> dict[str, object]:
    homepage = evidence["homepage"]
    robots = evidence["robots"]
    html = evidence["html"]
    policies = evidence["robots_policy"]
    json_ld_types = set(html["json_ld_types"])

    homepage_ok = homepage["status"] is not None and int(homepage["status"]) < 400
    robots_ok = robots["status"] is not None and int(robots["status"]) < 400
    search_allowed = bool(policies.get("Googlebot")) and bool(policies.get("OAI-SearchBot")) and bool(
        policies.get("Claude-SearchBot")
    )
    merchant_types = {"Product", "Offer", "AggregateOffer"}
    has_merchant_schema = bool(json_ld_types & merchant_types)
    has_discovery_schema = bool(json_ld_types & {"Organization", "WebSite", "BreadcrumbList", "ItemList"})

    if not homepage_ok:
        readiness = 35
        confidence = "medium" if robots_ok else "low"
    else:
        readiness = 50
        if robots_ok:
            readiness += 15
        if search_allowed:
            readiness += 15
        if html["title"]:
            readiness += 5
        if html["meta_description"]:
            readiness += 5
        if has_discovery_schema:
            readiness += 5
        if has_merchant_schema:
            readiness += 10
        confidence = "medium"

    blockers: list[str] = []
    if not homepage_ok:
        blockers.append("홈페이지 HTTP 접근이 4xx/5xx 또는 네트워크 오류로 확인되어 public fetch 안정성이 낮음")
    if not robots_ok:
        blockers.append("robots.txt를 정상 판독하지 못해 crawler control 증거가 불완전함")
    if not policies.get("OAI-SearchBot"):
        blockers.append("OAI-SearchBot의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음")
    if not policies.get("Claude-SearchBot"):
        blockers.append("Claude-SearchBot의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음")
    if homepage_ok and not has_merchant_schema:
        blockers.append("수집된 루트 HTML에서 Product/Offer 계열 merchant schema가 확인되지 않음")

    return {
        "readiness_score": min(readiness, 100),
        "confidence": confidence,
        "search_access_ready": search_allowed,
        "merchant_schema_on_root": has_merchant_schema,
        "discovery_schema_on_root": has_discovery_schema,
        "blockers": blockers,
    }


def audit_site(slug: str, url: str) -> dict[str, object]:
    parsed = urllib.parse.urlparse(url)
    robots_url = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, "/robots.txt", "", "", ""))

    robots = fetch(robots_url)
    homepage = fetch(url)
    parser = HeadParser()
    parser.feed(homepage.body[:1_000_000])

    html = {
        "title": normalize_space("".join(parser.title_parts)),
        "meta_description": first_meta(parser.meta, "name", "description"),
        "meta_robots": first_meta(parser.meta, "name", "robots"),
        "canonical": first_link(parser.links, "canonical"),
        "open_graph_count": len([item for item in parser.meta if item.get("property", "").startswith("og:")]),
        "json_ld_block_count": len(parser.json_ld_blocks),
        "json_ld_types": extract_json_ld_types(parser.json_ld_blocks),
    }
    evidence: dict[str, object] = {
        "slug": slug,
        "url": url,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "platform_sources": PLATFORM_SOURCES,
        "robots": {
            "url": robots_url,
            "status": robots.status,
            "final_url": robots.final_url,
            "content_type": robots.headers.get("Content-Type"),
            "error": robots.error,
            "sitemaps": extract_sitemaps(robots.body),
            "body_excerpt": robots.body[:3000],
        },
        "robots_policy": robots_policy(robots_url, robots.body, url)
        if robots.body and robots.status is not None and int(robots.status) < 400
        else {agent: None for agent in AGENTS},
        "homepage": {
            "url": url,
            "status": homepage.status,
            "final_url": homepage.final_url,
            "content_type": homepage.headers.get("Content-Type"),
            "server": homepage.headers.get("Server"),
            "challenge_signal": homepage.headers.get("cf-mitigated")
            or homepage.headers.get("x-reference-error")
            or homepage.headers.get("X-Reference-Error"),
            "error": homepage.error,
            "body_bytes_sampled": len(homepage.body.encode("utf-8")),
        },
        "html": html,
    }
    evidence["classification"] = classify_site(evidence)
    return evidence


def site_name(slug: str) -> str:
    return {
        "coupang": "Coupang",
        "gmarket": "Gmarket",
        "musinsa": "Musinsa",
        "oliveyoung": "Olive Young",
    }[slug]


def yes_no(value: object) -> str:
    if value is True:
        return "허용"
    if value is False:
        return "차단/비허용"
    return "미확인"


def write_report(out_dir: Path, evidence: dict[str, object]) -> None:
    slug = str(evidence["slug"])
    html = evidence["html"]
    robots = evidence["robots"]
    homepage = evidence["homepage"]
    classification = evidence["classification"]
    policy = evidence["robots_policy"]
    platform_sources = evidence["platform_sources"]
    evidence_path = f"reports/2026-05-12-individual-commerce-geo-audit/evidence/{slug}.json"
    lines = [
        f"# {site_name(slug)} GEO 개별 감사 리포트",
        "",
        "## 메타데이터",
        "",
        f"- report_id: commerce-geo-individual-{slug}-2026-05-12",
        f"- generated_at: {evidence['generated_at']}",
        f"- scope: {evidence['url']}",
        "- score_type: readiness",
        "- evidence_label: live_public_surface_capture",
        f"- confidence: {classification['confidence']}",
        f"- evidence_path: `{evidence_path}`",
        "- last_verified: 2026-05-12",
        "- measurement_status: not measured",
        "- commerce_status: product/schema only",
        "- private_surface_status: public only",
        "- regional_context: named region: Korea / Korean ecommerce",
        "- policy_risk: caution",
        "",
        "## Executive Conclusion",
        "",
        f"- 준비도 점수: {classification['readiness_score']}/100",
        f"- 검색/AI crawler 접근 준비: {'가능' if classification['search_access_ready'] else '제한 또는 미확인'}",
        f"- 루트 HTML merchant schema: {'확인' if classification['merchant_schema_on_root'] else '미확인'}",
        "- 이 점수는 public crawl/readiness 점수이며, AI 답변 노출·citation·referral·conversion 성과가 측정됐다는 뜻이 아니다.",
        "",
        "## Scope And Evidence",
        "",
        f"- robots.txt: `{robots['url']}` status=`{robots['status']}`",
        f"- homepage: `{homepage['final_url'] or homepage['url']}` status=`{homepage['status']}`",
        f"- homepage server: {homepage.get('server') or '미확인'}",
        f"- challenge signal: {homepage.get('challenge_signal') or '미확인'}",
        f"- title: {html['title'] or '미확인'}",
        f"- meta description: {html['meta_description'] or '미확인'}",
        f"- canonical: {html['canonical'] or '미확인'}",
        f"- JSON-LD types: {', '.join(html['json_ld_types']) if html['json_ld_types'] else '미확인'}",
        f"- sitemap count from robots.txt: {len(robots['sitemaps'])}",
        "",
        "## Platform Truth And Access Profile",
        "",
        "| agent | robots 기준 루트 접근 |",
        "| --- | --- |",
    ]
    for agent in AGENTS:
        lines.append(f"| `{agent}` | {yes_no(policy.get(agent))} |")
    lines.extend(
        [
            "",
            "공식 기준: OpenAI는 `OAI-SearchBot`을 ChatGPT Search 노출 관리 표면으로, `GPTBot`을 학습 crawler 표면으로, `ChatGPT-User`를 사용자 요청 fetcher로 분리한다. Google merchant listing은 `Product`와 `Offer` structured data 및 Search Console 검증을 요구한다. Anthropic은 `ClaudeBot`, `Claude-SearchBot`, `Claude-User`를 용도별로 분리한다.",
            "",
            "근거 URL:",
            "",
            f"- OpenAI crawlers: {platform_sources['openai']}",
            f"- Google crawlers: {platform_sources['google_crawlers']}",
            f"- Google merchant listing structured data: {platform_sources['google_merchant']}",
            f"- Anthropic crawler controls: {platform_sources['anthropic']}",
            "",
            "## Measurement Status",
            "",
            "- observed_answer: 미측정",
            "- observed_citation: 미측정",
            "- referral_signal: 미측정",
            "- conversion_signal: 미측정",
            "- 필요한 다음 측정: 동일 query set으로 ChatGPT Search/Google AI/Perplexity/Claude 결과 캡처, Search Console merchant listing report, 서버 로그의 AI crawler hit, referral UTMs.",
            "",
            "## Commerce / Action Status",
            "",
            "- 루트 URL만 수집했으므로 상품 상세 템플릿 전체의 Product/Offer 품질은 확정하지 않는다.",
            "- merchant listing readiness는 상품 상세 URL 샘플, 가격/재고/배송/반품 필드, canonical, robots 접근성을 별도 검증해야 한다.",
            "",
            "## Policy Risk Gate",
            "",
            "- public evidence only 기준으로 작성했다.",
            "- robots.txt 허용은 visibility 보장이 아니며, 차단/미확인은 원인 분석이 필요한 risk로만 취급한다.",
            "",
            "## Prioritized Remediation Plan",
            "",
        ]
    )
    blockers = classification["blockers"]
    if blockers:
        for index, item in enumerate(blockers, 1):
            lines.append(f"{index}. {item}")
    else:
        lines.append("1. 루트 표면의 기본 crawl/readiness는 양호하므로 상품 상세 URL 표본 기반 merchant schema 검증으로 넘어간다.")
    lines.extend(
        [
            "",
            "## Remaining Gaps And Next Verification",
            "",
            "- 상품 상세 URL 10개 이상에서 Product/Offer/price/availability/shipping/return markup을 샘플링한다.",
            "- robots 정책 변경 후 최소 24시간 이상 경과한 뒤 OpenAI/Anthropic crawler 접근을 로그로 재확인한다.",
            "- AI answer/citation 결과는 readiness와 별도 evidence set으로 저장한다.",
            "",
        ]
    )
    (out_dir / f"{slug}.GEO-개별-감사-리포트.md").write_text("\n".join(lines), encoding="utf-8")


def write_summary(out_dir: Path, evidence_items: list[dict[str, object]]) -> None:
    lines = [
        "# Commerce GEO 개별 감사 요약",
        "",
        "- generated_at: " + dt.datetime.now(dt.timezone.utc).isoformat(),
        "- scope: Coupang, Gmarket, Musinsa, Olive Young public root URL live audit",
        "- score_type: readiness",
        "- measurement_status: not measured",
        "",
        "| site | readiness | homepage | robots | OAI-SearchBot | Claude-SearchBot | root merchant schema | report |",
        "| --- | ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for evidence in evidence_items:
        slug = str(evidence["slug"])
        classification = evidence["classification"]
        homepage = evidence["homepage"]
        robots = evidence["robots"]
        policy = evidence["robots_policy"]
        lines.append(
            f"| {site_name(slug)} | {classification['readiness_score']} | {homepage['status']} | {robots['status']} | "
            f"{yes_no(policy.get('OAI-SearchBot'))} | {yes_no(policy.get('Claude-SearchBot'))} | "
            f"{'확인' if classification['merchant_schema_on_root'] else '미확인'} | "
            f"[report](./{slug}.GEO-개별-감사-리포트.md) |"
        )
    lines.extend(
        [
            "",
            "이 요약은 public live capture 기반 readiness 비교다. AI 답변 노출, citation, referral, conversion은 별도 측정 전까지 주장하지 않는다.",
            "",
        ]
    )
    (out_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    evidence_dir = out_dir / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    items: list[dict[str, object]] = []
    for slug, url in SITES.items():
        evidence = audit_site(slug, url)
        items.append(evidence)
        (evidence_dir / f"{slug}.json").write_text(
            json.dumps(evidence, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        write_report(out_dir, evidence)
    (evidence_dir / "summary.json").write_text(
        json.dumps(items, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_summary(out_dir, items)


if __name__ == "__main__":
    sys.exit(main())
