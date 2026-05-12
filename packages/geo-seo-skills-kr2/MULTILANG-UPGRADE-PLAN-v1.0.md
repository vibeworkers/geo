# KR GEO → 다국어 GEO 스킬 업그레이드 수행계획

작성일: 2026-05-09  |  최종 수정: 2026-05-09 (클로바X 종료 → 네이버 AI 브리핑·AI 탭 반영)

---

## 1. 업그레이드 목표 및 범위

### 목표

| 목표 | 내용 |
|---|---|
| 다국어 사이트 분석 | 한·영·일·중·스페인어 등 다국어 버전을 운영하는 사이트의 GEO 신호를 언어별로 진단 |
| 스킬 자체 다국어 출력 | 분석 결과를 사용자 선택 언어(ko·en·ja·zh·es)로 출력 |
| 언어별 AI 플랫폼 커버리지 | 국가/언어 시장별 주요 AI 플랫폼을 분리하여 분석 |

### 확정 범위

```
지원 언어: 한국어(ko) · 영어(en) · 일본어(ja) · 중국어(zh) · 스페인어(es) · 기타(auto)
언어별 AI 플랫폼: 한국(네이버 AI 브리핑·네이버 AI 탭·ChatGPT·Gemini) /
                  일본(ChatGPT·Yahoo! Japan AI·Perplexity) /
                  중국(Baidu Ernie·Kimi·Qwen·DeepSeek) / 스페인어권(ChatGPT·Perplexity·Gemini)
※ 클로바X는 2026년 4월 9일 서비스 종료. 네이버 AI 브리핑(2025.03 출시)·AI 탭(2026.04 베타 출시)으로 대체.
출력 언어: OUTPUT_LANG 변수로 런타임 선택 (기본값: 사이트 감지 언어 기준)
```

---

## 2. 현황 분석 — KR GEO 한계점

| 한계 항목 | 내용 |
|---|---|
| 한국어 단일 출력 | 모든 스킬 출력이 한국어 고정. 영어·일본어 사이트 분석 결과도 한국어로만 출력됨 |
| hreflang 미검사 | 다국어 사이트의 핵심 기술 신호인 hreflang 태그 분석 없음 |
| 언어별 URL 구조 미진단 | 서브디렉토리(/en/)·서브도메인(en.example.com)·ccTLD(.co.uk) 방식 미구분 |
| 글로벌 봇 불완전 | 네이버봇·Baiduspider·AppleBot 등 비영어권 AI 봇 목록 없음 |
| 클로바X 종료 미반영 | 클로바X는 2026년 4월 9일 종료. 네이버 AI 브리핑·AI 탭 기반 최적화 기준이 없음 |
| 중국 AI 플랫폼 미지원 | Baidu Ernie·Kimi·Qwen·DeepSeek 등 중국 AI 플랫폼 분석 없음 |
| 다국어 스키마 없음 | `inLanguage`, `availableLanguage`, `translationOfWork` 등 다국어 스키마 미포함 |
| 번역 품질 평가 없음 | 기계 번역 감지 신호 평가 없음 |
| 다국어 llms.txt 없음 | 언어별 섹션으로 구성된 llms.txt 생성 로직 없음 |

---

## 3. 신규·변경 스킬 목록

### 3-1. 신규 스킬 (2개)

| 스킬명 | 파일 경로 | 역할 | 대상 레벨 |
|---|---|---|---|
| `geo-multilang` | `skills/geo-multilang/SKILL.md` | 다국어 사이트 전용 진단 (hreflang·언어별 URL·번역 품질·언어별 AI 가시성) | L2, L3 |
| `geo-lang-platform` | `skills/geo-lang-platform/SKILL.md` | 언어/국가별 AI 플랫폼 매핑 및 최적화 분석 | L1, L2, L3 |

### 3-2. 기존 스킬 변경 (7개)

| 스킬명 | 변경 내용 | 우선순위 |
|---|---|---|
| `geo/SKILL.md` (오케스트레이터) | 언어 감지 로직·OUTPUT_LANG 시스템·`/geo multilang` 명령어 추가 | P0 |
| `geo-crawlers` | 비영어권 AI 봇 추가(네이버봇·Baiduspider·AppleBot 등), 언어별 허용 전략 분기 | P1 |
| `geo-technical` | hreflang 분석 모듈 추가, 다국어 URL 구조 진단 추가 | P1 |
| `geo-platform-optimizer` | 언어별 AI 플랫폼 분기 로직 추가 | P1 |
| `geo-schema` | 다국어 스키마 타입 추가 (inLanguage·availableLanguage·translationOfWork) | P2 |
| `geo-content` | 다국어 E-E-A-T 평가 추가, 번역 품질 감지 신호 추가 | P2 |
| `geo-llmstxt` | 다국어 llms.txt 생성 로직 추가 | P3 |

---

## 4. Phase별 구현 계획

### Phase 0 — 사전 설계 (착수 전 완료)

**목표:** 전체 아키텍처 확정

| 작업 | 산출물 |
|---|---|
| 언어별 AI 플랫폼·봇 목록 확정 | `references/lang-platform-map.md` |
| OUTPUT_LANG 변수 설계 (값·기본값·선택 방식) | 설계 문서 (본 파일에 포함) |
| 각 스킬 변경 범위 상세 정의 | 본 파일 섹션 5 |
| 다국어 hreflang 검사 체크리스트 | `references/hreflang-checklist.md` |

---

### Phase 1 — 핵심 인프라 (최우선 구현)

**목표:** 다국어 분석의 기반이 되는 3개 스킬 완성

#### 1-1. 오케스트레이터 (`geo/SKILL.md`) 개편

추가 내용:

```
[언어 감지 시스템]
- 사이트 HTML lang 속성, hreflang 태그, Content-Language 헤더 순으로 언어 감지
- 감지 결과를 SITE_LANGS 변수에 저장 (예: ["ko", "en", "ja"])

[OUTPUT_LANG 변수]
- 사용자 첫 실행 시 출력 언어 선택 (기본값: ko)
- 지원: ko · en · ja · zh · es
- /geo lang 명령으로 언제든 변경 가능

[신규 명령어]
- /geo multilang <url>       다국어 사이트 전용 진단
- /geo lang                  출력 언어 변경
- /geo lang-platform <url>   언어별 AI 플랫폼 분석
```

예상 작업량: 342줄 → 약 420줄 (+80줄)

---

#### 1-2. `geo-crawlers` 확장

추가할 비영어권 봇:

| 봇 이름 | User-agent | 서비스 | 언어/지역 | 용도 |
|---|---|---|---|---|
| Yeti | `Yeti` | NAVER 검색·HyperCLOVA | 한국 | 검색+학습 |
| NaverBot | `NaverBot` | NAVER | 한국 | 검색 |
| Baiduspider | `Baiduspider` | Baidu Ernie | 중국 | 검색+학습 |
| Baiduspider-render | `Baiduspider-render` | Baidu 렌더링 봇 | 중국 | 검색 |
| SogouBot | `Sogou web spider` | Sogou AI | 중국 | 검색 |
| 360Spider | `360Spider` | 360 AI | 중국 | 검색 |
| AppleBot | `Applebot` | Apple Intelligence · Siri | 글로벌 | 학습+검색 |
| YahooSeeker | `YahooSeeker` | Yahoo! Japan AI | 일본 | 검색 |
| ia_archiver | `ia_archiver` | Internet Archive (AI 학습 소스) | 글로벌 | 학습 |

언어별 봇 허용 전략 추가:

```
전략 D: 한국 시장 최적화 — Yeti·NaverBot 추가 허용
전략 E: 일본 시장 최적화 — YahooSeeker·AppleBot 추가 허용
전략 F: 중국 시장 최적화 — Baiduspider·SogouBot·360Spider 추가 허용
전략 G: 글로벌 전체 허용 — 전략 A + D + E + F 통합
```

예상 작업량: 485줄 → 약 650줄 (+165줄)

---

#### 1-3. `geo-technical` hreflang 모듈 추가

새로 추가할 분석 모듈:

**hreflang 분석 (0~20점 추가)**

| 항목 | 확인 내용 |
|---|---|
| hreflang 태그 존재 | `<link rel="alternate" hreflang="...">` 또는 HTTP 헤더 또는 sitemap에 존재 여부 |
| x-default 설정 | 언어 미지정 사용자를 위한 x-default 지정 여부 |
| 언어-국가 코드 정확성 | ISO 639-1(언어) + ISO 3166-1(국가) 조합 정확성 (en-US · ko-KR · ja-JP 등) |
| 양방향 참조 | 각 언어 페이지가 서로를 참조하는지 교차 확인 |
| 누락된 언어 조합 | 사이트에 언어 버전이 있으나 hreflang 미등록인 페이지 탐지 |

**다국어 URL 구조 분석**

| 구조 방식 | 예시 | GEO 권장도 | 비고 |
|---|---|---|---|
| 서브디렉토리 | `/ko/`, `/en/`, `/ja/` | 높음 | 단일 도메인, 크롤러 효율 최고 |
| 서브도메인 | `ko.example.com` | 보통 | 별도 크롤 예산 소모 |
| ccTLD | `.co.kr`, `.co.jp` | 조건부 | 지역 신뢰도 높으나 관리 복잡 |
| 쿼리 파라미터 | `?lang=ko` | 낮음 | AI 크롤러 혼란 가능 |

예상 작업량: 374줄 → 약 480줄 (+106줄)

---

### Phase 2 — 분석 깊이 확장

#### 2-1. 신규 스킬: `geo-multilang`

**역할:** 다국어 사이트 전용 종합 진단 스킬

**5단계 실행 흐름:**

```
1단계: 언어 구성 파악
  - HTML lang 속성 확인
  - hreflang 태그 목록 추출
  - 언어별 URL 패턴 감지 (서브디렉토리·서브도메인·ccTLD)
  - 각 언어 버전 URL 수집

2단계: hreflang 정확성 검증
  - x-default 유무
  - 언어-국가 코드 정확성
  - 양방향 참조 확인
  - 고아 페이지(hreflang 미설정 언어 버전) 탐지

3단계: 언어별 콘텐츠 품질 비교
  - 언어별 콘텐츠 볼륨 (단어 수, H 태그 수)
  - 기계 번역 감지 신호:
      * 어색한 반복 표현
      * 브랜드명 오번역
      * 언어별 날짜 형식 불일치
      * 언어별 수치 단위 불일치 (예: 파운드 vs kg)
  - 언어별 저자·E-E-A-T 신호 차이

4단계: 언어별 AI 가시성 비교
  - 각 언어 버전 URL의 geo-citability 점수 비교
  - 언어별 FAQ 구조 유무
  - 언어별 스키마 inLanguage 설정 여부

5단계: 다국어 GEO 점수 산출
  hreflang 정확성   × 0.35
  콘텐츠 균형도     × 0.25  (언어별 콘텐츠 볼륨 차이)
  번역 품질         × 0.25
  AI 가시성 균형도  × 0.15
```

**점수 등급:**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | 다국어 GEO 최적화 완료 |
| 60–79 | 양호 | 일부 언어 버전 개선 필요 |
| 40–59 | 보통 | hreflang 오류 또는 콘텐츠 불균형 |
| 20–39 | 미흡 | 다국어 구조 재설계 필요 |
| 0–19 | 위험 | 다국어 사이트로 인식 불가 |

예상 작업량: 신규 약 420줄

---

#### 2-2. 신규 스킬: `geo-lang-platform`

**역할:** 언어/국가별 AI 플랫폼 매핑 및 최적화 진단

**언어별 AI 플랫폼 매핑표:**

| 언어/시장 | 주요 AI 플랫폼 | 주요 봇 | 핵심 최적화 포인트 |
|---|---|---|---|
| 한국어 (ko) | **네이버 AI 브리핑** · **네이버 AI 탭** · ChatGPT · Gemini | **Yeti · NaverBot** · GPTBot · Google-Extended | C-rank·D.I.A. 최적화, FAQ·표·목록 구조, 네이버 Search Advisor 등록 |
| 영어 (en) | ChatGPT · Perplexity · Gemini · Copilot · Grok | GPTBot · PerplexityBot · Google-Extended · Bingbot | E-E-A-T, Wikipedia 등재, Reddit 언급 |
| 일본어 (ja) | ChatGPT · Yahoo! Japan AI · Perplexity | GPTBot · YahooSeeker · PerplexityBot | Yahoo! Japan 최적화, 일본어 FAQ 구조 |
| 중국어 (zh) | Baidu Ernie · Kimi · Qwen · DeepSeek · 360 AI | Baiduspider · 360Spider · SogouBot | 바이두 검색 최적화, ICP 번호, 중국어 스키마 |
| 스페인어 (es) | ChatGPT · Perplexity · Gemini · Copilot | GPTBot · PerplexityBot · Google-Extended · Bingbot | 라틴아메리카 지역 hreflang 분리, es-ES vs es-MX |

> **한국 시장 플랫폼 변경 이력 (2026-05-09 반영)**
>
> | 항목 | 이전 | 변경 후 | 비고 |
> |---|---|---|---|
> | 클로바X | 주요 플랫폼 | **제거** | 2026-04-09 서비스 종료 |
> | 네이버 AI 브리핑 | 미포함 | **추가** | 2025-03-27 출시, 전체 검색 20%+ 적용 중 |
> | 네이버 AI 탭 | 미포함 | **추가** | 2026-04-28 베타 출시, 대화형 에이전틱 검색 |
> | 봇(크롤러) | 클로바X 전용 봇 없음 | **Yeti 유지** | AI 브리핑도 Yeti로 콘텐츠 수집. 전용 봇 없음 |

**한국 시장 특별 고려사항 (2026년 기준):**

```
[네이버 AI 브리핑 인용 최적화]
서비스: 네이버 통합검색 최상단 AI 요약 박스 (전체 검색의 20%+ 적용)
봇: Yeti (User-agent: Yeti/1.1) — 전용 AI 봇 없음, 기존 Yeti가 AI 브리핑 콘텐츠 수집 담당
인용 선택 기준: C-rank(창작자 랭크) + D.I.A.(딥 인텐트 분석)

콘텐츠 구조 요건:
  - 첫 번째 문단에 질문에 대한 직접 답변 배치
  - H3 질문 형식 FAQ 섹션 (실제 네이버 검색 쿼리와 일치)
  - 목록·표·단계별 가이드 형식 우선 인용
  - 작성일·수정일 명시 (신선도 반영)

네이버 생태계 최적화:
  - Naver Search Advisor 등록 및 sitemap 제출
  - robots.txt에 Yeti·NaverBot Allow 명시
  - 네이버 블로그·포스트·지식iN에 브랜드 언급 확보 (C-rank 간접 영향)

[네이버 AI 탭 대응 (2026.04 베타 출시)]
서비스: 통합검색 내 별도 탭, 대화형 에이전틱 검색
특징: 쇼핑·플레이스·지도 등 네이버 서비스와 연계, 멀티턴 대화 지원
최적화 방향: AI 브리핑 최적화와 동일 기반 + 구조화 데이터(FAQPage·HowTo) 강화
```

**중국 시장 특별 고려사항:**

```
- ICP 번호 없으면 중국 내 AI 플랫폼 인덱싱 불가
- 바이두 SearchConsole(百度搜索资源平台) 등록 여부 확인
- CDN: 중국 내 서버 필요 (글로벌 CDN 차단 가능)
- robots.txt: Baiduspider·SogouBot·360Spider 허용 여부 별도 확인
- Great Firewall: 사이트 접근 가능 여부 외부 도구로 확인
```

예상 작업량: 신규 약 380줄

---

#### 2-3. `geo-platform-optimizer` 언어 분기 추가

현재 5개 플랫폼(Google AIO·Perplexity·ChatGPT·Copilot·Grok) → 언어별 플랫폼 분기로 확장

추가 로직:

```
실행 시 SITE_LANGS를 확인한다.
- "zh" 포함 → geo-lang-platform의 중국 AI 플랫폼 분석 실행
- "ko" 포함 → 네이버 AI 브리핑·AI 탭 최적화 항목 추가
              (C-rank·D.I.A. 구조, Yeti 허용, Naver Search Advisor 등록)
              ※ 클로바X 2026-04-09 종료 — 목록에서 제외
- "ja" 포함 → Yahoo! Japan AI 최적화 항목 추가
- "es" 포함 → 스페인어권 플랫폼 + hreflang es-ES/es-MX 분리 확인
```

예상 작업량: 400줄 → 약 520줄 (+120줄)

---

#### 2-4. `geo-schema` 다국어 스키마 추가

추가할 스키마 타입 및 속성:

| 스키마 / 속성 | 용도 | 예시 |
|---|---|---|
| `inLanguage` | 페이지 언어 명시 | `"inLanguage": "ko-KR"` |
| `availableLanguage` | 사이트 지원 언어 목록 | `"availableLanguage": ["ko", "en", "ja"]` |
| `translationOfWork` | 이 페이지가 번역본임을 원본에 연결 | 번역 페이지 → 원본 URL 참조 |
| `workTranslation` | 원본 페이지에서 번역본을 연결 | 원본 페이지 → 번역 URL 참조 |
| `LocationFeatureSpecification` | 지역별 서비스 가용 언어 | 로컬 비즈니스 다국어 지원 표기 |

예상 작업량: 541줄 → 약 650줄 (+109줄)

---

### Phase 3 — 출력 다국어화

**목표:** 스킬 자체 출력을 5개 언어로 지원

#### 3-1. OUTPUT_LANG 시스템 설계

```
변수: OUTPUT_LANG
기본값: 사이트 감지 언어 (SITE_LANGS[0]) 또는 "ko"
변경: /geo lang 명령어 실행 시

지원 언어:
  ko — 한국어 (기본)
  en — English
  ja — 日本語
  zh — 中文 (简体)
  es — Español
```

#### 3-2. 각 스킬 출력 템플릿 다국어화

각 스킬의 L1/L2/L3 출력 템플릿에 다국어 버전을 추가하는 방식.

우선순위:
1. geo-audit (핵심 보고서)
2. geo-crawlers (봇 현황표)
3. geo-citability (점수 보고서)
4. 나머지 스킬 순차 적용

템플릿 구조 (각 스킬에 추가):

```markdown
## 다국어 출력 분기

OUTPUT_LANG 값에 따라 아래 템플릿을 선택하여 출력한다.

### ko 출력 (기존 템플릿 유지)
[기존 내용]

### en 출력
[영어 버전 템플릿]

### ja 출력
[일본어 버전 템플릿]

### zh 출력
[중국어 간체 버전 템플릿]

### es 출력
[스페인어 버전 템플릿]
```

예상 작업량: 스킬당 +50~100줄 (7개 주요 스킬 기준 총 +500줄)

---

#### 3-3. `geo-content` 번역 품질 평가 추가

추가할 평가 항목 (기존 E-E-A-T 4차원 외 별도 모듈):

**번역 품질 감지 신호 (다국어 사이트 전용)**

| 신호 | 확인 방법 |
|---|---|
| 브랜드명 일관성 | 언어별 페이지에서 브랜드명 표기 통일 여부 |
| 날짜 형식 | 언어별 날짜 포맷 (ko: 2026년 5월 9일 / en: May 9, 2026 / ja: 2026年5月9日) |
| 통화·수치 단위 | 언어별 통화·단위 로컬라이즈 여부 |
| 문화적 참조 | 원본 언어 문화 참조를 대상 언어 기준으로 변환했는지 |
| 콘텐츠 볼륨 편차 | 언어별 단어 수 차이 30% 이상이면 콘텐츠 누락 의심 |

예상 작업량: 334줄 → 약 420줄 (+86줄)

---

### Phase 4 — 마무리 및 통합

#### 4-1. `geo-llmstxt` 다국어 생성 로직 추가

다국어 llms.txt 구조:

```
# [사이트명] — Multilingual
> [영어 사이트 설명]

## Korean (ko)
> [한국어 사이트 설명]
- 주요 콘텐츠: [ko URL 목록]

## English (en)
> [영어 설명]
- Main Content: [en URL 목록]

## Japanese (ja)
> [일본어 설명]
- メインコンテンツ: [ja URL 목록]

## Chinese Simplified (zh-CN)
> [중국어 설명]
- 主要内容: [zh URL 목록]

## Spanish (es)
> [스페인어 설명]
- Contenido Principal: [es URL 목록]

## Sitemap
- [sitemap-index URL]
```

예상 작업량: 422줄 → 약 520줄 (+98줄)

---

#### 4-2. CLAUDE.md 및 README.md 갱신

- CLAUDE.md: 신규 스킬 2개 추가, 다국어 지원 범위 기록
- README.md: 레벨 매트릭스에 `geo-multilang`·`geo-lang-platform` 추가, 명령어 일람 갱신

---

## 5. 상세 변경 설계

### OUTPUT_LANG 변수 설계

```
[초기화 순서]
1. 사용자가 /geo lang <코드> 명시적으로 입력한 경우 → 해당 값 사용
2. 미입력 + SITE_LANGS 감지된 경우 → SITE_LANGS[0] 사용 (사이트 주 언어 기준)
3. 미입력 + 감지 실패 → "ko" 기본값

[선택 메뉴 (언어 감지 실패 시)]
분석 결과를 어떤 언어로 받으시겠어요?
  1) 한국어 (ko)
  2) English (en)
  3) 日本語 (ja)
  4) 中文简体 (zh)
  5) Español (es)
번호를 입력해 주세요:
```

### hreflang 검사 체크리스트

```
필수 확인:
□ <link rel="alternate" hreflang="x-default"> 존재
□ 각 언어 버전 hreflang 태그 존재
□ hreflang 언어 코드 ISO 639-1 준수 (en, ko, ja, zh, es)
□ hreflang 국가 코드 ISO 3166-1 준수 (en-US, ko-KR, ja-JP, zh-CN, zh-TW, es-ES, es-MX)
□ 양방향 참조 (A페이지가 B를 가리키면 B도 A를 가리켜야 함)

경고 확인:
△ 언어 버전 URL이 robots.txt에 차단되지 않았는가
△ 각 언어 URL이 실제로 200 응답하는가
△ canonical 태그가 hreflang과 충돌하지 않는가
△ 언어별 sitemap에 hreflang 정보 포함 여부
```

---

## 6. 작업량 및 일정 요약

| Phase | 대상 스킬 | 예상 추가 줄 수 | 난이도 |
|---|---|---|---|
| Phase 0 | 설계 문서 작성 | 약 200줄 | 낮음 |
| Phase 1 | 오케스트레이터·geo-crawlers·geo-technical | 약 350줄 | 중간 |
| Phase 2 | geo-multilang(신규)·geo-lang-platform(신규)·geo-platform-optimizer·geo-schema | 약 1,030줄 | 높음 |
| Phase 3 | 7개 스킬 출력 다국어화·geo-content | 약 590줄 | 중간 |
| Phase 4 | geo-llmstxt·CLAUDE.md·README.md | 약 200줄 | 낮음 |
| **합계** | **신규 2개 + 변경 7개 + 문서 2개** | **약 2,370줄** | |

업그레이드 완료 후 총 스킬 수: **15개 → 17개**
업그레이드 완료 후 총 줄 수: 약 **5,700줄 → 8,070줄**

---

## 7. 실행 순서 (Phase별 작업 지시)

```
Phase 0: 설계 문서 완성 (본 파일)
         → references/lang-platform-map.md 작성
         → references/hreflang-checklist.md 작성

Phase 1: /cp write 순서로 실행
  1. geo/SKILL.md (오케스트레이터) 수정
  2. skills/geo-crawlers/SKILL.md 수정
  3. skills/geo-technical/SKILL.md 수정

Phase 2:
  4. skills/geo-multilang/SKILL.md 신규 작성
  5. skills/geo-lang-platform/SKILL.md 신규 작성
  6. skills/geo-platform-optimizer/SKILL.md 수정
  7. skills/geo-schema/SKILL.md 수정

Phase 3:
  8. skills/geo-content/SKILL.md 수정
  9. geo-audit / geo-crawlers / geo-citability 출력 다국어화 (en·ja·zh·es 템플릿 추가)
  10. 나머지 스킬 출력 다국어화

Phase 4:
  11. skills/geo-llmstxt/SKILL.md 수정
  12. CLAUDE.md 갱신
  13. README.md 갱신
```

---

## 8. 정합성 검증 체크리스트 (완료 후)

```
□ OUTPUT_LANG 변수가 모든 스킬에서 일관되게 참조되는가
□ SITE_LANGS 변수가 오케스트레이터에서 서브스킬로 올바르게 전달되는가
□ geo-multilang이 L1 차단 처리를 올바르게 하는가
□ 중국 AI 플랫폼 분석 시 ICP 번호 항목이 포함되는가
□ hreflang 양방향 참조 검사가 geo-technical과 geo-multilang 양쪽에서 중복 없이 처리되는가
□ 각 스킬의 출력 파일명에 언어 코드가 포함되는가 (예: GEO-크롤러-분석-ko.md)
□ README.md 명령어 일람에 신규 명령어 2개가 추가됐는가
□ CLAUDE.md 주요 파일 목록에 신규 스킬 2개가 추가됐는가
```
