---
name: geo-schema
description: >
  페이지에 필요한 JSON-LD 구조화 데이터를 생성하고 검증한다.
  현재 스키마 현황을 파악하고 누락된 타입의 완성 코드를 제공한다.
  Organization, Article, FAQPage, HowTo, speakable 등 GEO 영향도 높은 타입을 우선한다.
  L3(개발자) 전용 스킬.
  트리거: "스키마", "JSON-LD", "구조화 데이터", "schema".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-schema — JSON-LD 구조화 데이터 생성

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정한다.
> `L1` 또는 `L2`로 판단되면 아래 안내 메시지를 출력하고 실행을 중단한다.
> `L3`로 판단되면 아래 단계를 순서대로 실행한다.
> 결과는 `GEO-스키마-[도메인].md`로 저장한다.

---

## L1 / L2 접근 안내 (L1·L2이면 이 메시지 출력 후 중단)

```
JSON-LD 스키마 생성은 HTML 소스 편집이 필요한 개발 작업입니다.

현재 레벨에서는 직접 실행이 어렵습니다.

선택 사항:
1. 이 작업을 다시 요청할 때 `L3 개발자 프로필로 진행해 주세요.`처럼 수신자 레벨을 직접 명시하세요.
2. 개발팀에 아래 내용을 전달하세요:

   "페이지에 JSON-LD 구조화 데이터를 추가해 주세요.
    우선 항목: Organization, Article, FAQPage, speakable
    참고: https://schema.org / https://search.google.com/test/rich-results"
```

---

## 스키마 타입 개요

GEO 영향도 기준으로 우선순위를 정한다.

| 타입 | GEO 영향도 | 적용 대상 | 용도 |
|---|---|---|---|
| Organization | 높음 | 전 페이지 | 브랜드 정체성, AI 출처 인식 |
| Article / BlogPosting | 높음 | 콘텐츠 페이지 | 저자·날짜·제목 메타데이터 |
| FAQPage | 높음 | FAQ 포함 페이지 | AI 직접 답변 추출 |
| speakable | 높음 | 핵심 콘텐츠 페이지 | 음성·AI 응답용 구간 지정 |
| HowTo | 보통 | 절차 안내 페이지 | 단계별 안내 구조화 |
| BreadcrumbList | 보통 | 모든 내부 페이지 | 탐색 경로, 사이트 구조 전달 |
| Person | 보통 | 저자 프로필 페이지 | 저자 신뢰성 강화 |
| WebPage / WebSite | 낮음 | 홈·주요 페이지 | 기본 페이지 식별 |
| LocalBusiness | 조건부 | 지역 비즈니스 | 오프라인 사업체 위치·연락처 |
| Product | 조건부 | 제품·서비스 페이지 | 가격·평점·가용성 |

---

## 실행 단계

### 1단계: 현재 스키마 현황 파악

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests, re, json
from urllib.parse import urlparse

url = '[TARGET_URL]'
r = requests.get(url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
html = r.text

# JSON-LD 블록 추출
blocks = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.DOTALL)
print(f'JSON-LD 블록 수: {len(blocks)}개')

for i, block in enumerate(blocks, 1):
    try:
        data = json.loads(block.strip())
        t = data.get('@type', 'Unknown')
        print(f'  [{i}] @type: {t}')
        if isinstance(data.get('mainEntity'), list):
            print(f'       mainEntity 항목 수: {len(data[\"mainEntity\"])}개')
    except:
        print(f'  [{i}] 파싱 오류')

# 스키마 타입 전체 목록
all_types = re.findall(r'\"@type\"\s*:\s*\"([^\"]+)\"', html)
print(f'발견된 @type 전체: {list(set(all_types))}')
"
```

**Claude 웹 환경 (WebFetch 대체)**

> WebFetch로 대상 URL을 로드한다.
> HTML에서 `<script type="application/ld+json">` 블록을 찾아 `@type` 값을 모두 기록한다.
> 블록이 없으면 "스키마 없음"으로 판단한다.

---

### 2단계: 타입별 필요 여부 판단

페이지 성격에 따라 필요한 스키마를 결정한다.

| 타입 | 필요 조건 |
|---|---|
| Organization | 모든 페이지 (사이트 전체 적용) |
| Article | 블로그·뉴스·가이드 등 콘텐츠 페이지 |
| FAQPage | 질문-답변 형식 블록이 2개 이상인 페이지 |
| speakable | AI 음성 응답·인용에 쓰일 핵심 요약 구간이 있는 페이지 |
| HowTo | 번호 목록으로 절차를 안내하는 페이지 |
| BreadcrumbList | 홈 제외 모든 내부 페이지 |
| Person | 저자 소개·팀 소개 페이지 |
| LocalBusiness | 매장·사무소 주소·전화가 있는 페이지 |
| Product | 가격·구매 기능이 있는 페이지 |

---

### 3단계: 누락 스키마 코드 생성

필요하지만 없는 타입의 JSON-LD를 생성한다.
각 타입의 완성 코드는 아래 레퍼런스에서 제공한다.

---

## 스키마 타입별 완성 코드

---

### Organization

브랜드 정체성을 AI에게 전달한다. `sameAs`에 공식 채널을 모두 연결한다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[조직명]",
  "url": "https://[도메인]/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://[도메인]/logo.png",
    "width": 200,
    "height": 60
  },
  "description": "[조직 한 줄 설명]",
  "foundingDate": "[설립연도]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[전화번호]",
    "contactType": "customer service",
    "availableLanguage": "Korean"
  },
  "sameAs": [
    "https://www.instagram.com/[계정]",
    "https://www.youtube.com/@[채널]",
    "https://blog.naver.com/[블로그]",
    "https://ko.wikipedia.org/wiki/[항목]"
  ]
}
</script>
```

---

### Article / BlogPosting

콘텐츠 페이지의 저자·날짜·제목을 구조화한다.
뉴스·매거진은 `Article`, 블로그 포스트는 `BlogPosting`을 사용한다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[글 제목 — 110자 이하]",
  "description": "[글 요약 — 160자 이하]",
  "image": {
    "@type": "ImageObject",
    "url": "https://[도메인]/[이미지경로].jpg",
    "width": 1200,
    "height": 630
  },
  "url": "https://[도메인]/[글경로]/",
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "author": {
    "@type": "Person",
    "name": "[저자명]",
    "url": "https://[도메인]/author/[저자슬러그]/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[조직명]",
    "logo": {
      "@type": "ImageObject",
      "url": "https://[도메인]/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://[도메인]/[글경로]/"
  }
}
</script>
```

---

### FAQPage

FAQ 형식 콘텐츠를 AI가 개별 답변으로 인식하도록 구조화한다.
페이지에 표시된 질문·답변 텍스트와 정확히 일치시킨다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[질문 텍스트]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[답변 텍스트 — HTML 태그 없이 순수 텍스트]"
      }
    },
    {
      "@type": "Question",
      "name": "[질문 텍스트]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[답변 텍스트]"
      }
    }
  ]
}
</script>
```

---

### speakable

Google Assistant·Gemini 등 AI 음성 응답에서 이 페이지 콘텐츠를 활용하도록
핵심 요약 구간을 CSS 선택자로 지정한다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[페이지 제목]",
  "url": "https://[도메인]/[경로]/",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [
      "h1",
      ".article-summary",
      ".key-points",
      "#toc-summary"
    ]
  }
}
</script>
```

**cssSelector 선택 기준:**
- H1: 페이지 핵심 주제
- 첫 단락 또는 요약 블록 class
- 핵심 포인트 블록 class/id
- 실제 HTML 구조에 맞는 선택자만 사용

---

### HowTo

단계별 절차 페이지를 구조화한다. 각 step은 페이지의 실제 번호 항목과 일치시킨다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "[절차 제목]",
  "description": "[절차 요약]",
  "totalTime": "PT[숫자]M",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "[단계 1 제목]",
      "text": "[단계 1 상세 설명]",
      "image": "https://[도메인]/[단계1이미지].jpg"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "[단계 2 제목]",
      "text": "[단계 2 상세 설명]"
    }
  ]
}
</script>
```

---

### BreadcrumbList

탐색 경로를 구조화하여 사이트 계층을 AI에게 전달한다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "홈",
      "item": "https://[도메인]/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[카테고리명]",
      "item": "https://[도메인]/[카테고리]/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[현재 페이지 제목]",
      "item": "https://[도메인]/[카테고리]/[슬러그]/"
    }
  ]
}
</script>
```

---

### Person

저자·전문가 신뢰성을 구조화한다. E-E-A-T 강화에 직접적인 영향을 미친다.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "[이름]",
  "url": "https://[도메인]/author/[슬러그]/",
  "image": "https://[도메인]/[프로필이미지].jpg",
  "jobTitle": "[직함]",
  "worksFor": {
    "@type": "Organization",
    "name": "[조직명]"
  },
  "description": "[전문성 한 줄 소개]",
  "sameAs": [
    "https://www.linkedin.com/in/[계정]",
    "https://twitter.com/[계정]"
  ]
}
</script>
```

---

### LocalBusiness

오프라인 사업체 정보를 구조화한다. 업종에 따라 `Restaurant`, `MedicalBusiness` 등 서브타입 사용 가능.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[상호명]",
  "url": "https://[도메인]/",
  "telephone": "[전화번호]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[도로명 주소]",
    "addressLocality": "[시·구]",
    "addressRegion": "[도·특별시]",
    "postalCode": "[우편번호]",
    "addressCountry": "KR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": [위도],
    "longitude": [경도]
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "sameAs": [
    "https://map.naver.com/v5/entry/place/[플레이스ID]",
    "https://place.map.kakao.com/[장소ID]"
  ]
}
</script>
```

---

## 4단계: 검증 및 삽입 안내

### 검증 도구

```bash
# Google Rich Results Test (CLI 접근 불가 — 브라우저에서 직접 실행)
# https://search.google.com/test/rich-results

# Schema.org 검증기
# https://validator.schema.org/

# JSON 문법 검증 (Bash)
python3 -c "
import json, sys
with open('schema.json') as f:
    try:
        json.load(f)
        print('JSON 문법 유효')
    except json.JSONDecodeError as e:
        print(f'오류: {e}')
        sys.exit(1)
"
```

### HTML 삽입 위치

```html
<!-- </head> 바로 앞에 삽입 — 여러 스키마는 별도 <script> 블록으로 분리 -->
<head>
  ...
  <script type="application/ld+json">{ Organization 스키마 }</script>
  <script type="application/ld+json">{ Article 스키마 }</script>
  <script type="application/ld+json">{ FAQPage 스키마 }</script>
</head>
```

### WordPress 삽입 방법

**Yoast SEO 사용 중:**
- SEO → 검색 모습 → 구조화 데이터: Organization 자동 생성
- 커스텀 스키마는 테마 `functions.php` 또는 Custom HTML 블록에 추가

**플러그인 없이 직접 삽입:**
```php
// functions.php
add_action('wp_head', function() {
    if (is_single()) {
        echo '<script type="application/ld+json">';
        echo json_encode([
            '@context' => 'https://schema.org',
            '@type' => 'BlogPosting',
            'headline' => get_the_title(),
            'datePublished' => get_the_date('c'),
            'dateModified' => get_the_modified_date('c'),
            'author' => ['@type' => 'Person', 'name' => get_the_author()],
        ], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
        echo '</script>';
    }
});
```

---

## L3 출력 템플릿

```markdown
# [도메인] JSON-LD 스키마 분석

Date: [날짜]  |  URL: [URL]

---

## 현재 스키마 현황

JSON-LD 블록: [N]개

| @type | 상태 | 주요 필드 | 누락 필드 |
|---|---|---|---|
| Organization | ✅ 있음 / ❌ 없음 | [있는 필드] | [누락 필드] |
| Article | ✅ 있음 / ❌ 없음 | [있는 필드] | [누락 필드] |
| FAQPage | ✅ 있음 / ❌ 없음 | — | — |
| speakable | ✅ 있음 / ❌ 없음 | — | — |
| HowTo | 해당 없음 / ✅ / ❌ | — | — |
| BreadcrumbList | ✅ 있음 / ❌ 없음 | — | — |
| Person | 해당 없음 / ✅ / ❌ | — | — |

---

## 생성된 스키마 코드

### [타입명]

```json
{ 완성 코드 }
```

### [타입명]

```json
{ 완성 코드 }
```

---

## 삽입 체크리스트

- [ ] JSON 문법 검증 완료 (python3 또는 validator.schema.org)
- [ ] `</head>` 바로 앞에 `<script type="application/ld+json">` 태그로 삽입
- [ ] Google Rich Results Test 통과 확인
- [ ] 스테이징 배포 후 검증, 이상 없으면 프로덕션 반영

---

## 구현 우선순위

| 우선순위 | 타입 | GEO 영향도 | 난이도 | 비고 |
|---|---|---|---|---|
| 1 | Organization | 높음 | 낮음 | 전 페이지 공통 적용 |
| 2 | FAQPage | 높음 | 낮음 | FAQ 콘텐츠 존재 시 |
| 3 | speakable | 높음 | 낮음 | cssSelector 확인 필요 |
| 4 | Article | 높음 | 낮음 | 콘텐츠 페이지 전체 |
| 5 | BreadcrumbList | 보통 | 낮음 | 내부 페이지 전체 |
| 6 | Person | 보통 | 낮음 | 저자 페이지 존재 시 |
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
