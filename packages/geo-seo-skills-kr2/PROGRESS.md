# geo-seo-skills-kr 제작 진행 현황

## 프로젝트 개요

- **목적:** GEO·SEO 분석 스킬 라이브러리 (사용자 레벨별 출력 분기)
- **위치:** `09_utils/geo-seo-skills-kr/`
- **기존 프로젝트와 관계:** `geo-seo-claude-main`과 별개로 완전 신규 제작
- **레벨 시스템:** L1(마케팅 담당자) / L2(웹마스터·운영자) / L3(개발자)

---

## 핵심 설계 원칙

- 분석 깊이는 모든 레벨에서 동일, **출력 방식만 레벨별로 분기**
- L1: 비즈니스 언어, 담당자 전달 형태
- L2: FTP·CMS·파일 수정 단계별 안내
- L3: 코드 스니펫, 기술 명세, CLI 명령어 포함
- 에이전트 파일 없이 단일 SKILL.md 구조 (Claude 웹·Code 모두 호환)
- 모든 출력은 한국어 (URL·코드·기술 용어는 원문 유지)

---

## 주요 결정 사항

| 결정 | 내용 |
|---|---|
| 레벨 명칭 | 사용자에게는 역할명 노출, 내부는 L1/L2/L3 유지 |
| `/geo level` | 포함 — 언제든 레벨 변경 가능 |
| 레벨 초과 접근 | "직접 실행 or 담당자 전달 메모 생성" 2가지 선택 |
| L1 기술/스키마 분석 | 생략하지 않고 실행, 비기술 언어로 요약 출력 |
| 전체 감사 흐름 | 5개 영역 모든 레벨 동일 실행 |
| 코어/확장 계층 분리 | 코어(Claude 웹·Code 모두): WebFetch 기반 / 확장(Claude Code 전용): Playwright+파일시스템 |
| CCBot 완전 제거 | 상업적 GEO 관점에서 오픈소스 LLM 생태계용 봇은 우선순위 낮음 |
| Grok 봇 3종 추가 | xAI 점유율 고려 (GrokBot·xAI-Grok·Grok-DeepSearch) |
| geo-compare 점수 분리 | 사이트 설정(30점)과 페이지 콘텐츠(30점) 합산 없이 각각 표시 |
| CRITICAL/HIGH/MEDIUM/LOW | 심각도 4단계 분류 — 처리 기한(1주/1달/3달/순차) 연동 |

---

## 스킬 제작 계획 및 현황

### Phase 1 — 기반 구조

| 파일 | 상태 | 최종 줄 수 | 완료일 |
|---|---|---|---|
| `geo/SKILL.md` | ✅ 완료 | 약 445줄 | 2026-05-09 (업그레이드) |

**주요 내용:**
- 레벨 선택 로직, `/geo level` 변경 기능
- L1·L2·L3 명령어 메뉴 (레벨별 노출 명령어 다름)
- 22개 명령어 → 서브스킬 라우팅 테이블
- 레벨 초과 접근 시 "담당자 전달 메모 생성" 옵션
- OUTPUT_LANG·SITE_LANGS 다국어 변수 지원
- `/geo lang` 명령어 (언어 설정)
- 환경 분기 가이드 섹션: 코어 계층 vs 확장 계층 안내
- L3 메뉴에 `/geo realtime`, `/geo tracker`, `/geo batch` 추가

---

### Phase 2 — 공통 스킬 (L1+L2+L3)

| 순서 | 스킬 | 상태 | 최종 줄 수 | 완료일 |
|---|---|---|---|---|
| 1 | `skills/geo-audit/SKILL.md` | ✅ 완료 | 약 340줄 | 2026-05-09 (업그레이드) |
| 2 | `skills/geo-content/SKILL.md` | ✅ 완료 | 약 390줄 | 2026-05-09 (업그레이드) |
| 3 | `skills/geo-citability/SKILL.md` | ✅ 완료 | 345줄 | 2026-05-03 |
| 4 | `skills/geo-brand/SKILL.md` | ✅ 완료 | 565줄 | 2026-05-07 |
| 5 | `skills/geo-crawlers/SKILL.md` | ✅ 완료 | 475줄 | 2026-05-09 (업그레이드) |
| 6 | `skills/geo-brand-mentions/SKILL.md` | ✅ 완료 | 약 440줄 | 2026-05-09 (업그레이드) |
| 7 | `skills/geo-platform-optimizer/SKILL.md` | ✅ 완료 | 515줄 | 2026-05-09 (업그레이드) |
| 8 | `skills/geo-report/SKILL.md` | ✅ 완료 | 약 368줄 | 2026-05-09 (업그레이드) |

**geo-audit 추가 사항 (2026-05-09):**
- 심각도 분류 4단계 섹션 추가 (CRITICAL/HIGH/MEDIUM/LOW)
- CRITICAL 항목 발견 시 경고 배너 출력

**geo-content 추가 사항 (2026-05-09):**
- 번역 품질 평가 모듈 신규 (5-1단계): 번역 완성도·현지화 신호·기계 번역 감지·5단계 등급
- OUTPUT_LANG 출력 규칙 블록 추가

**geo-crawlers 추가 사항 (2026-05-09):**
- 봇 20개 (글로벌 13 + 지역 7) — Naver·Baidu·야후재팬 포함
- 전략 D~G robots.txt 코드 (언어별 지역 플랫폼 전략)

**geo-platform-optimizer 추가 사항 (2026-05-09):**
- 지역 플랫폼 평가: 네이버 AI 브리핑·Yahoo! Japan AI·Baidu Ernie
- 전략별 점수 조건부 산출
- L1/L2/L3 출력 템플릿 지역 섹션 추가

**geo-brand 주요 내용 (2026-05-07 신규 추가):**
- Gap 분석: 원하는 포지셔닝 vs 현재 인식 수치화
- 콘텐츠 연결: Gap → /cp prep 자동 투입
- 순환 추적: --track으로 4주마다 ΔGap 측정
- 5가지 실측 지표: 포지셔닝 반영률 / SOV / BCI / 채널 인용률 / 맥락 일치율
- 5단계 Gap 등급: INVISIBLE → DISTANT → PARTIAL → ALIGNED → ANCHORED
- 출력 파일 3종: GEO-BRAND-GAP-*.md / GEO-BRAND-CP-인풋-*.md / GEO-BRAND-BASELINE-*.json

**geo-report 추가 사항 (2026-05-09):**
- 3단계 우선순위 → CRITICAL/HIGH/MEDIUM/LOW 4단계로 교체
- L1 출력: "이번 주 할 일(CRITICAL)" + "이번 달 할 일(HIGH/MEDIUM)" 2단계
- L2 체크리스트: CRITICAL/HIGH/MEDIUM/LOW 섹션 분리
- L3 로드맵: Sprint 1/2/3 → 1주차/2주차/3~4주차/이후

---

### Phase 3 — L2+L3 스킬

| 순서 | 스킬 | 상태 | 최종 줄 수 | 완료일 |
|---|---|---|---|---|
| 1 | `skills/geo-technical/SKILL.md` | ✅ 완료 | 약 380줄 | 2026-05-09 (업그레이드) |
| 2 | `skills/geo-llmstxt/SKILL.md` | ✅ 완료 | 약 500줄 | 2026-05-09 (업그레이드) |
| 3 | `skills/geo-compare/SKILL.md` | ✅ 완료 | 약 490줄 | 2026-05-09 (업그레이드) |

**geo-technical 추가 사항 (2026-05-09):**
- 0단계: 렌더링 방식 사전 판정 (SSR/하이브리드/CSR+SSR신호/순수CSR 4단계)
- hreflang 분석 모듈 (1-1단계): 다국어 조건부 점수 공식

**geo-llmstxt 추가 사항 (2026-05-09):**
- 다국어 llms.txt 구조 섹션: 루트 + /ko·/en·/ja·/zh·/es 언어별 파일 템플릿
- OUTPUT_LANG 출력 규칙 블록 추가

**geo-compare 추가 사항 (2026-05-09):**
- OUTPUT_LANG 출력 규칙 블록 추가

---

### Phase 4 — L3 전용 스킬

| 순서 | 스킬 | 상태 | 최종 줄 수 | 완료일 |
|---|---|---|---|---|
| 1 | `skills/geo-schema/SKILL.md` | ✅ 완료 | 692줄 | 2026-05-09 (업그레이드) |
| 2 | `skills/geo-proposal/SKILL.md` | ✅ 완료 | 278줄 | 2026-05-09 (업그레이드) |
| 3 | `skills/geo-prospect/SKILL.md` | ✅ 완료 | 330줄 | 2026-05-03 |
| 4 | `skills/geo-report-pdf/SKILL.md` | ✅ 완료 | 318줄 | 2026-05-09 (업그레이드) |

**geo-schema 추가 사항 (2026-05-09):**
- 다국어 스키마 4종: inLanguage·availableLanguage·translationOfWork·workTranslation
- L3 출력 템플릿 지역 섹션 추가

---

### Phase 5 — 다국어 업그레이드

완료일: 2026-05-09. 코어 17개 스킬 전체에 OUTPUT_LANG·SITE_LANGS 지원 추가.

#### Phase 0 — 참조 자료

| 파일 | 내용 |
|---|---|
| `references/lang-platform-map.md` | 봇 20개·전략 A~G·언어별 AI 플랫폼 매핑 |
| `references/hreflang-checklist.md` | 필수 5개·경고 5개·점수 산정 기준 |

#### Phase 1 — 오케스트레이터·크롤러·기술 업그레이드

| 파일 | 주요 추가 내용 |
|---|---|
| `geo/SKILL.md` | OUTPUT_LANG·SITE_LANGS 변수, `/geo lang` 명령어 |
| `skills/geo-crawlers/SKILL.md` | 봇 20개(글로벌 13+지역 7), 전략 D~G robots.txt |
| `skills/geo-technical/SKILL.md` | hreflang 분석 모듈, 다국어 조건부 점수 공식 |

#### Phase 2 — 다국어 전용 스킬 신규 생성

| 스킬 | 상태 | 줄 수 | 완료일 |
|---|---|---|---|
| `skills/geo-multilang/SKILL.md` | ✅ 완료 | 410줄 | 2026-05-09 |
| `skills/geo-lang-platform/SKILL.md` | ✅ 완료 | 416줄 | 2026-05-09 |

**geo-multilang 주요 내용:**
- 다국어 GEO 통합 진단 (hreflang·콘텐츠·AI 가시성)
- 언어별 AI 플랫폼 노출 현황 비교

**geo-lang-platform 주요 내용:**
- 언어별 AI 플랫폼 매핑 (ko/en/ja/zh/es)
- 봇별 전략 A~G 자동 선택

#### Phase 3 — 공통·L2+L3 스킬 OUTPUT_LANG 반영

geo-audit·geo-content·geo-citability·geo-brand-mentions·geo-report·geo-compare 6개 스킬에:
- description OUTPUT_LANG 언급
- 헤더 파일명 분기 (OUTPUT_LANG별)
- OUTPUT_LANG 출력 규칙 블록

#### Phase 4 — llmstxt·오케스트레이터 최종 정합

- `geo-llmstxt`: 다국어 llms.txt 구조 신규 섹션
- `geo/SKILL.md`: 출력 파일 목록에 `/geo brand` 행 추가
- 전체 17개 스킬 정합성 검증 완료

---

### Phase 6 — 확장 계층 구현

완료일: 2026-05-09. Claude Code 전용 4개 스킬 + 코어 스킬 3개 업그레이드.

#### A — 코어 스킬 업그레이드

| 코드 | 파일 | 변경 내용 | 완료일 |
|---|---|---|---|
| A-1 | `skills/geo-audit/SKILL.md` | 심각도 4단계(CRITICAL/HIGH/MEDIUM/LOW) 섹션 추가, 5단계 재번호화 | 2026-05-09 |
| A-2 | `skills/geo-technical/SKILL.md` | 렌더링 방식 사전 판정(0단계): SSR/하이브리드/CSR+SSR신호/순수CSR 4단계 | 2026-05-09 |
| A-3 | `skills/geo-report/SKILL.md` | 3단계 우선순위 → 4단계 심각도, L3 로드맵 Sprint→주차 구조 | 2026-05-09 |

#### B — 오케스트레이터 업그레이드

| 코드 | 파일 | 변경 내용 | 완료일 |
|---|---|---|---|
| B | `geo/SKILL.md` | 환경 분기 가이드 섹션, L3 메뉴 realtime·tracker·batch 추가, 라우팅 테이블 3행 추가 | 2026-05-09 |

#### C~F — 확장 계층 신규 스킬

| 코드 | 스킬 | 상태 | 줄 수 | 완료일 |
|---|---|---|---|---|
| C | `skills/geo-realtime/SKILL.md` | ✅ 완료 | 392줄 | 2026-05-09 |
| D | `skills/geo-tracker/SKILL.md` | ✅ 완료 | 229줄 | 2026-05-09 |
| E | `skills/geo-batch/SKILL.md` | ✅ 완료 | 166줄 | 2026-05-09 |
| F | `skills/geo-code/SKILL.md` | ✅ 완료 | 267줄 | 2026-05-09 |

**geo-realtime 주요 내용:**
- browser-citation.js 연동 (CDP 포트 9222, 7개 플랫폼)
- 기본 모드: 10개 표준 질문 자동 생성
- --cp 모드: topics.csv + H2/H3에서 질문 추출
- --track: BASELINE realtime_snapshots 배열에 인용률 기록
- 출력: GEO-REALTIME-[도메인]-[날짜].md

**geo-tracker 주요 내용:**
- GEO-BRAND-BASELINE-*.json 수집 → 5개 지표 시계열 추적
- 추이 판정: 개선(+5 이상)/정체(±4)/악화(-5 이하)
- realtime_snapshots 통합 표시
- --export: CSV 내보내기
- 출력: GEO-TRACKER-[도메인]-[날짜].md

**geo-batch 주요 내용:**
- 최대 20개 도메인 순차 스캔
- 8개 항목 확인 (HTTPS·AI봇·llms.txt·sitemap·스키마·렌더링·meta·OG)
- 간이 점수: `100 - (FAIL수×15) - (WARN수×5)`
- 출력: GEO-BATCH-[날짜].md

**geo-code 주요 내용 (오케스트레이터):**
- `/geo-code init`: 5항목 환경 점검 (Node.js/Playwright/Chromium/browser-citation.js/Chrome CDP)
- `/geo-code pipeline <url>`: audit → brand(BASELINE 없을 때) → realtime(--track) → tracker 자동 순서
- `/geo-code pipeline <url1> <url2>...`: batch → 선별(--top N) → 도메인별 순차 실행
- `/geo-code status`: 분석 파일·BASELINE·CP 연동 현황 점검

---

## 현재 디렉토리 구조

```
geo-seo-skills-kr/
├── PROGRESS.md                         ← 이 파일
├── README.md                           ✅ (22개 스킬 반영, 코어/확장 계층)
├── GUIDE.md                            ✅ (22개 스킬 반영, 확장 계층 시작 절차)
├── references/
│   ├── lang-platform-map.md            ✅ 봇 20개·전략 A~G 매핑
│   └── hreflang-checklist.md           ✅ hreflang 필수·경고 항목
├── geo/
│   └── SKILL.md                        ✅ 오케스트레이터 (환경 분기 가이드 포함)
└── skills/
    ├── geo-audit/
    │   └── SKILL.md                    ✅ (CRITICAL/HIGH/MEDIUM/LOW 추가)
    ├── geo-content/
    │   └── SKILL.md                    ✅ (번역 품질 평가 모듈 추가)
    ├── geo-citability/
    │   └── SKILL.md                    ✅
    ├── geo-brand/
    │   └── SKILL.md                    ✅ (Gap 분석·순환 추적·BASELINE)
    ├── geo-crawlers/
    │   └── SKILL.md                    ✅ (봇 20개·전략 D~G 추가)
    ├── geo-brand-mentions/
    │   └── SKILL.md                    ✅
    ├── geo-platform-optimizer/
    │   └── SKILL.md                    ✅ (지역 플랫폼 평가 추가)
    ├── geo-report/
    │   └── SKILL.md                    ✅ (4단계 심각도·주차별 로드맵)
    ├── geo-technical/
    │   └── SKILL.md                    ✅ (렌더링 사전 판정·hreflang 모듈)
    ├── geo-llmstxt/
    │   └── SKILL.md                    ✅ (다국어 llms.txt 구조 추가)
    ├── geo-compare/
    │   └── SKILL.md                    ✅
    ├── geo-multilang/
    │   └── SKILL.md                    ✅ (신규, 다국어 GEO 통합 진단)
    ├── geo-lang-platform/
    │   └── SKILL.md                    ✅ (신규, 언어별 AI 플랫폼 매핑)
    ├── geo-schema/
    │   └── SKILL.md                    ✅ (다국어 스키마 4종 추가)
    ├── geo-proposal/
    │   └── SKILL.md                    ✅
    ├── geo-prospect/
    │   └── SKILL.md                    ✅
    ├── geo-report-pdf/
    │   └── SKILL.md                    ✅
    ├── geo-realtime/                   ← 확장 계층 (Claude Code 전용)
    │   └── SKILL.md                    ✅ (신규, browser-citation 연동)
    ├── geo-tracker/                    ← 확장 계층
    │   └── SKILL.md                    ✅ (신규, Gap 시계열 추적)
    ├── geo-batch/                      ← 확장 계층
    │   └── SKILL.md                    ✅ (신규, 도메인 배치 스캔)
    └── geo-code/                       ← 확장 계층 오케스트레이터
        └── SKILL.md                    ✅ (신규, pipeline 자동화)
```

---

## 스킬 현황 요약

| 계층 | 스킬 수 | 환경 |
|---|---|---|
| 코어 계층 | 18개 (오케스트레이터 포함) | Claude 웹·Code 모두 |
| 확장 계층 | 4개 | Claude Code 전용 |
| **합계** | **22개** | |

### 코어 계층 18개

| L1+L2+L3 (8개) | L2+L3 (5개) | L3 전용 (4개) | 오케스트레이터 (1개) |
|---|---|---|---|
| geo-audit | geo-technical | geo-schema | geo (오케스트레이터) |
| geo-content | geo-llmstxt | geo-proposal | |
| geo-citability | geo-compare | geo-prospect | |
| geo-brand | geo-multilang | geo-report-pdf | |
| geo-crawlers | geo-lang-platform | | |
| geo-brand-mentions | | | |
| geo-platform-optimizer | | | |
| geo-report | | | |

### 확장 계층 4개 (Claude Code 전용)

| 스킬 | 역할 |
|---|---|
| geo-realtime | browser-citation 실측 인용률 측정 |
| geo-tracker | Gap 시계열 추적·시각화 |
| geo-batch | 복수 도메인 배치 스캔 |
| geo-code | 확장 계층 파이프라인 오케스트레이터 |

---

## 현재 상태

**전체 완료. 총 22개 스킬 구현.**

- Phase 1~4: 코어 계층 18개 스킬 (오케스트레이터 포함)
- Phase 5: 다국어 업그레이드 (OUTPUT_LANG·SITE_LANGS·봇 20개·전략 A~G)
- Phase 6: 확장 계층 4개 스킬 + 코어 스킬 3개 업그레이드
- README.md / GUIDE.md: 22개 스킬 전체 반영 완료
