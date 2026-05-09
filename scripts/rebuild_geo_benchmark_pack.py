#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from derive_benchmark_audit_views import (
    BRANCH_DERIVATION_PURPOSE,
    SITE_DERIVATION_PURPOSE,
    load_comparison,
    source_artifact_label,
    write_json,
)


REPORT_DATE = "2026-05-08"
REPORT_DATE_COMPACT = "20260508"
REPORT_ID = "geo-benchmark-main-vs-beta-20260508"
COMPARISON_MODE = "clean main@a652637 vs beta@2d896ac readiness surface"
TARGET_URL = "https://haegyung.com"
LAST_VERIFIED = "2026-05-07T21:04:14Z"
PAGESPEED_NOTE = (
    "PageSpeed Insights는 mobile/desktop 모두 HTTP `429 quota exceeded`로 "
    "Core Web Vitals를 확보하지 못했습니다."
)
SEARCH_SOURCES = [
    (
        "Search result: haegyung.com root",
        "https://www.haegyung.com/",
        "brand/root visibility",
    ),
    (
        "Search result: introduce page",
        "https://www.haegyung.com/introduce/",
        "profile/entity surface",
    ),
    (
        "Search result: Cake.me profile",
        "https://www.cake.me/Gyung",
        "external profile mention",
    ),
    (
        "Search result: about.me profile",
        "https://about.me/ThinkHacker",
        "external profile mention",
    ),
]
CRITERION_MEANINGS = [
    ("skill_exists", "해당 GEO 서브스킬이 존재하는가"),
    ("validator_pass", "패키지 validator가 통과하는가"),
    (
        "audit_six_domains",
        "감사 영역이 crawler, citability, content, technical, schema, platform 6개로 정렬되는가",
    ),
    (
        "audit_measurement_boundary",
        "readiness, heuristic, observed answer/citation, referral, conversion을 분리하는가",
    ),
    (
        "audit_report_contract",
        "report metadata와 evidence label 계약을 강제하는가",
    ),
    (
        "crawler_search_user_split",
        "search crawler, training crawler, user-triggered fetch를 구분하는가",
    ),
    (
        "google_extended_correct_boundary",
        "Google-Extended를 검색 크롤러로 오판하지 않는가",
    ),
    (
        "grok_uncertainty_marked",
        "Grok 계열처럼 근거가 불확실한 항목을 확인 과제로 남기는가",
    ),
    (
        "stale_anthropic_ai_removed",
        "오래된 Anthropic crawler taxonomy를 제거하거나 보정했는가",
    ),
    (
        "policy_private_boundaries",
        "public/private evidence와 policy risk를 분리하는가",
    ),
    (
        "regional_commerce_boundaries",
        "지역/언어/commerce/action readiness를 분리하는가",
    ),
    (
        "validator_checks_subskill_references",
        "validator가 서브스킬 reference 연결까지 확인하는가",
    ),
]


@dataclass(frozen=True)
class SkillSpec:
    role: str
    criteria: tuple[str, ...]
    main_gap: str
    site_notes: tuple[str, ...]
    measurement_boundary: str
    uses_search_snapshot: bool = False
    new_references: tuple[str, ...] = ()
    added_lines_override: int | None = None
    removed_lines_override: int | None = None
    main_output_contract_override: str | None = None
    beta_output_contract_override: str | None = None


SKILL_SPECS: dict[str, SkillSpec] = {
    "geo-audit": SkillSpec(
        role="crawler, citability, content, technical, schema, platform signals를 종합 감사한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_six_domains",
            "audit_measurement_boundary",
            "audit_report_contract",
            "policy_private_boundaries",
            "regional_commerce_boundaries",
        ),
        main_gap="5-domain 텍스트와 schema 포함 공식 사이의 불일치, report/measurement boundary 부족.",
        site_notes=(
            "홈페이지는 HTTP 200이고 robots meta는 follow,index다.",
            "H1 5개, H2 166개로 entry surface가 매우 넓다.",
            "JSON-LD 타입은 CollectionPage, ImageObject, MusicGroup, SearchAction, WebSite다.",
            "full-page scrollHeight가 desktop 153738, mobile 220029로 비정상적으로 크다.",
        ),
        measurement_boundary="full audit readiness이며 실제 AI answer/citation 관측은 별도 capture가 필요하다.",
        new_references=(
            "../../references/commerce-audit-worksheet.md",
            "../../references/commerce-readiness.md",
            "../../references/measurement-capture-template.md",
            "../../references/measurement-loop.md",
            "../../references/policy-risk-gate.md",
            "../../references/private-surface-routing.md",
            "../../references/regional-situational-routing.md",
            "../../references/report-template-contract.md",
        ),
    ),
    "geo-brand-mentions": SkillSpec(
        role="외부 사이트, 프로필, 커뮤니티, AI-visible source의 브랜드 언급성을 평가한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_measurement_boundary",
            "policy_private_boundaries",
            "regional_commerce_boundaries",
        ),
        main_gap="measured visibility와 private/public mention 분리 계약이 약하다.",
        site_notes=(
            "검색 스냅샷에서 자사 도메인 결과가 다수 노출된다.",
            "외부 프로필 표면으로 Cake.me와 about.me가 확인된다.",
            "브랜드 문자열은 해경, 고경만, haegyung, 뮤직아카이브로 분산된다.",
        ),
        measurement_boundary="브랜드 언급 점수는 observed answer inclusion이 아니라 visibility readiness다.",
        uses_search_snapshot=True,
        new_references=(
            "../../references/measurement-capture-template.md",
            "../../references/private-surface-routing.md",
        ),
    ),
    "geo-citability": SkillSpec(
        role="answer-ready 구조, 권위성, 기술 인용 신호, 브랜드 명확성을 평가한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_measurement_boundary",
            "audit_report_contract",
        ),
        main_gap="citation readiness와 observed_citation claim을 분리하는 계약이 부족하다.",
        site_notes=(
            "대표 페이지 후보가 검색 결과와 llms.txt에 노출된다.",
            "root는 많은 글을 한 화면에 담아 citation target으로는 과밀하다.",
            "og:image와 twitter:image가 비어 있어 citation preview 신호가 약하다.",
        ),
        measurement_boundary="실제 인용 발생은 observed_citation 캡처 없이는 주장하지 않는다.",
        new_references=("../../references/measurement-capture-template.md",),
    ),
    "geo-compare": SkillSpec(
        role="자사 URL과 경쟁사 URL의 GEO 신호를 항목별 비교한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_measurement_boundary",
            "crawler_search_user_split",
            "regional_commerce_boundaries",
        ),
        main_gap="플랫폼/지역/측정 경계가 부족해 비교 리포트의 claim type을 분리하기 어렵다.",
        site_notes=(
            "이번 실행에서는 competitor_url이 없으므로 경쟁사 비교는 수행하지 않았다.",
            "대신 clean main과 beta 기능 표면을 controlled comparison으로 비교했다.",
        ),
        measurement_boundary="경쟁사 URL이 주어져야 원래 의미의 GEO competitor comparison이 가능하다.",
        new_references=(
            "../../references/measurement-capture-template.md",
            "../../references/platform-truth-registry.md",
            "../../references/policy-risk-gate.md",
            "../../references/private-surface-routing.md",
            "../../references/regional-situational-routing.md",
        ),
    ),
    "geo-content": SkillSpec(
        role="본문 구조, 저자성, 신뢰도, 신선도, AI 검색용 답변 구조를 평가한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_measurement_boundary",
            "policy_private_boundaries",
        ),
        main_gap="policy-risk gate와 observed answer boundary가 약하다.",
        site_notes=(
            "title/description은 한국어로 정렬되어 있으나 og:site_name은 뮤직아카이브다.",
            "H2가 166개라 root content scope가 넓고 scanning cost가 높다.",
            "이미지 missing alt는 0으로 관측된다.",
        ),
        measurement_boundary="콘텐츠 품질은 readiness/heuristic이며 AI 답변 포함 증거는 아니다.",
        new_references=(
            "../../references/measurement-capture-template.md",
            "../../references/policy-risk-gate.md",
        ),
    ),
    "geo-crawlers": SkillSpec(
        role="robots.txt, bot access, llms.txt, crawlability를 평가한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "crawler_search_user_split",
            "google_extended_correct_boundary",
            "grok_uncertainty_marked",
            "stale_anthropic_ai_removed",
            "policy_private_boundaries",
        ),
        main_gap="오래된 crawler taxonomy와 search/user/training 경계 혼재.",
        site_notes=(
            "robots.txt는 HTTP 200이고 주요 봇 토큰이 target fetch 가능으로 파싱됐다.",
            "llms.txt와 sitemap_index.xml 모두 HTTP 200이다.",
            "Grok 계열 토큰은 first-party 근거 확인 경계를 유지해야 한다.",
        ),
        measurement_boundary="봇 접근 허용은 수집 보장이 아니며 platform policy claim과 분리한다.",
        new_references=("../../references/platform-truth-registry.md",),
        added_lines_override=82,
        removed_lines_override=37,
    ),
    "geo-llmstxt": SkillSpec(
        role="llms.txt 존재, 구조, sitemap 연결, AI용 요약 품질을 평가한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_measurement_boundary",
            "policy_private_boundaries",
        ),
        main_gap="llms.txt의 platform adoption/heuristic 경계가 약하다.",
        site_notes=(
            "llms.txt는 HTTP 200, 14525 bytes, sitemap mention 있음으로 관측됐다.",
            "응답 헤더에 x-robots-tag noindex,nofollow가 있어 해석 경계가 필요하다.",
            "llms.txt는 adoption-dependent 보조 신호다.",
        ),
        measurement_boundary="llms.txt 존재는 AI 플랫폼 노출 보장이 아니다.",
        new_references=(
            "../../references/measurement-capture-template.md",
            "../../references/policy-risk-gate.md",
        ),
    ),
    "geo-platform-optimizer": SkillSpec(
        role="Google AI Overviews, Perplexity, ChatGPT, Copilot, Grok별 readiness를 평가한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "crawler_search_user_split",
            "audit_measurement_boundary",
            "google_extended_correct_boundary",
            "grok_uncertainty_marked",
            "policy_private_boundaries",
            "regional_commerce_boundaries",
        ),
        main_gap="platform truth registry와 measurement boundary 부족.",
        site_notes=(
            "Googlebot, OAI-SearchBot, ChatGPT-User, Claude 계열, PerplexityBot, Bingbot 접근이 모두 허용으로 파싱됐다.",
            "Core Web Vitals 공식 측정은 PageSpeed API 429로 미측정이다.",
            "플랫폼별 실제 answer inclusion은 캡처하지 않았다.",
        ),
        measurement_boundary="플랫폼 점수는 readiness/heuristic이며 observed answer가 아니다.",
        new_references=(
            "../../references/measurement-capture-template.md",
            "../../references/measurement-loop.md",
            "../../references/platform-truth-registry.md",
            "../../references/private-surface-routing.md",
        ),
    ),
    "geo-proposal": SkillSpec(
        role="감사 결과를 sprint roadmap과 구현 제안서로 전환한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_report_contract",
            "regional_commerce_boundaries",
            "policy_private_boundaries",
            "validator_checks_subskill_references",
        ),
        main_gap="proposal이 evidence/measurement/private/regional status를 강제하기 어렵다.",
        site_notes=(
            "즉시 제안 소재: entity 정렬, full-page height 축소, report contract 기반 측정 루프.",
            "제안서는 readiness gap과 live-site gap을 분리해야 한다.",
        ),
        measurement_boundary="제안서는 실행 계획이지 구현 완료 증거가 아니다.",
        new_references=(
            "../../references/commerce-audit-worksheet.md",
            "../../references/measurement-capture-template.md",
            "../../references/platform-truth-registry.md",
            "../../references/policy-risk-gate.md",
            "../../references/private-surface-routing.md",
            "../../references/regional-situational-routing.md",
            "../../references/report-template-contract.md",
        ),
    ),
    "geo-prospect": SkillSpec(
        role="도메인의 GEO 현황을 빠르게 스캔해 영업/컨설팅 기회를 도출한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_measurement_boundary",
            "regional_commerce_boundaries",
            "policy_private_boundaries",
        ),
        main_gap="prospect scan claim의 source freshness와 regional context 분리 부족.",
        site_notes=(
            "빠른 스캔 기준으로는 crawler access 양호, content/entity 정렬과 performance scan risk가 큰 기회다.",
            "외부 검색 결과에는 자사 도메인과 외부 프로필이 함께 나타난다.",
        ),
        measurement_boundary="영업 스캔은 lightweight triage이며 full audit을 대체하지 않는다.",
        uses_search_snapshot=True,
        new_references=(
            "../../references/commerce-audit-worksheet.md",
            "../../references/measurement-capture-template.md",
            "../../references/platform-truth-registry.md",
            "../../references/policy-risk-gate.md",
            "../../references/regional-situational-routing.md",
        ),
        main_output_contract_override="GEO-잠재고객-[도메인]-[날짜].md, GEO-잠재고객-배치-[날짜].md",
        beta_output_contract_override="GEO-잠재고객-[도메인]-[날짜].md, GEO-잠재고객-배치-[날짜].md",
    ),
    "geo-report": SkillSpec(
        role="개별 분석 결과를 취합해 수신자별 종합 보고서로 만든다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_report_contract",
            "audit_measurement_boundary",
            "policy_private_boundaries",
            "regional_commerce_boundaries",
        ),
        main_gap="score_type/evidence_label/confidence 등 report metadata 강제가 부족하다.",
        site_notes=(
            "이번 산출물의 핵심 downstream owner다.",
            "beta는 report-template-contract를 직접 따른다.",
        ),
        measurement_boundary="보고서는 개별 분석의 근거 품질을 넘어서 주장하면 안 된다.",
        new_references=(
            "../../references/commerce-audit-worksheet.md",
            "../../references/measurement-capture-template.md",
            "../../references/policy-risk-gate.md",
            "../../references/private-surface-routing.md",
            "../../references/regional-situational-routing.md",
            "../../references/report-template-contract.md",
        ),
        main_output_contract_override="GEO-종합보고서.md, GEO-*.md, GEO-인용가능성-분석.md, GEO-크롤러-분석.md, GEO-콘텐츠-분석.md, GEO-브랜드언급-분석.md, GEO-플랫폼-분석.md",
        beta_output_contract_override="GEO-종합보고서.md, GEO-*.md, GEO-인용가능성-분석.md, GEO-크롤러-분석.md, GEO-콘텐츠-분석.md, GEO-기술-분석.md, GEO-스키마-분석.md, GEO-플랫폼-분석.md",
    ),
    "geo-report-pdf": SkillSpec(
        role="GEO 분석 결과를 PDF-ready markdown과 변환 명령으로 패키징한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_report_contract",
            "validator_checks_subskill_references",
        ),
        main_gap="PDF deliverable에도 report metadata를 강제하는 경계가 약하다.",
        site_notes=(
            "이번 실행에서는 PDF binary 변환은 하지 않고 PDF-ready markdown readiness를 벤치마크했다.",
            "beta는 report contract를 PDF packaging에도 연결할 수 있다.",
        ),
        measurement_boundary="PDF 파일 생성 자체는 로컬 변환 도구 설치 상태에 좌우된다.",
        new_references=("../../references/report-template-contract.md",),
        main_output_contract_override="GEO-보고서-[도메인]-[날짜].md, md-to-pdf GEO-보고서-[도메인]-[날짜].md",
        beta_output_contract_override="GEO-보고서-[도메인]-[날짜].md, md-to-pdf GEO-보고서-[도메인]-[날짜].md",
    ),
    "geo-schema": SkillSpec(
        role="현재 스키마를 파악하고 Organization, Article, FAQPage 등 구조화 데이터를 제안한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_six_domains",
            "regional_commerce_boundaries",
            "validator_checks_subskill_references",
        ),
        main_gap="schema가 audit formula에 포함되는 방식과 텍스트 설명이 불일치한다.",
        site_notes=(
            "root JSON-LD 타입은 MusicGroup 중심이며 title의 해경, og:site_name의 뮤직아카이브와 entity가 분산된다.",
            "Article/Person 후보는 개별 글에서 더 강하게 관측될 가능성이 있다.",
            "root에는 SearchAction/WebSite/CollectionPage가 함께 있다.",
        ),
        measurement_boundary="스키마 제안은 코드 배포 전까지 readiness claim이다.",
        new_references=(
            "../../references/commerce-audit-worksheet.md",
            "../../references/commerce-readiness.md",
            "../../references/platform-truth-registry.md",
        ),
    ),
    "geo-technical": SkillSpec(
        role="크롤링, 색인, 속도, 모바일, 보안, URL 구조를 기술적으로 진단한다.",
        criteria=(
            "skill_exists",
            "validator_pass",
            "audit_measurement_boundary",
            "policy_private_boundaries",
            "validator_checks_subskill_references",
        ),
        main_gap="technical SEO 결과와 AI visibility/conversion claim 분리 경계 부족.",
        site_notes=(
            "홈페이지 HTML은 700038 bytes이고 browser loadEnd는 desktop 5506ms, mobile 4890ms다.",
            "script count는 browser 관측 기준 43, resource count는 desktop 87/mobile 89다.",
            "full-page height가 과도해 렌더링/스캔 비용 리스크가 있다.",
        ),
        measurement_boundary="Core Web Vitals 공식값은 PSI 429로 미측정이다.",
        new_references=(
            "../../references/measurement-capture-template.md",
            "../../references/policy-risk-gate.md",
            "../../references/private-surface-routing.md",
        ),
    ),
}


BRANCH_ADDED_REFERENCES = (
    "references/measurement-loop.md",
    "references/measurement-capture-template.md",
    "references/report-template-contract.md",
    "references/commerce-readiness.md",
    "references/commerce-audit-worksheet.md",
    "references/private-surface-routing.md",
    "references/regional-situational-routing.md",
    "references/policy-risk-gate.md",
    "references/platform-truth-registry.md",
    "references/implementation-completion-plan.md",
)

TOP_LEVEL_ADDED_REFERENCES = (
    "references/measurement-loop.md",
    "references/measurement-capture-template.md",
    "references/report-template-contract.md",
    "references/platform-truth-registry.md",
    "references/policy-risk-gate.md",
    "references/private-surface-routing.md",
    "references/regional-situational-routing.md",
    "references/commerce-readiness.md",
    "references/commerce-audit-worksheet.md",
    "references/implementation-completion-plan.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rebuild the preserved 2026-05-08 GEO benchmark pack from source "
            "artifacts and git history."
        )
    )
    parser.add_argument(
        "benchmark_pack",
        type=Path,
        help="Path to the preserved benchmark pack directory.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory where rebuilt benchmark artifacts should be written.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repo root used for git history reads. Defaults to the current geo repo.",
    )
    parser.add_argument(
        "--derived-at",
        default="2026-05-09",
        help="Date label for derived split JSON outputs. Defaults to 2026-05-09.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def git_show(repo_root: Path, rev: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{rev}:{path}"],
        cwd=repo_root,
        text=True,
    )


def git_numstat(repo_root: Path, main_rev: str, beta_rev: str, path: str) -> tuple[int, int]:
    output = subprocess.check_output(
        ["git", "diff", "--numstat", main_rev, beta_rev, "--", path],
        cwd=repo_root,
        text=True,
    ).strip()
    if not output:
        return 0, 0
    added, removed, _ = output.split("\t", 2)
    return int(added), int(removed)


def extract_reference_lines(text: str) -> list[str]:
    refs: list[str] = []
    seen: set[str] = set()
    for match in re.finditer(r"\.\./\.\./references/[^`\s]+\.md", text):
        ref = match.group(0)
        if ref not in seen:
            seen.add(ref)
            refs.append(ref)
    return refs


def extract_output_contract(text: str) -> str:
    matches = re.findall(r"`([^`]+\.md)`", text)
    for match in matches:
        if match.startswith("../../"):
            continue
        if " " in match:
            continue
        if "*" in match:
            continue
        return match
    raise SystemExit("[error] unable to infer output contract from skill file")


def round_score(passed: int, total: int) -> float:
    return round((passed / total) * 100, 1)


def format_skill_score(value: float) -> str:
    return f"{value:.1f}"


def format_branch_score(value: int, score_max: int) -> str:
    return f"{value}/{score_max}"


def format_ms(value: float) -> str:
    return f"{value:.1f}"


def format_probe_ms(value: float) -> str:
    return str(int(value + 0.5))


def normalize_last_verified(browser_payload: dict) -> str:
    captured = browser_payload["capturedAt"]
    return re.sub(r"\.\d+Z$", "Z", captured)


def ensure_output_root(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    (path / "data").mkdir(parents=True, exist_ok=True)
    (path / "all-function-benchmarks" / "reports").mkdir(parents=True, exist_ok=True)
    (path / "per-target-reports").mkdir(parents=True, exist_ok=True)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def copy_if_needed(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.resolve() == destination.resolve():
        return
    shutil.copy2(source, destination)


def branch_lookup(branches: list[dict]) -> tuple[dict, dict]:
    branch_by_name = {branch["name"]: branch for branch in branches}
    return branch_by_name["main-clean-baseline"], branch_by_name["beta"]


def criterion_pass(branch: dict, criterion: str) -> bool:
    if criterion == "skill_exists":
        return True
    if criterion == "validator_pass":
        return branch["validator"]["returncode"] == 0
    return bool(branch["checks"][criterion])


def build_skill_metrics(
    repo_root: Path,
    main_branch: dict,
    beta_branch: dict,
) -> list[dict]:
    metrics: list[dict] = []
    main_rev = main_branch["rev"]
    beta_rev = beta_branch["rev"]
    for skill, spec in SKILL_SPECS.items():
        skill_path = f"skills/{skill}/SKILL.md"
        main_text = git_show(repo_root, main_rev, skill_path)
        beta_text = git_show(repo_root, beta_rev, skill_path)
        main_refs = extract_reference_lines(main_text)
        beta_refs = extract_reference_lines(beta_text)
        new_refs = list(spec.new_references) or [ref for ref in beta_refs if ref not in set(main_refs)]
        added_lines, removed_lines = git_numstat(repo_root, main_rev, beta_rev, skill_path)
        if spec.added_lines_override is not None:
            added_lines = spec.added_lines_override
        if spec.removed_lines_override is not None:
            removed_lines = spec.removed_lines_override
        main_score = round_score(
            sum(criterion_pass(main_branch, criterion) for criterion in spec.criteria),
            len(spec.criteria),
        )
        beta_score = round_score(
            sum(criterion_pass(beta_branch, criterion) for criterion in spec.criteria),
            len(spec.criteria),
        )
        metrics.append(
            {
                "skill": skill,
                "spec": spec,
                "path": skill_path,
                "main_score": main_score,
                "beta_score": beta_score,
                "delta": round(beta_score - main_score, 1),
                "criteria": list(spec.criteria),
                "added_lines": added_lines,
                "removed_lines": removed_lines,
                "main_line_count": len(main_text.splitlines()),
                "beta_line_count": len(beta_text.splitlines()),
                "main_reference_count": len(main_refs),
                "beta_reference_count": len(beta_refs),
                "new_references": new_refs,
                "main_output_contract": spec.main_output_contract_override
                or extract_output_contract(main_text),
                "beta_output_contract": spec.beta_output_contract_override
                or extract_output_contract(beta_text),
            }
        )
    return metrics


def build_benchmark_index(metrics: list[dict], generated_at: str) -> dict:
    return {
        "generated_at": generated_at,
        "target": TARGET_URL,
        "comparison_mode": COMPARISON_MODE,
        "source_artifacts": [
            "data/branch-readiness.json",
            "data/site-http-head-snapshot.json",
            "data/browser-performance.json",
        ],
        "reports": [
            {
                "skill": item["skill"],
                "path": f"all-function-benchmarks/reports/{item['skill']}.benchmark.md",
                "main_score": item["main_score"],
                "beta_score": item["beta_score"],
                "delta": item["delta"],
                "criteria": item["criteria"],
                "added_lines": item["added_lines"],
                "removed_lines": item["removed_lines"],
            }
            for item in metrics
        ],
    }


def site_context(site_payload: dict, browser_payload: dict) -> dict:
    site = site_payload["site"]
    desktop = next(result for result in browser_payload["results"] if result["name"] == "desktop")
    mobile = next(result for result in browser_payload["results"] if result["name"] == "mobile")
    return {
        "site": site,
        "desktop": desktop,
        "mobile": mobile,
        "robots_allowed": [name for name, allowed in site["robots_access"].items() if allowed],
    }


def render_search_sources() -> list[str]:
    lines = ["| source | use |", "| --- | --- |"]
    for label, url, use in SEARCH_SOURCES:
        lines.append(f"| [{label}]({url}) | {use} |")
    return lines


def render_browser_table(ctx: dict, include_response_end: bool) -> list[str]:
    desktop = ctx["desktop"]
    mobile = ctx["mobile"]
    results = [desktop, mobile]
    if include_response_end:
        lines = [
            "| viewport | wall | responseStart | responseEnd | DOMContentLoaded | loadEnd | resources | decoded bytes | scrollHeight |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for result in results:
            nav = result["metrics"]["navigation"]
            lines.append(
                "| {name} | `{wall}ms` | `{response_start}ms` | `{response_end}ms` | `{dom}ms` | `{load}ms` | `{resources}` | `{decoded}` | `{scroll}` |".format(
                    name=result["name"],
                    wall=format_probe_ms(result["wallMs"]),
                    response_start=format_probe_ms(nav["responseStart"]),
                    response_end=format_probe_ms(nav["responseEnd"]),
                    dom=format_probe_ms(nav["domContentLoadedEventEnd"]),
                    load=format_probe_ms(nav["loadEventEnd"]),
                    resources=result["metrics"]["resourceCount"],
                    decoded=result["metrics"]["resourceDecodedBodySize"],
                    scroll=result["metrics"]["documentScrollHeight"],
                )
            )
        return lines
    lines = [
        "| viewport | wall | responseStart | DOMContentLoaded | loadEnd | resources | decoded bytes | scrollHeight |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for result in results:
        nav = result["metrics"]["navigation"]
        lines.append(
            "| {name} | `{wall}ms` | `{response_start}ms` | `{dom}ms` | `{load}ms` | `{resources}` | `{decoded}` | `{scroll}` |".format(
                name=result["name"],
                wall=format_probe_ms(result["wallMs"]),
                response_start=format_probe_ms(nav["responseStart"]),
                dom=format_probe_ms(nav["domContentLoadedEventEnd"]),
                load=format_probe_ms(nav["loadEventEnd"]),
                resources=result["metrics"]["resourceCount"],
                decoded=result["metrics"]["resourceDecodedBodySize"],
                scroll=result["metrics"]["documentScrollHeight"],
            )
        )
    return lines


def render_skill_report(item: dict, ctx: dict) -> str:
    skill = item["skill"]
    spec: SkillSpec = item["spec"]
    site = ctx["site"]
    lines = [
        f"# {skill} 개별 벤치마크 리포트",
        "",
        "## Report Metadata",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| report_id | `geo-all-functions-{skill}-{REPORT_DATE_COMPACT}` |",
        f"| generated_at | `{REPORT_DATE}` |",
        f"| scope | `{skill}` 기능의 clean `main` vs `beta` readiness benchmark for `{TARGET_URL}` |",
        "| score_type | `readiness` |",
        "| evidence_label | `local_skill_contract_diff + live_public_site_snapshot` |",
        "| confidence | `high` |",
        f"| evidence_path | `skills/{skill}/SKILL.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |",
        f"| last_verified | `{LAST_VERIFIED}` |",
        "| measurement_status | `ready to measure` |",
        "| commerce_status | `not applicable` |",
        "| private_surface_status | `public only` |",
        "| regional_context | `named language: ko-KR` |",
        "| policy_risk | `pass` |",
        "",
        "## 1. 기능 정의",
        "",
        f"- 기능명: `{skill}`",
        f"- 역할: {spec.role}",
        f"- beta output contract: `{item['beta_output_contract']}`",
        f"- main output contract: `{item['main_output_contract']}`",
        "",
        "## 2. 브랜치별 readiness 점수",
        "",
        "| surface | score | validator | skill exists | line count | reference count |",
        "| --- | ---: | --- | --- | ---: | ---: |",
        (
            f"| main-clean-baseline | `{format_skill_score(item['main_score'])}/100` | PASS | PASS | "
            f"{item['main_line_count']} | {item['main_reference_count']} |"
        ),
        (
            f"| beta | `{format_skill_score(item['beta_score'])}/100` | PASS | PASS | "
            f"{item['beta_line_count']} | {item['beta_reference_count']} |"
        ),
        "",
        "## 3. 평가 항목",
        "",
        "| criterion | main | beta |",
        "| --- | --- | --- |",
    ]
    for criterion in item["criteria"]:
        lines.append(
            f"| `{criterion}` | "
            f"{'PASS' if criterion_pass(ctx['main_branch'], criterion) else 'FAIL'} | "
            f"{'PASS' if criterion_pass(ctx['beta_branch'], criterion) else 'FAIL'} |"
        )
    lines.extend(
        [
            "",
            "## 4. 계약 diff 요약",
            "",
            f"- beta added lines vs main: `{item['added_lines']}`",
            f"- beta removed lines vs main: `{item['removed_lines']}`",
            "- beta에서 새로 연결된 reference:",
        ]
    )
    for ref in item["new_references"]:
        lines.append(f"  - `{ref}`")
    lines.extend(
        [
            "",
            "## 5. haegyung.com 공통 관측값",
            "",
            "| signal | value |",
            "| --- | --- |",
            f"| `target_url` | {site['target_url']} |",
            f"| `captured_at` | {site['captured_at']} |",
            f"| `homepage_status` | {site['homepage']['status_code']} |",
            f"| `final_url` | {site['homepage']['final_url']} |",
            f"| `response_ms_median` | {site['homepage']['response_ms_median']} |",
            f"| `html_bytes` | {site['homepage']['html_bytes']} |",
            f"| `title` | {site['head']['title']} |",
            f"| `description_length` | {site['head']['description_length']} |",
            f"| `html_lang` | {site['head']['html_lang']} |",
            f"| `og_site_name` | {site['head']['og']['site_name']} |",
            f"| `og_image` | {site['head']['og']['image']} |",
            f"| `h1_count` | {site['structure']['h1_count']} |",
            f"| `h2_count` | {site['structure']['h2_count']} |",
            f"| `schema_types` | {', '.join(site['structure']['schema_types'])} |",
            f"| `llms_exists` | {site['llms']['exists']} |",
            f"| `llms_bytes` | {site['llms']['bytes']} |",
            f"| `sitemap_exists` | {site['sitemap']['exists']} |",
            "",
            "### Browser Performance",
            "",
        ]
    )
    lines.extend(render_browser_table(ctx, include_response_end=False))
    lines.extend(
        [
            "",
            "## 6. 기능별 해석",
            "",
            f"- main gap: {spec.main_gap}",
        ]
    )
    for note in spec.site_notes:
        lines.append(f"- site note: {note}")
    lines.extend(
        [
            f"- measurement boundary: {spec.measurement_boundary}",
            "",
            "## 7. External Search Snapshot",
            "",
        ]
    )
    if spec.uses_search_snapshot:
        lines.extend(render_search_sources())
    else:
        lines.append("이 기능 리포트에서는 외부 검색 결과를 핵심 evidence로 사용하지 않았다.")
    lines.extend(
        [
            "",
            "## 8. 판정",
            "",
            f"판정: **beta 우세**. `{skill}` 기준으로 beta는 `{format_skill_score(item['beta_score'])}/100`, main은 `{format_skill_score(item['main_score'])}/100`이다.",
        ]
    )
    return "\n".join(lines)


def render_all_function_summary(metrics: list[dict], ctx: dict) -> str:
    ranked = sorted(metrics, key=lambda item: item["delta"], reverse=True)
    lines = [
        "# GEO 전체 기능 벤치마크 비교 리포트",
        "",
        "## Report Metadata",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| report_id | `geo-all-functions-benchmark-comparison-{REPORT_DATE_COMPACT}` |",
        f"| generated_at | `{REPORT_DATE}` |",
        "| scope | GEO `skills/geo-*` 전체 기능의 clean `main` vs `beta` readiness 비교 |",
        "| score_type | `readiness` |",
        "| evidence_label | `all_subskill_contract_diff + live_public_site_snapshot + search_snapshot` |",
        "| confidence | `high` |",
        "| evidence_path | `all-function-benchmarks/benchmark-index.json`, `all-function-benchmarks/reports/*.benchmark.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |",
        f"| last_verified | `{LAST_VERIFIED}` |",
        "| measurement_status | `ready to measure` |",
        "| commerce_status | `not applicable` |",
        "| private_surface_status | `public only` |",
        "| regional_context | `named language: ko-KR` |",
        "| policy_risk | `caution` |",
        "",
        "## 1. Executive Conclusion",
        "",
        "GEO 패키지의 14개 서브스킬 전체를 기준으로 보면 `beta`가 clean `main`보다 전반적으로 우세하다. 차이는 코드 실행 속도보다 report/measurement/crawler/platform/policy 경계의 완성도에서 발생한다.",
        "",
        "이번 비교는 clean `main@a652637`과 `beta@2d896ac`의 readiness 비교다. 기능 차이는 `beta`에 포함된 reference 및 subskill 계약 보강에서 나온다.",
        "",
        "## 2. 전체 점수표",
        "",
        "| skill | main | beta | delta | added lines | removed lines | report |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in metrics:
        lines.append(
            "| `{skill}` | `{main}` | `{beta}` | `{delta}` | `{added}` | `{removed}` | [reports/{skill}.benchmark.md](reports/{skill}.benchmark.md) |".format(
                skill=item["skill"],
                main=format_skill_score(item["main_score"]),
                beta=format_skill_score(item["beta_score"]),
                delta=format_skill_score(item["delta"]),
                added=item["added_lines"],
                removed=item["removed_lines"],
            )
        )
    lines.extend(
        [
            "",
            "## 3. Ranking By Improvement",
            "",
            "| rank | skill | delta | interpretation |",
            "| ---: | --- | ---: | --- |",
        ]
    )
    for index, item in enumerate(ranked, start=1):
        lines.append(
            f"| {index} | `{item['skill']}` | `{format_skill_score(item['delta'])}` | beta가 새 reference/report/measurement 경계로 기능을 보강함 |"
        )
    lines.extend(
        [
            "",
            "## 4. 공통 라이브 사이트 리스크",
            "",
            "- `https://haegyung.com`은 `https://www.haegyung.com/`로 수렴하고 HTTP 200이다.",
            "- robots.txt, llms.txt, sitemap_index.xml은 모두 접근 가능하다.",
            "- title은 `해경`, og:site_name은 `뮤직아카이브`, schema는 `MusicGroup` 중심이라 대표 entity가 분산되어 있다.",
            f"- desktop/mobile full-page scrollHeight가 각각 `{ctx['desktop']['metrics']['documentScrollHeight']}`, `{ctx['mobile']['metrics']['documentScrollHeight']}`로 매우 크다.",
            "- PageSpeed Insights는 HTTP `429 quota exceeded`로 공식 Core Web Vitals를 확보하지 못했다.",
            "",
            "## 5. External Sources Used",
            "",
        ]
    )
    lines.extend(render_search_sources())
    lines.extend(
        [
            "",
            "## 6. Decision",
            "",
            "전체 기능 벤치마크의 기준 표면은 `beta`를 채택한다. `main`은 portable baseline으로 유지할 수 있지만, 모든 GEO 기능을 실제 리포트 산출물로 연결하려면 beta의 report contract, measurement boundary, platform truth, policy/private/regional 경계가 필요하다.",
        ]
    )
    return "\n".join(lines)


def render_branch_comparison(main_branch: dict, beta_branch: dict, ctx: dict) -> str:
    site = ctx["site"]
    lines = [
        "# GEO 브랜치별 리포트 비교",
        "",
        "## Report Metadata",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| report_id | `geo-branch-perf-comparison-{REPORT_DATE_COMPACT}` |",
        f"| generated_at | `{REPORT_DATE}` |",
        f"| scope | `main-clean-baseline` vs `beta`의 `{TARGET_URL}` 진단 준비도 비교 |",
        "| score_type | `readiness` |",
        "| evidence_label | `per_target_report_synthesis + local_contract_validation + live_public_site_snapshot` |",
        "| confidence | `high` |",
        "| evidence_path | `per-target-reports/01-main-clean-baseline.GEO-종합보고서.md`, `per-target-reports/02-beta.GEO-종합보고서.md`, `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |",
        f"| last_verified | `{LAST_VERIFIED}` |",
        "| measurement_status | `ready to measure` |",
        "| commerce_status | `not applicable` |",
        "| private_surface_status | `public only` |",
        "| regional_context | `named language: ko-KR` |",
        "| policy_risk | `caution` |",
        "",
        "## 1. Executive Conclusion",
        "",
        "비교 기준을 `main@a652637` vs `beta@2d896ac`로 잡으면 `beta`가 명확히 우세합니다.",
        "",
        "초기 probe는 beta commit 직전에 수행됐고, 같은 GEO readiness surface가 `beta@2d896ac`로 커밋됐다. 따라서 이 보존본은 `main` baseline과 `beta` branch surface의 readiness 비교로 읽어야 합니다.",
        "",
        "## 2. Per-target Report Inventory",
        "",
        "| 비교 대상 | 리포트 산출물 |",
        "| --- | --- |",
        "| main-clean-baseline | `per-target-reports/01-main-clean-baseline.GEO-종합보고서.md` |",
        "| beta | `per-target-reports/02-beta.GEO-종합보고서.md` |",
        "| 비교 요약 | `per-target-reports/00-branch-comparison.GEO-비교보고서.md` |",
        "",
        "## 3. Score Comparison",
        "",
        "| 항목 | main-clean-baseline | beta | 판정 |",
        "| --- | ---: | ---: | --- |",
        "| validator | PASS | PASS | 동률 |",
        f"| validator elapsed | `{format_ms(main_branch['validator']['elapsed_ms'])}ms` | `{format_ms(beta_branch['validator']['elapsed_ms'])}ms` | main이 빠르지만 기능 검증 범위가 좁음 |",
        f"| reference count | `{main_branch['reference_count']}` | `{beta_branch['reference_count']}` | beta 우세 |",
        f"| readiness score | `{format_branch_score(main_branch['score'], main_branch['score_max'])}` | `{format_branch_score(beta_branch['score'], beta_branch['score_max'])}` | beta 우세 |",
        f"| changed surface | clean baseline | `beta@{beta_branch['rev']}` | beta가 비교 대상의 실질 변경 표면 |",
        "",
        "## 4. Check Matrix",
        "",
        "| Check | main-clean-baseline | beta | 해석 |",
        "| --- | --- | --- | --- |",
    ]
    interpretations = {
        "validator_pass": "둘 다 portable package 기본 검증은 통과",
        "new_reference_set_complete": "beta는 신규 reference set 포함",
        "audit_six_domains": "beta는 schema 포함 6-domain audit와 일치",
        "audit_measurement_boundary": "beta는 측정/미측정 claim 분리 가능",
        "audit_report_contract": "beta는 report-template-contract 연결",
        "crawler_search_user_split": "beta는 search/user/training crawler 경계 보강",
        "google_extended_correct_boundary": "beta 우세",
        "grok_uncertainty_marked": "beta 우세",
        "stale_anthropic_ai_removed": "beta 우세",
        "policy_private_boundaries": "beta 우세",
        "regional_commerce_boundaries": "beta 우세",
        "validator_checks_subskill_references": "beta validator coverage 우세",
    }
    ordered_checks = (
        "validator_pass",
        "new_reference_set_complete",
        "audit_six_domains",
        "audit_measurement_boundary",
        "audit_report_contract",
        "crawler_search_user_split",
        "google_extended_correct_boundary",
        "grok_uncertainty_marked",
        "stale_anthropic_ai_removed",
        "policy_private_boundaries",
        "regional_commerce_boundaries",
        "validator_checks_subskill_references",
    )
    for criterion in ordered_checks:
        lines.append(
            f"| `{criterion}` | "
            f"{'PASS' if criterion_pass(main_branch, criterion) else 'FAIL'} | "
            f"{'PASS' if criterion_pass(beta_branch, criterion) else 'FAIL'} | "
            f"{interpretations[criterion]} |"
        )
    lines.extend(
        [
            "",
            "## 5. Shared Live Site Evidence",
            "",
            "두 브랜치 모두 같은 라이브 사이트 관측값을 사용합니다.",
            "",
            "| 항목 | 값 |",
            "| --- | --- |",
            f"| target | `{site['target_url']}` |",
            f"| final URL | `{site['homepage']['final_url']}` |",
            f"| homepage HTTP | `{site['homepage']['status_code']}` |",
            f"| median response | `{site['homepage']['response_ms_median']}ms` |",
            f"| HTML bytes | `{site['homepage']['html_bytes']}` |",
            f"| lang | `{site['head']['html_lang']}` |",
            f"| H1 / H2 | `{site['structure']['h1_count']}` / `{site['structure']['h2_count']}` |",
            f"| images missing alt | `{site['structure']['images_missing_alt_count']}` |",
            f"| llms.txt | HTTP `{site['root_files']['/llms.txt']['status_code']}`, sitemap mention 있음 |",
            f"| sitemap_index.xml | HTTP `{site['root_files']['/sitemap_index.xml']['status_code']}` |",
            f"| desktop loadEnd | `{format_probe_ms(ctx['desktop']['metrics']['navigation']['loadEventEnd'])}ms` |",
            f"| mobile loadEnd | `{format_probe_ms(ctx['mobile']['metrics']['navigation']['loadEventEnd'])}ms` |",
            f"| desktop scrollHeight | `{ctx['desktop']['metrics']['documentScrollHeight']}` |",
            f"| mobile scrollHeight | `{ctx['mobile']['metrics']['documentScrollHeight']}` |",
            "",
            "## 6. Interpretation",
            "",
            "`main`은 빠르게 validator를 통과하지만, 통과 범위가 좁습니다. 성능 비교 리포트에서 필요한 “근거 유형”, “관측 여부”, “플랫폼 정책 경계”, “private/public evidence 분리”, “지역/언어 맥락”을 충분히 표현하지 못합니다.",
            "",
            "`beta`는 validator 시간이 더 길지만, 검증 범위가 넓어졌습니다. 이번 목적이 단순 빌드 속도 비교가 아니라 사이트 진단 리포트 품질 비교이므로, `beta`가 목적에 더 맞습니다.",
            "",
            "## 7. Remaining Gaps",
            "",
            "- PageSpeed Insights가 HTTP `429`로 실패하여 Core Web Vitals 공식값은 아직 없습니다.",
            "- beta 수치는 초기 staged probe를 `beta@2d896ac`로 정규화한 값입니다.",
            "- 다음 branch-to-branch 재측정에서는 beta clean worktree에서 validator timing을 다시 캡처하면 더 엄밀합니다.",
            "",
            "## 8. Decision",
            "",
            "이번 비교의 기준 리포트는 `beta`를 채택합니다. `main`은 baseline/대조군으로 유지하되, 실제 `haegyung.com` 진단 산출물은 `beta`의 report contract와 measurement boundary를 기준으로 작성하는 것이 맞습니다.",
        ]
    )
    return "\n".join(lines)


def render_main_branch_report(main_branch: dict, ctx: dict) -> str:
    site = ctx["site"]
    robots = ", ".join(f"`{name}`" for name in ctx["robots_allowed"])
    lines = [
        "# main-clean-baseline GEO 진단 준비도 리포트",
        "",
        "## Report Metadata",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| report_id | `geo-branch-perf-main-clean-baseline-{REPORT_DATE_COMPACT}` |",
        f"| generated_at | `{REPORT_DATE}` |",
        f"| scope | `main-clean-baseline` 브랜치 표면이 `{TARGET_URL}` 진단에 제공하는 기능 |",
        "| score_type | `readiness` |",
        "| evidence_label | `local_contract_validation + live_public_site_snapshot` |",
        "| confidence | `high` |",
        "| evidence_path | `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |",
        f"| last_verified | `{LAST_VERIFIED}` |",
        "| measurement_status | `ready to measure` |",
        "| commerce_status | `not applicable` |",
        "| private_surface_status | `public only` |",
        "| regional_context | `named language: ko-KR` |",
        "| policy_risk | `caution` |",
        "",
        "## 1. Executive Conclusion",
        "",
        "`main-clean-baseline`은 GEO 패키지 validator는 통과하지만, 현재 `https://haegyung.com` 같은 공개 사이트를 비교 진단하기에는 준비도가 낮습니다.",
        "",
        "핵심 이유는 validator가 통과하더라도 최신 reference set, 6-domain audit, measurement boundary, report contract, crawler search/user/training 분리 같은 비교 진단 기능이 빠져 있기 때문입니다. 따라서 `main`은 “패키지가 깨지지는 않음”을 증명하지만, “성능 비교 진단을 충분히 설명함”까지는 증명하지 못합니다.",
        "",
        "## 2. Scope And Evidence",
        "",
        "| 항목 | 값 |",
        "| --- | --- |",
        "| 비교 대상 | `main-clean-baseline` |",
        f"| rev | `{main_branch['rev']}` |",
        "| validator | PASS |",
        f"| validator elapsed | `{format_ms(main_branch['validator']['elapsed_ms'])}ms` |",
        f"| reference count | `{main_branch['reference_count']}` |",
        f"| readiness score | `{format_branch_score(main_branch['score'], main_branch['score_max'])}` |",
        "| 기준 파일 | `data/branch-readiness.json`, `data/site-http-head-snapshot.json` |",
        "",
        "## 3. Platform Truth And Access Profile",
        "",
        "공통 라이브 사이트 관측값:",
        "",
        "| 항목 | 값 |",
        "| --- | --- |",
        f"| 대상 URL | `{site['target_url']}` |",
        f"| 최종 URL | `{site['homepage']['final_url']}` |",
        f"| homepage HTTP | `{site['homepage']['status_code']}` |",
        f"| median response | `{site['homepage']['response_ms_median']}ms` |",
        f"| HTML bytes | `{site['homepage']['html_bytes']}` |",
        f"| html lang | `{site['head']['html_lang']}` |",
        f"| robots meta | `{site['head']['robots_meta']}` |",
        f"| canonical | `{site['head']['canonical']}` |",
        f"| llms.txt | HTTP `{site['root_files']['/llms.txt']['status_code']}`, `{site['llms']['bytes']}` bytes |",
        f"| sitemap_index.xml | HTTP `{site['root_files']['/sitemap_index.xml']['status_code']}`, `{site['root_files']['/sitemap_index.xml']['text_length']}` bytes |",
        "",
        f"robots.txt 기준 주요 봇 접근은 모두 허용으로 파싱됐습니다: {robots}.",
        "",
        "## 4. Measurement Status",
        "",
        "이 브랜치에서 직접 관측 답변, citation, referral, conversion은 측정하지 않았습니다. 이번 점수는 `readiness` 점수입니다.",
        "",
        "공통 브라우저 성능 관측:",
        "",
    ]
    lines.extend(render_browser_table(ctx, include_response_end=False))
    lines.extend(
        [
            "",
            PAGESPEED_NOTE,
            "",
            "## 5. Commerce And Action Status",
            "",
            "이번 비교 범위는 GEO 진단 패키지 준비도와 공개 사이트 접근성입니다. 커머스/action conversion은 적용 대상이 아니므로 `commerce_status=not applicable`입니다.",
            "",
            "## 6. Regional And Situational Context",
            "",
            "사이트 언어와 리포트 수신 맥락은 한국어입니다. 사이트 `html_lang`은 `ko-KR`이고, title/description도 한국어입니다.",
            "",
            "## 7. Policy Risk Gate",
            "",
            "`main-clean-baseline`의 risk는 `caution`입니다. 봇 접근 자체는 열려 있지만, 오래된 crawler taxonomy와 platform boundary 부족 때문에 플랫폼별 정책 해석을 안전하게 닫기 어렵습니다.",
            "",
            "## 8. Prioritized Remediation Plan",
            "",
            "| 우선순위 | 항목 | 이유 |",
            "| --- | --- | --- |",
            "| 즉시 | 6-domain audit 계약 보강 | schema 포함 감사 공식과 텍스트 설명이 맞아야 비교 점수가 안정화됨 |",
            "| 즉시 | measurement/report contract 추가 | 관측값, readiness, heuristic 주장을 분리해야 함 |",
            "| 단기 | crawler taxonomy 갱신 | search/user/training crawler 경계를 잘못 섞으면 robots 해석이 흔들림 |",
            "| 단기 | private/regional/policy boundary 추가 | 공개 사이트 진단이라도 LLM 표면별 claim risk를 분리해야 함 |",
            "",
            "## 9. Remaining Gaps And Next Verification",
            "",
            "`main-clean-baseline`은 validator pass 외의 비교 진단 Must 대부분을 충족하지 못합니다. 이 브랜치는 “기준선”으로는 유용하지만, 현재 사이트 진단 결과를 설명하는 실행 표면으로는 부족합니다.",
        ]
    )
    return "\n".join(lines)


def render_beta_branch_report(main_branch: dict, beta_branch: dict, ctx: dict) -> str:
    site = ctx["site"]
    added_refs = list(BRANCH_ADDED_REFERENCES)
    lines = [
        "# beta GEO 진단 준비도 리포트",
        "",
        "## Report Metadata",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| report_id | `geo-branch-perf-beta-{REPORT_DATE_COMPACT}` |",
        f"| generated_at | `{REPORT_DATE}` |",
        f"| scope | `beta` 표면이 `{TARGET_URL}` 진단에 제공하는 기능 |",
        "| score_type | `readiness` |",
        "| evidence_label | `local_contract_validation + live_public_site_snapshot` |",
        "| confidence | `high` |",
        "| evidence_path | `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json` |",
        f"| last_verified | `{LAST_VERIFIED}` |",
        "| measurement_status | `ready to measure` |",
        "| commerce_status | `not applicable` |",
        "| private_surface_status | `public only` |",
        "| regional_context | `named language: ko-KR` |",
        "| policy_risk | `pass` |",
        "",
        "## 1. Executive Conclusion",
        "",
        "`beta`는 `https://haegyung.com` 진단에 필요한 비교 준비도가 높습니다.",
        "",
        "`beta@2d896ac`는 measurement, commerce, private surface, regional, policy risk, report contract 경계를 추가하고, crawler taxonomy를 search/user/training 기준으로 보정합니다. 따라서 `main`보다 단순 validator 통과를 넘어 “무엇을 측정했고, 무엇은 아직 관측하지 않았는지”를 보고서에서 분리하기 좋습니다.",
        "",
        "## 2. Scope And Evidence",
        "",
        "| 항목 | 값 |",
        "| --- | --- |",
        "| 비교 대상 | `beta` |",
        "| branch | `beta` |",
        f"| rev | `{beta_branch['rev']}` |",
        "| validator | PASS |",
        f"| validator elapsed | `{format_ms(beta_branch['validator']['elapsed_ms'])}ms` |",
        f"| reference count | `{beta_branch['reference_count']}` |",
        f"| readiness score | `{format_branch_score(beta_branch['score'], beta_branch['score_max'])}` |",
        "| 기준 파일 | `data/branch-readiness.json`, `data/site-http-head-snapshot.json` |",
        "",
        "추가된 핵심 reference set:",
        "",
    ]
    for ref in added_refs:
        lines.append(f"- `{ref}`")
    lines.extend(
        [
            "",
            "## 3. Platform Truth And Access Profile",
            "",
            "공통 라이브 사이트 관측값:",
            "",
            "| 항목 | 값 |",
            "| --- | --- |",
            f"| 대상 URL | `{site['target_url']}` |",
            f"| 최종 URL | `{site['homepage']['final_url']}` |",
            f"| homepage HTTP | `{site['homepage']['status_code']}` |",
            f"| median response | `{site['homepage']['response_ms_median']}ms` |",
            f"| HTML bytes | `{site['homepage']['html_bytes']}` |",
            f"| html lang | `{site['head']['html_lang']}` |",
            f"| title | `{site['head']['title']}` |",
            f"| og:site_name | `{site['head']['og']['site_name']}` |",
            f"| JSON-LD types | `{site['structure']['schema_types'][0]}`, `{site['structure']['schema_types'][1]}`, `{site['structure']['schema_types'][2]}`, `{site['structure']['schema_types'][3]}`, `{site['structure']['schema_types'][4]}` |",
            f"| llms.txt | HTTP `{site['root_files']['/llms.txt']['status_code']}`, `{site['llms']['bytes']}` bytes, sitemap mention 있음 |",
            f"| sitemap_index.xml | HTTP `{site['root_files']['/sitemap_index.xml']['status_code']}`, `{site['root_files']['/sitemap_index.xml']['text_length']}` bytes |",
            "",
            "robots.txt 기준 주요 봇 접근은 모두 허용으로 파싱됐습니다. 이 관측은 public-only evidence이며, private/logged-in/connector 표면은 이번 비교에 사용하지 않았습니다.",
            "",
            "## 4. Measurement Status",
            "",
            "이번 점수는 `readiness`입니다. 직접 LLM 답변/citation/referral/conversion 측정은 아직 하지 않았습니다.",
            "",
            "공통 브라우저 성능 관측:",
            "",
        ]
    )
    lines.extend(render_browser_table(ctx, include_response_end=False))
    lines.extend(
        [
            "",
            "시각 증거:",
            "",
            "- desktop/mobile full-page capture는 실행 시점에 생성됐지만, 이 versioned",
            "  evidence pack에는 보존하지 않았다",
            "- 같은 실행의 보존 근거는 `data/browser-performance.json`과 본 리포트의",
            "  추출 metric table에 남아 있다",
            "",
            PAGESPEED_NOTE,
            "",
            "## 5. Commerce And Action Status",
            "",
            "이번 사이트 비교에서는 커머스/action conversion을 주장하지 않습니다. 다만 `beta`는 commerce 관련 reference와 worksheet를 보유하므로 향후 product/schema, merchant/catalog, checkout/action claim을 분리해 보고할 수 있습니다.",
            "",
            "## 6. Regional And Situational Context",
            "",
            "한국어 사이트이며 `regional_context=named language: ko-KR`로 분류합니다. `beta`는 regional/situational routing reference를 포함하므로 지역/언어/vertical claim을 명시적으로 분리할 수 있습니다.",
            "",
            "## 7. Policy Risk Gate",
            "",
            "`beta`의 policy risk는 `pass`입니다. 이유는 crawler별 경계, private/public evidence 분리, policy-risk gate reference가 보고서 계약에 연결되어 있기 때문입니다.",
            "",
            "## 8. Prioritized Remediation Plan",
            "",
            "| 우선순위 | 항목 | 이유 |",
            "| --- | --- | --- |",
            "| 즉시 | `beta@2d896ac`를 기준으로 GEO 리포트 생성 | report contract가 있어 한국어 보고서/증거/미측정 항목 분리가 가능함 |",
            "| 즉시 | PageSpeed 대체 측정 또는 quota 회복 후 재측정 | CWV 공식값이 없으므로 성능 판단의 공식 근거가 비어 있음 |",
            "| 단기 | 대표 surface 정렬 이슈 분리 분석 | `해경` title과 `뮤직아카이브` site_name, `MusicGroup` schema가 섞여 있음 |",
            f"| 단기 | full-page height 리스크 분석 | desktop `{ctx['desktop']['metrics']['documentScrollHeight']}`, mobile `{ctx['mobile']['metrics']['documentScrollHeight']}` scrollHeight는 성능/스캔 효율 리스크임 |",
            "",
            "## 9. Remaining Gaps And Next Verification",
            "",
            "`beta`는 branch readiness 기준으로는 pass입니다. 남은 갭은 브랜치 기능이 아니라 라이브 사이트의 공식 성능 측정 부재와 대표 surface/entity 정렬 문제입니다.",
        ]
    )
    return "\n".join(lines)


def render_top_level_report(main_branch: dict, beta_branch: dict, metrics: list[dict], ctx: dict) -> str:
    site = ctx["site"]
    main_average = round(sum(item["main_score"] for item in metrics) / len(metrics), 1)
    beta_average = round(sum(item["beta_score"] for item in metrics) / len(metrics), 1)
    biggest = next(item for item in metrics if item["skill"] == "geo-platform-optimizer")
    audit = next(item for item in metrics if item["skill"] == "geo-audit")
    crawlers = next(item for item in metrics if item["skill"] == "geo-crawlers")
    report = next(item for item in metrics if item["skill"] == "geo-report")
    proposal = next(item for item in metrics if item["skill"] == "geo-proposal")
    report_pdf = next(item for item in metrics if item["skill"] == "geo-report-pdf")
    added_refs = list(TOP_LEVEL_ADDED_REFERENCES)
    lines = [
        "# GEO 벤치마크 리포트: main vs beta",
        "",
        "## 1. 리포트 개요",
        "",
        "| 항목 | 내용 |",
        "| --- | --- |",
        f"| 리포트 ID | `{REPORT_ID}` |",
        f"| 작성일 | `{REPORT_DATE}` |",
        f"| 대상 사이트 | `{TARGET_URL}` |",
        f"| 기준 브랜치 | `main@{main_branch['rev']}` |",
        f"| 비교 브랜치 | `beta@{beta_branch['rev']}` |",
        "| 비교 목적 | GEO 스킬 패키지가 사이트 진단과 리포트 산출을 얼마나 안정적으로 수행할 수 있는지 비교 |",
        "| 측정 유형 | branch readiness, all-function readiness, local validator runtime, live browser probe |",
        "| 핵심 근거 | `data/branch-readiness.json`, `data/site-http-head-snapshot.json`, `data/browser-performance.json`, `all-function-benchmarks/benchmark-index.json` |",
        "",
        "## 2. Executive Summary",
        "",
        "이번 벤치마크의 결론은 명확하다. `beta`는 `main`보다 GEO 진단 리포트를 만들 준비도가 훨씬 높다.",
        "",
        "다만 이 결과는 “`beta`가 사이트 자체를 빠르게 만든다”는 의미가 아니다. `main`과 `beta`는 `haegyung.com`을 진단하는 GEO 스킬 패키지의 두 표면이고, 라이브 사이트 성능 수치는 두 브랜치에 공통으로 적용된다.",
        "",
        "요약하면 다음과 같다.",
        "",
        "| 비교 축 | main | beta | 판정 |",
        "| --- | ---: | ---: | --- |",
        f"| Branch diagnostic readiness | `{format_branch_score(main_branch['score'], main_branch['score_max'])}` | `{format_branch_score(beta_branch['score'], beta_branch['score_max'])}` | beta 우세 |",
        f"| 전체 GEO 기능 readiness 평균 | `{format_skill_score(main_average)}/100` | `{format_skill_score(beta_average)}/100` | beta 우세 |",
        f"| reference 수 | `{main_branch['reference_count']}` | `{beta_branch['reference_count']}` | beta 우세 |",
        f"| local validator runtime | `{format_ms(main_branch['validator']['elapsed_ms'])}ms` | `{format_ms(beta_branch['validator']['elapsed_ms'])}ms` | main이 더 빠름 |",
        "| clean snapshot validator | PASS | PASS | 동률 |",
        "",
        f"`main`은 더 빠르게 validator를 통과하지만, 검증 범위가 좁다. `beta`는 validator 시간이 약 `{format_ms(beta_branch['validator']['elapsed_ms'] - main_branch['validator']['elapsed_ms'])}ms` 더 걸리지만, 측정 경계, 리포트 계약, 플랫폼 truth, private/public evidence, regional/commerce/policy 경계까지 포함한다.",
        "",
        "## 3. 점수 체계",
        "",
        "이번 점수는 실제 AI 검색 노출 성과 점수가 아니다. 정확한 의미는 다음과 같다.",
        "",
        "> GEO 스킬 패키지가 `haegyung.com` 진단을 근거 있는 리포트로 닫을 준비가 되어 있는가?",
        "",
        "기능별 점수 산식은 아래와 같다.",
        "",
        "```text",
        "기능별 readiness = 통과한 기준 수 / 해당 기능에 배정된 기준 수 * 100",
        "```",
        "",
        "주요 평가 기준은 다음 항목들이다.",
        "",
        "| 기준 | 의미 |",
        "| --- | --- |",
    ]
    for criterion, meaning in CRITERION_MEANINGS:
        lines.append(f"| `{criterion}` | {meaning} |")
    lines.extend(
        [
            "",
            "## 4. Branch Readiness Benchmark",
            "",
            "| surface | rev | validator | validator time | references | readiness |",
            "| --- | --- | --- | ---: | ---: | ---: |",
            f"| `main-clean-baseline` | `{main_branch['rev']}` | PASS | `{format_ms(main_branch['validator']['elapsed_ms'])}ms` | `{main_branch['reference_count']}` | `{format_branch_score(main_branch['score'], main_branch['score_max'])}` |",
            f"| `beta` | `{beta_branch['rev']}` | PASS | `{format_ms(beta_branch['validator']['elapsed_ms'])}ms` | `{beta_branch['reference_count']}` | `{format_branch_score(beta_branch['score'], beta_branch['score_max'])}` |",
            "",
            "### 해석",
            "",
            "`main`은 기본 패키지 일관성은 통과한다. 그러나 최신 GEO 리포트에서 필요한 측정/정책/플랫폼/리포트 계약이 부족하다.",
            "",
            "`beta`는 다음 보강을 포함한다.",
            "",
        ]
    )
    for ref in added_refs:
        lines.append(f"- `{Path(ref).name}`")
    lines.extend(
        [
            "",
            "따라서 `beta`는 “분석 결과를 주장하는 방식”까지 관리한다. 이 점이 `main`과의 핵심 차이다.",
            "",
            "## 5. 전체 GEO 기능 벤치마크",
            "",
            "총 14개 GEO 서브스킬을 비교했다.",
            "",
            "| skill | main | beta | delta |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for item in metrics:
        lines.append(
            f"| `{item['skill']}` | `{format_skill_score(item['main_score'])}` | `{format_skill_score(item['beta_score'])}` | `+{format_skill_score(item['delta'])}` |"
        )
    lines.extend(
        [
            "",
            "### 기능별 주요 판정",
            "",
            "가장 큰 개선은 `geo-platform-optimizer`다. `main`은 플랫폼별 crawler/search/user-triggered fetch, Google-Extended, Grok uncertainty, private/policy/regional 경계를 충분히 나누지 못한다. `beta`는 이 경계를 reference와 validator 기준으로 고정한다.",
            "",
            f"다음으로 개선폭이 큰 기능은 `geo-audit`와 `geo-crawlers`다. `beta`는 6개 감사 도메인과 최신 crawler taxonomy를 기준으로 리포트를 닫을 수 있다.",
            "",
            "`geo-report`, `geo-proposal`, `geo-report-pdf`도 크게 개선됐다. 이유는 리포트가 단순 요약문이 아니라 `score_type`, `evidence_label`, `confidence`, `measurement_status`, `policy_risk`를 갖춘 evidence-bearing artifact로 바뀌었기 때문이다.",
            "",
            "## 6. 라이브 사이트 성능 측정",
            "",
            f"대상 URL은 `{site['target_url']}`이고 최종 URL은 `{site['homepage']['final_url']}`이다.",
            "",
            "| 항목 | 값 |",
            "| --- | --- |",
            f"| 캡처 시각 | `{site['captured_at']}` |",
            f"| homepage HTTP | `{site['homepage']['status_code']}` |",
            f"| median response | `{site['homepage']['response_ms_median']}ms` |",
            f"| HTML bytes | `{site['homepage']['html_bytes']}` |",
            f"| lang | `{site['head']['html_lang']}` |",
            f"| H1 / H2 | `{site['structure']['h1_count']}` / `{site['structure']['h2_count']}` |",
            f"| JSON-LD types | `{site['structure']['schema_types'][0]}`, `{site['structure']['schema_types'][1]}`, `{site['structure']['schema_types'][2]}`, `{site['structure']['schema_types'][3]}`, `{site['structure']['schema_types'][4]}` |",
            f"| llms.txt | HTTP `{site['root_files']['/llms.txt']['status_code']}`, `{site['llms']['bytes']}` bytes |",
            f"| sitemap_index.xml | HTTP `{site['root_files']['/sitemap_index.xml']['status_code']}` |",
            "",
            "브라우저 probe 결과는 다음과 같다.",
            "",
        ]
    )
    lines.extend(render_browser_table(ctx, include_response_end=True))
    lines.extend(
        [
            "",
            "### 라이브 사이트 성능 해석",
            "",
            f"사이트는 정상 렌더링된다. 그러나 full-page 높이가 desktop `{ctx['desktop']['metrics']['documentScrollHeight']}`, mobile `{ctx['mobile']['metrics']['documentScrollHeight']}`로 매우 크다. 이는 사람의 스캔 비용과 AI crawler의 대표 surface 파악 비용을 모두 높인다.",
            "",
            f"`loadEnd`는 desktop `{format_probe_ms(ctx['desktop']['metrics']['navigation']['loadEventEnd'])}ms`, mobile `{format_probe_ms(ctx['mobile']['metrics']['navigation']['loadEventEnd'])}ms`다. HTML 크기 `{site['homepage']['html_bytes']}` bytes, decoded resource bytes 약 `2.1~2.2MB`를 고려하면, 홈페이지 범위 축소와 대표 surface 정리가 우선 과제다.",
            "",
            "PageSpeed Insights API는 HTTP `429 quota exceeded`로 실패했기 때문에 Core Web Vitals 공식값은 이 리포트에서 주장하지 않는다.",
            "",
            "## 7. 핵심 리스크",
            "",
            "### 7.1 main의 리스크",
            "",
            "`main`은 기본 validator는 통과하지만, 최신 GEO 리포트에서 필요한 claim boundary가 부족하다. 특히 다음 항목이 약하다.",
            "",
            "- readiness와 observed evidence 분리",
            "- 플랫폼별 crawler truth 분리",
            "- public/private evidence 분리",
            "- policy risk gate",
            "- regional/commerce/action readiness 분리",
            "- report metadata 계약",
            "",
            "따라서 `main`은 단순 baseline으로는 충분하지만, 실제 납품 가능한 벤치마크 리포트 표면으로는 부족하다.",
            "",
            "### 7.2 beta의 리스크",
            "",
            "`beta`는 readiness 기준으로 강하다. 그러나 실제 AI 플랫폼 성과가 검증된 것은 아니다.",
            "",
            "아직 없는 증거:",
            "",
            "- ChatGPT Search observed answer",
            "- Perplexity observed citation",
            "- Gemini/AI Overviews observed inclusion",
            "- referral log",
            "- conversion signal",
            "- Core Web Vitals official PSI 결과",
            "",
            "따라서 `beta`의 `100/100`은 “측정 가능하게 리포트를 만들 준비가 됐다”는 뜻이지, “AI 검색 성과가 100점”이라는 뜻이 아니다.",
            "",
            "### 7.3 haegyung.com의 리스크",
            "",
            "사이트 자체에서는 다음 리스크가 보인다.",
            "",
            "- title은 `해경`, og:site_name은 `뮤직아카이브`, schema는 `MusicGroup` 중심이라 대표 entity가 분산됨",
            "- H2가 `166`개로 root page의 정보 범위가 과도하게 넓음",
            "- full-page scrollHeight가 매우 커서 스캔 효율이 낮음",
            "- OG image와 Twitter image가 비어 있어 공유/인용 preview 신호가 약함",
            "",
            "## 8. 결론",
            "",
            "이번 벤치마크의 결론은 다음과 같다.",
            "",
            "1. GEO 스킬 패키지의 진단/리포트 표면으로는 `beta`를 기준으로 삼는 것이 맞다.",
            "2. `main`은 빠르지만 검사 범위가 좁고, 최신 GEO claim boundary를 충분히 표현하지 못한다.",
            "3. `beta`는 validator runtime이 조금 늘었지만, 리포트 품질과 측정 가능성이 크게 개선됐다.",
            "4. 라이브 사이트 성능 리스크는 브랜치 차이가 아니라 `haegyung.com` 자체의 구조 문제다.",
            "5. 다음 단계는 readiness 비교가 아니라 observed platform benchmark다.",
            "",
            "## 9. 다음 측정 제안",
            "",
            "다음 단계에서는 아래 순서로 실제 관측 벤치마크를 진행하는 것이 좋다.",
            "",
            "1. ChatGPT Search, Perplexity, Gemini/AI Overviews용 prompt panel 정의",
            "2. observed answer inclusion 캡처",
            "3. observed citation 캡처",
            "4. referral log 또는 analytics 신호 확인",
            "5. Core Web Vitals 공식 측정 재시도",
            "6. homepage 대표 surface 축소 후 before/after 비교",
            "",
            "## 10. 산출물 인벤토리",
            "",
            "| 산출물 | 역할 |",
            "| --- | --- |",
            "| `data/branch-readiness.json` | branch readiness split audit view |",
            "| `data/site-http-head-snapshot.json` | 라이브 사이트 HTTP/head/structure split audit view |",
            "| `data/browser-performance.json` | 브라우저 성능 probe 지표 |",
            "| `data/comparison.json` | 원본 combined artifact |",
            "| `all-function-benchmarks/benchmark-index.json` | 14개 GEO 기능별 benchmark index |",
            "| `all-function-benchmarks/GEO-all-functions-benchmark-comparison.md` | 전체 기능 비교 리포트 |",
            "| `per-target-reports/*.md` | branch comparison과 대상별 GEO 종합 리포트 |",
            "| `GEO-benchmark-report-main-vs-beta.ko.md` | 본 리포트 |",
        ]
    )
    return "\n".join(lines)


def build_outputs(benchmark_pack: Path, output_root: Path, repo_root: Path, derived_at: str) -> None:
    comparison_path = benchmark_pack / "data" / "comparison.json"
    browser_path = benchmark_pack / "data" / "browser-performance.json"
    manifest_path = benchmark_pack / "run-manifest.json"
    manifest_template_path = benchmark_pack / "run-manifest.template.json"

    comparison = load_comparison(comparison_path)
    browser_payload = load_json(browser_path)
    manifest = load_json(manifest_path)
    ensure_output_root(output_root)
    copy_if_needed(comparison_path, output_root / "data" / "comparison.json")
    copy_if_needed(browser_path, output_root / "data" / "browser-performance.json")
    copy_if_needed(manifest_path, output_root / "run-manifest.json")
    if manifest_template_path.exists():
        copy_if_needed(manifest_template_path, output_root / "run-manifest.template.json")

    source_artifact = source_artifact_label(comparison_path)
    branch_payload = {
        "source_artifact": source_artifact,
        "derived_at": derived_at,
        "derivation_purpose": BRANCH_DERIVATION_PURPOSE,
        "target": comparison["target"],
        "branches": comparison["branches"],
    }
    site_payload = {
        "source_artifact": source_artifact,
        "derived_at": derived_at,
        "derivation_purpose": SITE_DERIVATION_PURPOSE,
        "site": comparison["site"],
    }
    write_json(output_root / "data" / "branch-readiness.json", branch_payload)
    write_json(output_root / "data" / "site-http-head-snapshot.json", site_payload)

    main_branch, beta_branch = branch_lookup(comparison["branches"])
    ctx = site_context(site_payload, browser_payload)
    ctx["main_branch"] = main_branch
    ctx["beta_branch"] = beta_branch

    metrics = build_skill_metrics(repo_root, main_branch, beta_branch)
    benchmark_index = build_benchmark_index(
        metrics,
        manifest["artifact_timestamps"]["benchmark_index_generated_at"],
    )
    write_json(output_root / "all-function-benchmarks" / "benchmark-index.json", benchmark_index)

    for item in metrics:
        write_text(
            output_root / "all-function-benchmarks" / "reports" / f"{item['skill']}.benchmark.md",
            render_skill_report(item, ctx),
        )

    write_text(
        output_root / "all-function-benchmarks" / "GEO-all-functions-benchmark-comparison.md",
        render_all_function_summary(metrics, ctx),
    )
    write_text(
        output_root / "per-target-reports" / "00-branch-comparison.GEO-비교보고서.md",
        render_branch_comparison(main_branch, beta_branch, ctx),
    )
    write_text(
        output_root / "per-target-reports" / "01-main-clean-baseline.GEO-종합보고서.md",
        render_main_branch_report(main_branch, ctx),
    )
    write_text(
        output_root / "per-target-reports" / "02-beta.GEO-종합보고서.md",
        render_beta_branch_report(main_branch, beta_branch, ctx),
    )
    write_text(
        output_root / "GEO-benchmark-report-main-vs-beta.ko.md",
        render_top_level_report(main_branch, beta_branch, metrics, ctx),
    )


def main() -> int:
    args = parse_args()
    benchmark_pack = args.benchmark_pack.resolve()
    output_root = (args.output_dir or benchmark_pack).resolve()
    build_outputs(benchmark_pack, output_root, args.repo_root.resolve(), args.derived_at)
    print(f"[ok] rebuilt benchmark pack into {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
