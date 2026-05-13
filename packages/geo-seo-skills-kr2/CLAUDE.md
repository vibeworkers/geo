# CLAUDE.md

## 프로젝트 개요

GEO·SEO 분석 스킬 라이브러리. 사용자 레벨(L1 마케팅 담당자 / L2 웹마스터 / L3 개발자)에 따라 동일한 분석 깊이를 유지하면서 출력 방식만 분기한다.

## 주요 파일 목록

| 파일 | 역할 |
|---|---|
| `README.md` | 17개 스킬 통합 가이드 — 레벨 매트릭스·명령어 일람·워크플로 (기술 참조용) |
| `GUIDE.md` | 초보자 사용 가이드 — GEO 개념·레벨별 단계 안내·FAQ |
| `PROGRESS.md` | 전체 진행 현황, 스킬별 구성 요약, 다음 작업 |
| `geo/SKILL.md` | 오케스트레이터 — 레벨 선택, 명령어 라우팅 |
| `skills/geo-audit/SKILL.md` | 전체 GEO 감사 (L1+L2+L3) |
| `skills/geo-content/SKILL.md` | E-E-A-T 콘텐츠 평가 (L1+L2+L3) |
| `skills/geo-citability/SKILL.md` | AI 인용 가능성 평가 (L1+L2+L3) |
| `skills/geo-brand/SKILL.md` | AI 브랜드 인식 Gap 추적 (L1+L2+L3) |
| `skills/geo-crawlers/SKILL.md` | AI 크롤러 접근 진단 (L1+L2+L3) — 봇 20개·전략 A~G |
| `skills/geo-brand-mentions/SKILL.md` | 브랜드 언급 분석 (L1+L2+L3) |
| `skills/geo-platform-optimizer/SKILL.md` | 플랫폼별 최적화 (L1+L2+L3) |
| `skills/geo-report/SKILL.md` | 분석 결과 보고서 (L1+L2+L3) |
| `skills/geo-lang-platform/SKILL.md` | 언어별 AI 플랫폼 매핑·봇 전략 (L1+L2+L3) |
| `skills/geo-technical/SKILL.md` | 기술 SEO 진단·hreflang 분석 (L2+L3) |
| `skills/geo-llmstxt/SKILL.md` | llms.txt 진단·생성 (L2+L3) |
| `skills/geo-compare/SKILL.md` | GEO 경쟁 비교 분석 (L2+L3) |
| `skills/geo-multilang/SKILL.md` | 다국어 GEO 통합 진단 — hreflang·콘텐츠·AI가시성 (L2+L3) |
| `skills/geo-schema/SKILL.md` | JSON-LD 스키마 생성 (L3) |
| `skills/geo-proposal/SKILL.md` | GEO 개선 제안서 (L3) |
| `skills/geo-prospect/SKILL.md` | 잠재 고객 빠른 스캔 (L3) |
| `skills/geo-report-pdf/SKILL.md` | PDF 보고서 생성 (L3) |
| `skills/geo-realtime/SKILL.md` | AI 인용 실측 — Code 전용 확장 계층 (L3) |
| `skills/geo-tracker/SKILL.md` | Gap 시계열 추적 — Code 전용 확장 계층 (L3) |
| `skills/geo-batch/SKILL.md` | 도메인 배치 스캔 — Code 전용 확장 계층 (L3) |
| `skills/geo-code/SKILL.md` | 확장 계층 오케스트레이터 — Code 전용 (L3) |

## 핵심 설계 원칙

- 분석 깊이 동일, 출력 방식만 레벨별 분기
- 에이전트 파일 없이 단일 SKILL.md 구조 (Claude 웹·Code 모두 호환)
- 환경 분기 패턴: Claude Code → Bash / Claude 웹 → WebFetch + 외부도구(httpstatus.io 등)
- L1 접근 불가 스킬: 안내 메시지 + 개발팀 전달 텍스트 출력 후 중단

## 주요 결정 사항

| 결정 | 이유 |
|---|---|
| CCBot 완전 제거 | 상업적 GEO 관점에서 오픈소스 LLM 생태계용 봇은 우선순위 낮음 |
| Grok 봇 3종 추가 | xAI 점유율 고려 (GrokBot·xAI-Grok·Grok-DeepSearch) |
| Claude 웹/Code 환경 분기 | Bash를 제거하지 않고 환경별로 분리하여 두 환경 모두 지원 |
| geo-compare 점수 분리 | 사이트 설정(도메인 루트 30점)과 페이지 콘텐츠(URL 기준 30점)를 합산하지 않고 각각 표시 — 성격이 다른 두 레벨을 단일 점수로 합치면 의미가 흐려짐 |

## 진행 상황

- 2026-05-03: Phase 1 완료 — `geo/SKILL.md` (오케스트레이터, 335줄)
- 2026-05-03: Phase 2 완료 — 공통 스킬 7개 (geo-audit·content·citability·crawlers·brand-mentions·platform-optimizer·report)
- 2026-05-03: Phase 3 완료 — L2+L3 스킬 3개 (geo-technical·llmstxt·compare)
- 2026-05-03: Phase 4 완료 — L3 전용 스킬 4개 (geo-schema·proposal·prospect·report-pdf)
- **전체 완료: 총 14개 스킬**
- 2026-05-03: 정합성 검증 완료 — 7개 카테고리 전수 검사, 불일치 9건 수정
- 2026-05-05: README.md 생성 — 14개 스킬 통합 가이드 (333줄, 레벨 매트릭스·명령어 코드블록·워크플로 예시 포함)
- 2026-05-05: GUIDE.md 생성 — 초보자 사용 가이드 (364줄, GEO 개념 설명·레벨별 단계 안내·FAQ 포함)
- 2026-05-07: `/geo brand` 스킬 신규 추가 — AI 브랜드 인식 Gap 추적 스킬 완성
  - **설계 차별화:** 함샤우트(현재 인식 1회 진단) vs `/geo brand`(원하는 포지셔닝 vs 현재 인식 Gap 수치화 + CP 콘텐츠 자동 연결 + 4주 순환 추적)
  - **3가지 핵심 기능:** ① Gap 분석(COMP 포지셔닝 기준) ② 콘텐츠 연결(Gap → /cp prep 투입 자동화) ③ 순환 추적(--track으로 ΔGap 측정)
  - **5가지 실측 지표:** 포지셔닝 반영률, SOV, BCI, 채널 인용률, 맥락 일치율 (모두 0~100점)
  - **5단계 Gap 등급:** INVISIBLE(0-20) → DISTANT(21-40) → PARTIAL(41-60) → ALIGNED(61-80) → ANCHORED(81+)
  - **3가지 출력 파일:** GEO-BRAND-GAP-*.md(메인 보고서), GEO-BRAND-CP-인풋-*.md(콘텐츠 계획), GEO-BRAND-BASELINE-*.json(추적 스냅샷)
  - **구현 완료:** skills/geo-brand/SKILL.md(565줄), geo/SKILL.md 라우팅 추가(routing table + L1/L2/L3 메뉴), README.md 레벨 매트릭스·명령어 일람·상세 섹션 추가

## 정합성 검증 결과 (2026-05-03)

| 수정 항목 | 내용 |
|---|---|
| geo/SKILL.md 출력 파일 목록 | 7개 파일명 통일 + 2개 신규 추가 (총 14개) |
| geo/SKILL.md 명령어 설명 | /geo compare·prospect 설명 실제 기능으로 교정 |
| geo-proposal 참조 파일명 | `GEO-감사-보고서.md`로 통일 |
| geo-prospect AI 봇 목록 | 6개 → 10개 (Bingbot·xAI-Grok·Grok-DeepSearch·Google-Extended 추가) |
| geo-report-pdf 환경 분기 | Claude 웹 환경 안내 블록 추가 |
| geo-technical L1 차단 패턴 | 인라인 메시지 → `## L1 접근 안내` 섹션으로 통일 |
| geo-content 등급표 누락 | 5단계 점수-등급 표 추가 (0–19 위험 포함) |

## 다국어 업그레이드 진행 현황 (2026-05-09)

### Phase 0 완료
- `references/lang-platform-map.md` — 봇 20개·전략 A~G·언어별 AI 플랫폼 매핑
- `references/hreflang-checklist.md` — 필수 5개·경고 5개·점수 산정 기준

### Phase 1 완료
- `geo/SKILL.md` — 언어 시스템(SITE_LANGS·OUTPUT_LANG·/geo lang 명령어) 추가
- `skills/geo-crawlers/SKILL.md` — 봇 20개(글로벌 13+지역 7), 전략 D~G robots.txt 코드
- `skills/geo-technical/SKILL.md` — hreflang 분석 모듈(1-1단계), 다국어 조건부 점수 공식

### Phase 2 완료
- `skills/geo-multilang/SKILL.md` 신규 생성 (410줄) — 다국어 GEO 통합 진단
- `skills/geo-lang-platform/SKILL.md` 신규 생성 (416줄) — 언어별 AI 플랫폼 매핑

### Phase 2 추가 완료 (2026-05-09)
- `skills/geo-platform-optimizer/SKILL.md` (400→515줄) — 지역 플랫폼 평가(네이버 AI 브리핑·Yahoo! Japan AI·Baidu Ernie), 전략별 점수 조건부 산출, L1/L2/L3 출력 템플릿 지역 섹션 추가
- `skills/geo-schema/SKILL.md` (541→692줄) — 다국어 스키마 4종(inLanguage·availableLanguage·translationOfWork·workTranslation) 코드 및 L3 출력 템플릿 반영

### Phase 3 완료 (2026-05-09)
- geo-audit·geo-content·geo-citability·geo-brand-mentions·geo-report·geo-compare 6개 스킬 — description OUTPUT_LANG 언급, 헤더 파일명 분기, OUTPUT_LANG 출력 규칙 블록 추가
- geo-content — 번역 품질 평가 모듈 신규 추가 (5-1단계): 번역 완성도·현지화 신호·기계 번역 감지·5단계 등급
- README.md — 17개 스킬 반영, 명령어 일람 geo-multilang·geo-lang-platform·/geo lang 추가
- GUIDE.md — 17개 스킬 반영, 다국어 GEO 섹션(9번) 신규 추가

### Phase 4 완료 (2026-05-09)
- `skills/geo-llmstxt/SKILL.md` — 다국어 llms.txt 구조 신규 섹션 추가: 루트 /llms.txt 템플릿, /ko·/en·/ja·/zh·/es 언어별 파일 템플릿, 배포 체크리스트, OUTPUT_LANG 출력 규칙 블록
- `geo/SKILL.md` — 출력 파일 목록에 `/geo brand` 행 추가 (GEO-BRAND-GAP-*.md · GEO-BRAND-CP-인풋-*.md · GEO-BRAND-BASELINE-*.json)
- 전체 정합성 검증 완료 — 17개 스킬 라우팅 테이블 일치, audience 필드 전수 확인

**다국어 업그레이드 전체 완료: Phase 0~4 완성, 총 17개 스킬**

## 확장 계층 구현 계획 (2026-05-09~)

### 설계 방향
- 코어 계층(17개 스킬): Claude 웹/Code 모두 호환, WebFetch 기반, 변경 없음
- 확장 계층(신규): Claude Code 전용, Playwright + 파일 시스템 연동

### 완료
- **A-1**: `skills/geo-audit/SKILL.md` — 심각도 분류 4단계(CRITICAL/HIGH/MEDIUM/LOW) 섹션 추가, 5단계 재번호화
- **A-2**: `skills/geo-technical/SKILL.md` — 렌더링 방식 사전 판정(0단계) 추가: SSR/하이브리드/CSR+SSR신호/순수CSR 4단계 판정
- **A-3**: `skills/geo-report/SKILL.md` — 30일 로드맵 정교화: Sprint 1/2/3 → 1주차(CRITICAL)/2주차(HIGH)/3~4주차(MEDIUM)/이후(LOW), 3단계 우선순위 기준표를 심각도 4단계로 교체, L1 출력 "이번 주/이번 달" 2단계로 단순화, L2 체크리스트 심각도별 섹션 분리, L3 로드맵 구조 변경
- **B**: `geo/SKILL.md` — 환경 분기 가이드 섹션 신규 추가, L3 메뉴 `/geo realtime` 항목 추가, 라우팅 테이블 `/geo realtime` 행 추가

- **C**: `skills/geo-realtime/SKILL.md` 신규 구현 완료 (392줄) — browser-citation.js 연동, CP topics.csv + H2/H3 질문 추출, geo-brand BASELINE --track 연동, 0단계 환경 확인(Node.js/Playwright/Chrome CDP), 인용 강도 4등급

- **D**: `skills/geo-tracker/SKILL.md` 신규 구현 완료 (229줄) — BASELINE 시계열, 5개 Gap 지표 추이, realtime_snapshots 통합, 등급 변화 판정, CSV 내보내기

- **E**: `skills/geo-batch/SKILL.md` 신규 구현 완료 (166줄) — 8개 간이 스캔 항목(HTTPS·AI봇·llms.txt·sitemap·스키마·렌더링·meta·OG), PASS/WARN/FAIL/ERR 판정, 간이 점수 산출, 비교 표 정렬

**확장 계층 A~E 전체 완료.**

- **README.md 업데이트 (333줄 → 581줄):** 22개 스킬 반영. 코어/확장 계층 구조 설명 추가, 레벨 매트릭스에 geo-multilang·geo-lang-platform·확장 계층 4개 추가, 명령어 일람 확장 계층 섹션 신규, 스킬별 상세에 6개 스킬 추가(geo-multilang·geo-lang-platform·geo-realtime·geo-tracker·geo-batch·geo-code), 워크플로 예시에 확장 계층·다국어 워크플로 추가, 환경 호환 테이블 3열로 확장.

- **F**: `skills/geo-code/SKILL.md` 신규 구현 완료 (267줄) — Claude Code 전용 확장 계층 오케스트레이터. init(환경 5항목 점검), pipeline(단일/복수 도메인 자동 파이프라인), status(폴더·BASELINE·CP 연동 상태 확인). geo/SKILL.md 환경 분기 가이드에 진입점 안내 추가.

## 마무리 정합성 작업 (2026-05-09)

- **PROGRESS.md 전면 재작성**: Phase 1~4(15개 스킬) → Phase 1~6(22개 스킬) 반영. 다국어 업그레이드(Phase 5), 확장 계층(Phase 6: A~F), 디렉토리 구조(22개), 스킬 현황 요약 표(코어 18개·확장 4개) 신규 추가. "다음 작업" 섹션을 "전체 완료. 총 22개 스킬 구현."으로 갱신.
- **`skills/geo-report-pdf/SKILL.md` 정합성 수정**: 개선 로드맵 Sprint 1/2/3 → 1주차/2주차/3~4주차/이후 구조로 교체 (geo-report와 통일). 재분석 일정 시점 명칭 병기.
- **`skills/geo-proposal/SKILL.md` 정합성 수정**: Sprint 분류 기준표에 심각도(CRITICAL+HIGH / MEDIUM / LOW) 열 추가. 재분석 일정에 주차 정보 병기.

## 현재 상태 (2026-05-09 기준)

**전체 완료. 22개 스킬, 모든 문서 최신 상태.**
- 코어 계층 18개 (Claude 웹·Code 모두 호환)
- 확장 계층 4개 (Claude Code 전용: geo-realtime·geo-tracker·geo-batch·geo-code)
- README.md / GUIDE.md / PROGRESS.md 전체 22개 스킬 반영 완료
- 모든 스킬 간 정합성 검증 완료
