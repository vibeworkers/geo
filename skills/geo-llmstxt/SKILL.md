---
name: geo-llmstxt
description: >
  llms.txt 파일 존재 여부 확인, 내용 품질 평가, 신규 생성 템플릿 제공.
  AI 크롤러가 사이트 구조를 이해하도록 돕는 llms.txt를 진단하고 최적화한다.
  L2(웹마스터·운영자)와 L3(개발자) 전용 스킬.
  트리거: "llms.txt", "llms", "AI 크롤러 안내 파일".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-llmstxt — llms.txt 진단 및 최적화

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정한다.
> `L1`로 판단되면 아래 안내 메시지를 출력하고 실행을 중단한다.
> `L2` 또는 `L3`로 판단되면 아래 단계를 순서대로 실행한다.
> 결과는 `GEO-llmstxt-분석.md`로 저장한다.

---

## L1 접근 안내 (L1이면 이 메시지 출력 후 중단)

```
llms.txt 설정은 서버 파일 관리가 필요한 기술 작업입니다.

현재 레벨(마케팅 담당자)에서는 직접 실행이 어렵습니다.

선택 사항:
1. 이 작업을 다시 요청할 때 `L2 운영자 프로필로 진행해 주세요.` 또는 `L3 개발자 프로필로 진행해 주세요.`처럼 수신자 레벨을 직접 명시하세요.
2. 개발팀 또는 운영팀에 아래 내용을 전달하세요:

   "사이트 루트에 llms.txt 파일이 있는지 확인하고,
    없다면 AI 크롤러용 안내 파일로 추가해 주세요.
    참고: https://llmstxt.org"
```

---

## 실행 단계

### 1단계: llms.txt 존재 여부 확인

대상 URL에서 도메인을 추출하여 `/llms.txt` 경로를 확인한다.

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests
from urllib.parse import urlparse
url = '[TARGET_URL]'
parsed = urlparse(url)
base = f'{parsed.scheme}://{parsed.netloc}'

targets = ['/llms.txt', '/llms-full.txt']
for path in targets:
    try:
        r = requests.get(base + path, headers={'User-Agent':'GEO-Audit/1.0'}, timeout=15)
        print(f'{path} STATUS: {r.status_code}')
        if r.status_code == 200:
            print(r.text[:3000])
            print('---')
    except Exception as e:
        print(f'{path} ERROR: {e}')
"
```

**Claude 웹 환경 (WebFetch 대체)**

> WebFetch로 아래 두 경로를 순서대로 로드한다.
> - `https://[도메인]/llms.txt`
> - `https://[도메인]/llms-full.txt`
>
> 내용이 반환되면 존재, 오류 페이지 또는 HTML이 반환되면 미존재로 판단한다.
> HTTP 상태 코드를 직접 확인하려면 외부 도구 활용: https://httpstatus.io/

---

### 2단계: llms.txt 내용 품질 평가

llms.txt가 존재하는 경우 아래 항목을 평가한다. 각 항목 0~10점, 합산 100점 만점.

#### 필수 항목 (60점)

| 항목 | 배점 | 확인 기준 |
|---|---|---|
| 사이트 설명 | 20점 | `> [설명]` 형식의 블록쿼트 존재 여부 및 내용 충실도 |
| 주요 URL 목록 | 20점 | `## [섹션명]` 하위에 `- [제목]: [URL]` 형식으로 최소 5개 이상 |
| Sitemap 링크 | 20점 | `## Sitemap` 섹션에 sitemap.xml URL 포함 여부 |

#### 권장 항목 (40점)

| 항목 | 배점 | 확인 기준 |
|---|---|---|
| 섹션 분류 | 15점 | 콘텐츠 유형별(제품/블로그/문서 등) 섹션 구분 여부 |
| 제외 안내 | 10점 | `## Optional` 또는 주석으로 학습에서 제외할 경로 안내 |
| 업데이트 날짜 | 15점 | 파일 내 최종 업데이트 일자 명시 여부 |

**llms.txt 없음:** 0점 처리. 신규 생성 가이드를 출력한다.

---

### 3단계: llms-full.txt 확인

`llms-full.txt`는 각 페이지의 전체 마크다운 내용을 포함하는 확장 파일이다.
AI가 콘텐츠를 더 깊이 학습하도록 돕는다.

- 존재: 파일 크기와 포함된 페이지 수를 확인한다.
- 미존재: 운영 부담이 크므로 권고만 한다 (필수 아님).

---

### 4단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-llmstxt-분석.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L2 출력 — 웹마스터 / 운영자

점수와 함께 FTP·CMS에서 직접 수정하거나 생성할 수 있는 방법을 안내한다.

```markdown
# [도메인] llms.txt 진단 보고서

진단일: [날짜]  |  대상: [도메인]

---

## llms.txt 현황: [존재 / 없음]

[존재 시] **품질 점수: [점수]/100**

| 항목 | 상태 | 설명 |
|---|---|---|
| 사이트 설명 | 있음 / 없음 | [내용 요약 또는 누락 이유] |
| 주요 URL 목록 | 충분 / 부족 / 없음 | [URL 수] 개 등록됨 |
| Sitemap 링크 | 있음 / 없음 | [sitemap URL 또는 누락] |
| 섹션 분류 | 있음 / 없음 | [분류 현황] |
| 제외 안내 | 있음 / 없음 | [제외 경로 현황] |
| 업데이트 날짜 | 있음 / 없음 | [날짜 또는 누락] |

[없음 시] AI 크롤러가 사이트 구조를 파악할 수 없는 상태입니다.
아래 생성 가이드를 참고하여 파일을 만들고 업로드하세요.

---

## 수정·생성 방법

### FTP로 업로드하는 경우

1. 텍스트 편집기(메모장, VSCode 등)로 아래 내용을 작성한다.
2. 파일명: `llms.txt` (소문자, 확장자 포함)
3. FTP 클라이언트(FileZilla 등)로 접속한다.
4. 사이트 루트 디렉토리(`/public_html` 또는 `/www`)에 업로드한다.
5. 브라우저에서 `https://[도메인]/llms.txt` 접속해 내용이 보이면 완료.

### WordPress인 경우

**방법 1 — 플러그인 없이 직접 추가:**
1. WordPress 관리자 → 외모 → 테마 파일 편집기
2. 또는 FTP로 WordPress 루트 디렉토리에 직접 업로드

**방법 2 — Yoast SEO 또는 RankMath 사용 중인 경우:**
- 현재 llms.txt 자동 생성 기능이 없음 → FTP 업로드 방법을 사용한다.

---

## llms.txt 파일 내용

아래 템플릿을 사이트에 맞게 수정하여 사용하세요.

```
# [사이트명] llms.txt
# 최종 업데이트: [날짜]
# AI 크롤러용 사이트 안내 파일

> [사이트에 대한 한두 문장 설명. 어떤 서비스인지, 누구를 위한 사이트인지 명확히 작성]

## 주요 페이지

- 홈: https://[도메인]/
- 소개: https://[도메인]/about/
- 서비스: https://[도메인]/services/
- 블로그: https://[도메인]/blog/
- 연락처: https://[도메인]/contact/

## 주요 콘텐츠

- [콘텐츠 제목]: https://[도메인]/[경로]/
- [콘텐츠 제목]: https://[도메인]/[경로]/

## Sitemap

- https://[도메인]/sitemap.xml

## Optional (선택 — 학습 제외 권고 경로)

- https://[도메인]/admin/
- https://[도메인]/wp-admin/
- https://[도메인]/cart/
- https://[도메인]/checkout/
```

---

## llms-full.txt 현황

**상태:** [존재 / 없음]

[존재 시] 파일 크기 및 포함 페이지 수: [정보]

[없음 시] llms-full.txt는 각 페이지 전체 내용을 포함하는 파일입니다.
AI의 콘텐츠 학습 품질을 높이지만 유지 관리 부담이 큽니다.
정기 업데이트가 가능한 경우에만 개발팀에 생성을 요청하세요.
```

---

### L3 출력 — 개발자

전체 기술 명세, 파일 구조 검증, 자동화 스크립트를 포함한다.

```markdown
# [도메인] llms.txt Technical Audit

Date: [날짜]  |  Target: [도메인]

---

## llms.txt Status

| File | HTTP Status | Size | Last-Modified |
|---|---|---|---|
| /llms.txt | [200 / 404] | [bytes] | [날짜 또는 N/A] |
| /llms-full.txt | [200 / 404] | [bytes] | [날짜 또는 N/A] |

---

## Quality Score: [점수]/100

| 항목 | 점수 | 상태 | 발견 내용 |
|---|---|---|---|
| 사이트 설명 (블록쿼트) | [X]/20 | ✅ / ❌ | [내용] |
| 주요 URL 목록 | [X]/20 | ✅ / ❌ | [URL 수]개 |
| Sitemap 링크 | [X]/20 | ✅ / ❌ | [URL 또는 누락] |
| 섹션 분류 | [X]/15 | ✅ / ❌ | [섹션 수]개 |
| 제외 안내 | [X]/10 | ✅ / ❌ | [경로 수]개 |
| 업데이트 날짜 | [X]/15 | ✅ / ❌ | [날짜 또는 누락] |

---

## Current llms.txt Content

```
[실제 파일 내용 전체 — 없으면 "파일 없음" 표기]
```

---

## Critical Issues

[문제가 있는 경우만 출력]

### [CRITICAL] llms.txt 없음
현재: /llms.txt → 404
영향: AI 크롤러(ClaudeBot, GPTBot, PerplexityBot 등)가 사이트 구조를 자동 파악해야 하므로
      중요 페이지가 누락되거나 잘못 분류될 가능성 있음
해결: 아래 생성 스크립트 또는 수동으로 파일 생성 후 사이트 루트에 배포

### [WARNING] 사이트 설명 없음
현재: 블록쿼트(`> `) 형식의 설명 미존재
영향: AI가 사이트 맥락을 파악하지 못해 인용 시 부정확한 설명 생성 가능
해결: 파일 상단에 `> [한두 문장 설명]` 추가

### [WARNING] Sitemap 링크 없음
현재: `## Sitemap` 섹션 없음
영향: 크롤러가 추가 페이지 발견을 robots.txt·HTML 파싱에 의존해야 함
해결: `## Sitemap` 섹션과 sitemap.xml URL 추가

---

## 권장 llms.txt 구조

```
# [사이트명] llms.txt
# Last-Updated: [YYYY-MM-DD]

> [사이트 설명 — 무엇을 제공하는지, 대상 독자는 누구인지 명확히 작성]

## 주요 페이지

- 홈: https://[도메인]/
- 소개: https://[도메인]/about/
- 서비스: https://[도메인]/services/
- 블로그: https://[도메인]/blog/
- 연락처: https://[도메인]/contact/

## 핵심 콘텐츠

- [페이지 제목]: https://[도메인]/[경로]/
- [페이지 제목]: https://[도메인]/[경로]/

## Sitemap

- https://[도메인]/sitemap.xml

## Optional

- https://[도메인]/admin/
- https://[도메인]/wp-admin/
- https://[도메인]/cart/
- https://[도메인]/checkout/
- https://[도메인]/login/
```

---

## llms-full.txt 자동 생성 스크립트

중요 페이지의 마크다운 내용을 수집해 llms-full.txt를 생성하는 Python 스크립트.

```python
#!/usr/bin/env python3
"""
llms-full.txt 생성 스크립트
사이트맵에서 URL을 수집하고 각 페이지 내용을 마크다운으로 변환해 저장한다.
"""
import requests
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip_tags = {'script', 'style', 'nav', 'footer', 'header'}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_data(self, data):
        if self.current_tag not in self.skip_tags:
            stripped = data.strip()
            if stripped:
                self.text.append(stripped)

    def get_text(self):
        return '\n'.join(self.text)

def fetch_sitemap_urls(sitemap_url, limit=50):
    r = requests.get(sitemap_url, timeout=15)
    root = ET.fromstring(r.content)
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [loc.text for loc in root.findall('.//sm:loc', ns)]
    return urls[:limit]

def generate_llms_full(sitemap_url, output_path='llms-full.txt'):
    urls = fetch_sitemap_urls(sitemap_url)
    lines = [f'# llms-full.txt — {urlparse(sitemap_url).netloc}\n']

    for url in urls:
        try:
            r = requests.get(url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
            extractor = TextExtractor()
            extractor.feed(r.text)
            text = extractor.get_text()
            lines.append(f'\n## {url}\n\n{text[:5000]}\n')
        except Exception as e:
            lines.append(f'\n## {url}\n\n[수집 실패: {e}]\n')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'생성 완료: {output_path} ({len(urls)}개 페이지)')

if __name__ == '__main__':
    generate_llms_full('https://[도메인]/sitemap.xml')
```

**실행:**
```bash
python3 generate_llms_full.py
# 생성된 llms-full.txt를 사이트 루트에 배포
```

---

## 검증 명령어

```bash
# llms.txt 접근 확인
curl -I https://[도메인]/llms.txt

# 파일 내용 확인
curl -s https://[도메인]/llms.txt

# llms-full.txt 존재 확인
curl -I https://[도메인]/llms-full.txt

# Content-Type 확인 (text/plain 권장)
curl -I https://[도메인]/llms.txt | grep -i content-type
```

---

## 구현 우선순위

| 우선순위 | 작업 | 난이도 | 예상 효과 | 담당 |
|---|---|---|---|---|
| 1 | llms.txt 신규 생성 | 낮음 | 높음 | BE/운영 |
| 2 | 사이트 설명 블록쿼트 추가 | 낮음 | 높음 | 콘텐츠 |
| 3 | Sitemap 링크 추가 | 낮음 | 보통 | BE |
| 4 | 섹션 분류 및 URL 목록 확충 | 낮음 | 보통 | 콘텐츠 |
| 5 | 업데이트 자동화 (CI/CD 연동) | 높음 | 보통 | BE |
| 6 | llms-full.txt 생성 | 높음 | 높음 | BE |
```

---

## Setup

This restored execution skill is bundled inside the local `geo` execution
bundle under `skills/`.

Use it after the representative `geo` router has confirmed a direct execution
request, or invoke this subskill explicitly in a compatible agent surface that
loads nested skill directories.

## Dependencies and Permissions

This skill uses the tool boundary declared in frontmatter `allowed-tools`.

Network reads and local report writes are expected when the workflow runs.
External APIs are not required beyond the HTTP or browser-access checks already
named in the skill body.

## Source and License Notes

This restored execution surface preserves the original GEO-SEO execution
workflow inside the current repository's local execution bundle.

Repository-level reuse terms are inherited from `../../LICENSE`.
