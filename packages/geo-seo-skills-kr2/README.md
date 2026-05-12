# geo-seo-skills-kr — GEO·SEO 분석 스킬 라이브러리

GEO(Generative Engine Optimization)와 SEO를 통합 분석하는 22개 스킬 라이브러리.  
마케팅 담당자(L1) · 웹마스터(L2) · 개발자(L3) 세 레벨에 맞춰 동일한 분석 깊이를 다른 언어로 전달한다.  
한국어·영어·일본어·중국어·스페인어 5개 언어 사이트 분석과 OUTPUT_LANG 다국어 보고서 출력을 지원한다.

**코어 계층(18개):** Claude 웹 / Claude Code 모두 동작 — WebFetch 기반 원격 분석.  
**확장 계층(4개):** Claude Code 전용 — Playwright 실측·로컬 파일 시스템·자동 파이프라인.

---

## 시작하기

### Claude 웹 / Claude Code 공통

처음 실행하면 레벨 선택 메뉴가 표시된다. 레벨은 이후 언제든 변경할 수 있다.

```
/geo level
```

레벨 선택 후 첫 번째 명령:

```bash
/geo audit https://example.com
```

### Claude Code — 확장 계층 시작

Playwright 실측·파이프라인 자동화가 필요할 때 확장 계층 오케스트레이터를 사용한다.

```bash
/geo-code init                              # 환경 점검 (Node.js·Playwright·CDP)
/geo-code pipeline https://example.com     # 전체 파이프라인 자동 실행
```

---

## 레벨 시스템

| 레벨 | 대상 | 출력 방식 |
|---|---|---|
| **L1** | 마케팅 담당자 | 비즈니스 언어, 담당자 요청 메모 중심 |
| **L2** | 웹마스터 / 운영자 | FTP·CMS 파일 수정 단계별 안내 |
| **L3** | 개발자 | 코드 스니펫, 기술 명세, CLI 명령어 포함 |

분석 깊이는 세 레벨 모두 동일하다. 달라지는 것은 결과 표현 방식이다.

---

## 레벨 매트릭스

### 코어 계층 — Claude 웹 / Code 모두

| 명령어 | L1 마케팅 | L2 웹마스터 | L3 개발자 |
|---|:---:|:---:|:---:|
| `/geo audit` | ✓ | ✓ | ✓ |
| `/geo brand` | ✓ | ✓ | ✓ |
| `/geo content` | ✓ | ✓ | ✓ |
| `/geo citability` | ✓ | ✓ | ✓ |
| `/geo crawlers` | ✓ | ✓ | ✓ |
| `/geo brands` | ✓ | ✓ | ✓ |
| `/geo platforms` | ✓ | ✓ | ✓ |
| `/geo lang-platform` | ✓ | ✓ | ✓ |
| `/geo report` | ✓ | ✓ | ✓ |
| `/geo technical` | — | ✓ | ✓ |
| `/geo multilang` | — | ✓ | ✓ |
| `/geo llmstxt` | — | ✓ | ✓ |
| `/geo compare` | — | ✓ | ✓ |
| `/geo schema` | — | — | ✓ |
| `/geo proposal` | — | — | ✓ |
| `/geo prospect` | — | — | ✓ |
| `/geo report-pdf` | — | — | ✓ |

L1이 L2·L3 전용 명령어를 실행하면 담당자 전달 메모 생성 또는 레벨 변경 안내가 출력된다.

### 확장 계층 — Claude Code 전용 (L3)

| 명령어 | 필요 도구 | 기능 |
|---|---|---|
| `/geo realtime` | Playwright + Node.js | 브라우저 실측 AI 인용 확인 |
| `/geo tracker` | 로컬 파일 시스템 | Gap 시계열 추적 |
| `/geo batch` | Bash + WebFetch | 복수 도메인 간이 GEO 스캔 비교 |
| `/geo-code` | Bash + Playwright | 확장 계층 오케스트레이터 (init·pipeline·status) |

Claude 웹에서 확장 계층 명령어를 호출하면 안내 메시지를 출력하고 중단한다.

---

## 명령어 일람

### 공통 스킬 — L1·L2·L3

| 명령어 | 기능 |
|---|---|
| `/geo audit <url>` | 전체 GEO 감사, 종합 점수 산출, 심각도 4단계 분류 |
| `/geo brand <url>` | AI 브랜드 인식 Gap 분석 |
| `/geo brand <url> --track` | Gap 변화 추적 (4주 순환 측정) |
| `/geo content <url>` | E-E-A-T 콘텐츠 품질 + 번역 품질 평가 |
| `/geo citability <url>` | AI 검색 인용 가능성 점수 |
| `/geo crawlers <url>` | AI 크롤러 접근 현황 진단 (봇 20개·전략 A~G) |
| `/geo brands <url>` | 외부 채널 브랜드 언급 분석 |
| `/geo platforms <url>` | AI 플랫폼별 최적화 분석 (글로벌+지역 플랫폼) |
| `/geo lang-platform <url>` | 언어별 AI 플랫폼 매핑·봇 전략 |
| `/geo report` | 전체 분석 결과 종합 보고서 생성 (30일 로드맵 포함) |
| `/geo lang` | 출력 언어 선택 (ko/en/ja/zh/es) |

### L2+L3 스킬 — 웹마스터·개발자

| 명령어 | 기능 |
|---|---|
| `/geo technical <url>` | 기술 SEO 진단 + 렌더링 방식 사전 판정 + hreflang 분석 |
| `/geo multilang <url>` | 다국어 GEO 통합 진단 (hreflang·콘텐츠·AI 가시성) |
| `/geo llmstxt <url>` | llms.txt 존재·품질 진단 및 생성 |
| `/geo compare <url1> <url2>` | 경쟁사 GEO 신호 비교 분석 |

### L3 전용 스킬 — 개발자

| 명령어 | 기능 |
|---|---|
| `/geo schema <url>` | JSON-LD 스키마 감지·생성 (다국어 스키마 포함) |
| `/geo proposal` | GEO 개선 제안서 자동 작성 |
| `/geo prospect <url>...` | 잠재 고객 GEO 빠른 스캔 (배치 지원) |
| `/geo report-pdf` | 전체 분석 결과 PDF 단일 보고서 |

### 확장 계층 — Claude Code 전용 (L3)

| 명령어 | 기능 |
|---|---|
| `/geo realtime <url>` | Playwright로 7개 AI 플랫폼에서 실측 인용 확인 |
| `/geo realtime <url> --cp` | CP 콘텐츠(topics.csv + H2/H3)에서 질문 추출 후 실측 |
| `/geo realtime <url> --cp --track` | 실측 후 geo-brand BASELINE에 스냅샷 기록 |
| `/geo tracker <도메인>` | BASELINE 파일 시계열 분석, 5개 Gap 지표 추이 |
| `/geo tracker <도메인> --export` | 시계열 데이터를 CSV로 추가 저장 |
| `/geo batch <url1> <url2> ...` | 복수 도메인 간이 스캔 비교 표 생성 |
| `/geo batch --file <path>` | URL 목록 파일에서 읽어 배치 스캔 |
| `/geo-code init` | 환경 초기화 점검 (Node.js·Playwright·browser-citation.js·Chrome CDP) |
| `/geo-code pipeline <url>` | 단일 도메인 자동 파이프라인 (audit → realtime → tracker) |
| `/geo-code pipeline <url1> <url2>` | 복수 도메인 파이프라인 (batch → 선별 → audit → realtime → tracker) |
| `/geo-code status [도메인]` | 현재 폴더·BASELINE·CP 프로젝트 연동 상태 확인 |

---

## 스킬별 상세

### `/geo audit` — 전체 GEO 감사

> 트리거: "GEO 감사", "전체 분석", "site audit", "사이트 점검", "/geo audit"  
> 사용 가능: L1·L2·L3

```bash
/geo audit https://example.com
```

5개 영역(AI 가시성·플랫폼·기술 SEO·콘텐츠·스키마)을 순차 분석하고 종합 GEO 점수를 산출한다.  
발견된 문제를 CRITICAL / HIGH / MEDIUM / LOW 4단계로 분류하여 처리 기한과 함께 제시한다.

출력: `GEO-감사-보고서.md`

---

### `/geo brand` — AI 브랜드 인식 Gap 분석

> 트리거: "브랜드 인식", "포지셔닝 검증", "AI 담변 분석", "/geo brand"  
> 사용 가능: L1·L2·L3

```bash
# 최초 측정 (Gap 분석 + CP 인풋 생성)
/geo brand https://example.com
/geo brand https://example.com --brand "브랜드명"
/geo brand https://example.com --comp competitive-positioning.md
/geo brand https://example.com --segments "신규사용자,기존사용자,경쟁사검토"

# 4주 후 재측정 (변화 추적)
/geo brand https://example.com --track
```

**핵심 기능:**
1. **Gap 분석** — COMP 포지셔닝(원하는 인식) vs 실제 AI 담변(현재 인식) 수치화
2. **콘텐츠 연결** — Gap을 메울 콘텐츠 주제 자동 생성 → `/cp prep` 투입
3. **순환 추적** — 4주마다 재측정해 ΔGap 변화 측정

**5가지 실측 지표 (0~100):**

| 지표 | 의미 |
|------|------|
| 포지셔닝 반영률 | 원하는 키워드가 AI 담변에 등장하는 비율 |
| SOV | 브랜드 등장 담변 수 / 전체 담변 수 (노출 점유율) |
| BCI | 단독 등장 / 전체 등장 (단독 브랜드 인식 강도) |
| 채널 인용률 | 자사 URL 인용 / 전체 인용 URL |
| 맥락 일치율 | 원하는 속성 매칭 비중 |

**5단계 Gap 등급:**

| 등급 | 반영률 | 의미 |
|------|--------|------|
| INVISIBLE | 0~20 | AI가 우리 포지셔닝을 전혀 반영하지 않음 |
| DISTANT | 21~40 | 우리 인식과 AI 인식 큰 차이 |
| PARTIAL | 41~60 | 일부 반영, 핵심 메시지 누락 |
| ALIGNED | 61~80 | 포지셔닝 대부분 반영됨 |
| ANCHORED | 81+ | AI가 우리 포지셔닝을 정확히 전달 |

출력: `GEO-BRAND-GAP-[브랜드]-[날짜].md` · `GEO-BRAND-CP-인풋-[날짜].md` · `GEO-BRAND-BASELINE-[날짜].json`

---

### `/geo content` — 콘텐츠 품질 평가

> 트리거: "E-E-A-T", "콘텐츠 품질", "콘텐츠 신뢰도", "content", "/geo content"  
> 사용 가능: L1·L2·L3

```bash
/geo content https://example.com/blog/article
```

출력: `GEO-콘텐츠-분석.md`

---

### `/geo citability` — AI 인용 가능성 점수

> 트리거: "인용 가능성", "AI 인용", "FAQPage", "speakable", "/geo citability"  
> 사용 가능: L1·L2·L3

```bash
/geo citability https://example.com
```

출력: `GEO-인용가능성-분석.md`

---

### `/geo crawlers` — AI 크롤러 접근 진단

> 트리거: "AI 크롤러", "robots.txt", "봇 차단", "크롤링", "/geo crawlers"  
> 사용 가능: L1·L2·L3

```bash
/geo crawlers https://example.com
```

출력: `GEO-크롤러-분석.md`

---

### `/geo brands` — 브랜드 언급 분석

> 트리거: "브랜드 언급", "brand mentions", "외부 언급", "Wikipedia", "/geo brands"  
> 사용 가능: L1·L2·L3

```bash
/geo brands https://example.com
```

출력: `GEO-브랜드언급-분석.md`

---

### `/geo platforms` — AI 플랫폼 최적화

> 트리거: "플랫폼", "ChatGPT", "Perplexity", "Google AI Overviews", "/geo platforms"  
> 사용 가능: L1·L2·L3

```bash
/geo platforms https://example.com
```

출력: `GEO-플랫폼-분석.md`

---

### `/geo lang-platform` — 언어별 AI 플랫폼 매핑

> 트리거: "언어별 플랫폼", "네이버 AI 브리핑", "Baidu", "Yahoo Japan", "/geo lang-platform"  
> 사용 가능: L1·L2·L3

```bash
/geo lang-platform https://example.com
```

SITE_LANGS를 감지하여 언어별로 최적화해야 할 AI 플랫폼과 봇 전략을 제시한다.  
출력: `GEO-언어플랫폼-[도메인]-[날짜].md`

---

### `/geo report` — 종합 보고서

> 트리거: "보고서", "종합", "report", "/geo report"  
> 사용 가능: L1·L2·L3

```bash
/geo report
```

CRITICAL/HIGH/MEDIUM/LOW 심각도 기준으로 개선 과제를 정렬하고 30일 로드맵을 생성한다.  
출력: `GEO-종합보고서.md`

---

### `/geo technical` — 기술 SEO 진단

> 트리거: "기술 SEO", "페이지 속도", "Core Web Vitals", "렌더링", "technical", "/geo technical"  
> 사용 가능: L2·L3

```bash
/geo technical https://example.com
```

0단계에서 렌더링 방식을 사전 판정(SSR / 하이브리드 / CSR+SSR신호 / 순수 CSR)한다.  
순수 CSR 감지 시 CRITICAL 경고 배너를 출력한다.  
출력: `GEO-기술SEO-분석.md`

---

### `/geo multilang` — 다국어 GEO 통합 진단

> 트리거: "다국어", "hreflang", "multilang", "언어별 GEO", "/geo multilang"  
> 사용 가능: L2·L3

```bash
/geo multilang https://example.com
```

hreflang 구현 현황, 언어별 콘텐츠 품질, AI 가시성을 통합 진단한다.  
출력: `GEO-다국어-[도메인]-[날짜].md`

---

### `/geo llmstxt` — llms.txt 진단 및 생성

> 트리거: "llms.txt", "AI 크롤러 안내 파일", "llmstxt", "/geo llmstxt"  
> 사용 가능: L2·L3

```bash
/geo llmstxt https://example.com
```

출력: `GEO-llmstxt-분석.md`

---

### `/geo compare` — 경쟁사 비교 분석

> 트리거: "경쟁사 비교", "compare", "GEO 비교", "/geo compare"  
> 사용 가능: L2·L3

```bash
/geo compare https://my-site.com https://competitor.com
```

출력: `GEO-비교분석-[자사도메인]-vs-[경쟁사도메인].md`

---

### `/geo schema` — JSON-LD 스키마 생성

> 트리거: "JSON-LD", "스키마", "schema", "구조화 데이터", "/geo schema"  
> 사용 가능: L3

```bash
/geo schema https://example.com
```

출력: `GEO-스키마-[도메인].md`

---

### `/geo proposal` — GEO 개선 제안서

> 트리거: "제안서", "proposal", "개선 계획서", "/geo proposal"  
> 사용 가능: L3

```bash
/geo proposal
```

출력: `GEO-제안서-[도메인]-[날짜].md`

---

### `/geo prospect` — 잠재 고객 빠른 스캔

> 트리거: "잠재 고객", "영업 스캔", "prospect", "/geo prospect"  
> 사용 가능: L3

```bash
/geo prospect https://lead-site.com
/geo prospect https://a.com https://b.com https://c.com
```

출력: `GEO-잠재고객-[도메인]-[날짜].md` / `GEO-잠재고객-배치-[날짜].md`

---

### `/geo report-pdf` — PDF 보고서 생성

> 트리거: "PDF", "보고서 PDF", "report-pdf", "/geo report-pdf"  
> 사용 가능: L3

```bash
/geo report-pdf
```

출력: `GEO-보고서-[도메인]-[날짜].md` + PDF

---

### `/geo realtime` — AI 인용 실측 (Code 전용)

> 트리거: "실측", "browser-citation", "인용 확인", "/geo realtime"  
> 사용 가능: L3 / Claude Code 전용

```bash
/geo realtime https://example.com
/geo realtime https://example.com --cp              # CP 콘텐츠 기반 질문 추출
/geo realtime https://example.com --cp --track      # 실측 + BASELINE 스냅샷 기록
/geo realtime https://example.com --platforms perplexity,chatgpt,gemini
```

Playwright CDP로 7개 AI 플랫폼(Perplexity·Google AIO·Bing·ChatGPT·Gemini·Claude·Grok)에서  
실제 브라우저를 열어 도메인·브랜드 인용 여부를 확인한다.  
`--cp` 옵션으로 CP `topics.csv`와 완성 콘텐츠 H2/H3에서 질문을 추출한 후 실측한다.

인용 강도 등급: STRONG(60% 이상) / MODERATE(40~59%) / WEAK(20~39%) / MINIMAL(0~19%)

출력: `GEO-REALTIME-[도메인]-[날짜].md`

---

### `/geo tracker` — Gap 시계열 추적 (Code 전용)

> 트리거: "추적", "시계열", "gap 변화", "tracker", "/geo tracker"  
> 사용 가능: L3 / Claude Code 전용

```bash
/geo tracker example.com
/geo tracker example.com --weeks 8       # 최근 8주 데이터만 표시
/geo tracker example.com --export        # CSV 추가 저장
```

현재 폴더의 `GEO-BRAND-BASELINE-*.json` 파일을 날짜순으로 읽어  
포지셔닝 반영률·SOV·BCI·채널 인용률·맥락 일치율 5개 지표와  
geo-realtime 실측 인용률의 변화 추이를 분석한다.

출력: `GEO-TRACKER-[도메인]-[날짜].md`

---

### `/geo batch` — 복수 도메인 배치 스캔 (Code 전용)

> 트리거: "배치", "일괄 스캔", "여러 도메인", "batch", "/geo batch"  
> 사용 가능: L3 / Claude Code 전용

```bash
/geo batch https://a.com https://b.com https://c.com
/geo batch --file urls.txt
/geo batch https://a.com https://b.com --full      # geo-audit 수준 전체 스캔
```

도메인당 8개 항목(HTTPS·AI봇·llms.txt·sitemap·스키마·렌더링·meta·OG)을 스캔하고  
점수 낮은 순으로 비교 표를 생성한다. 최대 20개 도메인.

출력: `GEO-BATCH-[날짜].md`

---

### `/geo-code` — 확장 계층 오케스트레이터 (Code 전용)

> 트리거: "/geo-code", "geo-code init", "geo-code pipeline", "확장 파이프라인"  
> 사용 가능: L3 / Claude Code 전용

```bash
# 환경 초기화 점검
/geo-code init

# 단일 도메인 파이프라인 (audit → brand → realtime → tracker)
/geo-code pipeline https://example.com
/geo-code pipeline https://example.com --cp

# 복수 도메인 파이프라인 (batch → 선별 → audit → realtime → tracker)
/geo-code pipeline https://a.com https://b.com https://c.com
/geo-code pipeline https://a.com https://b.com --top 2

# 상태 확인
/geo-code status
/geo-code status example.com
```

**`/geo-code init`:** Node.js·Playwright·Chromium·browser-citation.js·Chrome CDP 5항목 순차 확인.

**`/geo-code pipeline`:** 확장 계층 스킬을 자동 순서대로 실행한다.
- BASELINE 없으면 `/geo brand`를 자동 호출해 생성 후 계속 진행
- 각 Step 완료 후 한 줄 요약 출력, CRITICAL 발견 시 계속 진행 여부 질의
- 종합 요약에 생성 파일 목록·인용률·Gap 등급·다음 측정 예정일 포함

**`/geo-code status`:** 분석 파일 현황, BASELINE 마지막 측정일·다음 예정일, CP topics.csv 연동 상태.

---

## 워크플로 예시

### L1 — 마케팅 담당자

```bash
/geo level                       # 레벨 설정 (처음 한 번)
/geo audit https://example.com   # 전체 감사
/geo report                      # 경영진 요약 보고서 생성
```

### L2 — 웹마스터

```bash
/geo audit https://example.com       # 전체 감사
/geo technical https://example.com   # 기술 SEO 상세 점검
/geo llmstxt https://example.com     # llms.txt 진단·생성
/geo compare https://example.com https://competitor.com
/geo report                          # 체크리스트 보고서
```

### L3 — 개발자 (코어 계층)

```bash
/geo prospect https://lead.com       # 영업 대상 빠른 스캔
/geo audit https://example.com       # 전체 감사
/geo schema https://example.com      # JSON-LD 스키마 생성
/geo technical https://example.com   # 기술 SEO 감사
/geo llmstxt https://example.com     # llms.txt 최적화
/geo proposal                        # 개선 제안서 생성
/geo report-pdf                      # PDF 단일 보고서 생성
```

### L3 — 개발자 (확장 계층, Claude Code)

```bash
# 최초 환경 설정
/geo-code init

# 단일 도메인 전체 사이클
/geo-code pipeline https://example.com --cp

# 복수 도메인 비교 후 하위 3개 집중 분석
/geo-code pipeline https://a.com https://b.com https://c.com https://d.com --top 3

# 4주 후 변화 추적
/geo-code pipeline https://example.com --cp    # realtime --track 자동 실행
/geo tracker example.com                       # 시계열 보고서 갱신
```

### 다국어 사이트

```bash
/geo lang ko                         # 출력 언어 한국어 설정
/geo audit https://example.com       # 사이트 분석 (SITE_LANGS 자동 감지)
/geo multilang https://example.com   # 다국어 GEO 통합 진단
/geo lang-platform https://example.com  # 언어별 AI 플랫폼 최적화
```

---

## 환경 호환

| 항목 | Claude 웹 (코어) | Claude Code (코어) | Claude Code (확장) |
|---|---|---|---|
| 데이터 수집 | WebFetch | WebFetch + Bash | Playwright 실측 |
| AI 인용 확인 | 간접 추정 (구조 분석) | 간접 추정 | 실제 브라우저 실측 |
| 파일 저장 | 대화 내 출력 | 로컬 .md 자동 저장 | 로컬 .md/.json 자동 저장 |
| 복수 도메인 | 수동 순차 실행 | /geo batch | /geo-code pipeline 자동화 |
| 시계열 추적 | 불가 | 불가 | /geo tracker (BASELINE 파일 기반) |
| 파이프라인 자동화 | 불가 | 불가 | /geo-code pipeline |

---

## 참고

| 파일 | 내용 |
|---|---|
| `CLAUDE.md` | 프로젝트 개요·핵심 설계 원칙·주요 결정 사항·진행 이력 |
| `geo/SKILL.md` | 코어 오케스트레이터 — 레벨 선택·명령어 라우팅 내부 로직 |
| `skills/geo-code/SKILL.md` | 확장 계층 오케스트레이터 — init·pipeline·status 내부 로직 |
| `references/lang-platform-map.md` | 봇 20개·전략 A~G·언어별 AI 플랫폼 매핑 |
| `references/hreflang-checklist.md` | hreflang 필수 5개·경고 5개·점수 기준 |
