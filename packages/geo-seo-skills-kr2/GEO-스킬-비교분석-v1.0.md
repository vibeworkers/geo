# GEO 스킬 비교 분석 보고서

작성일: 2026-05-09

---

## 비교 대상

| 구분 | 경로 | 명칭 |
|---|---|---|
| A | `00_tunnel/90_skills/geo/SKILL.md` | **Tunnel GEO** |
| B | `09_utils/geo-seo-skills-kr/` | **KR GEO** (오케스트레이터 + 15개 전문 스킬) |

---

## 0. 구조 개요

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| 파일 수 | 1개 (SKILL.md) | 16개 (오케스트레이터 + 15개 스킬) |
| 총 줄 수 | 312줄 | 약 5,700줄 |
| 언어 | 영문 기반 + 일부 한국어 | 한국어 전용 |
| 레벨 시스템 | 없음 | L1 / L2 / L3 3단계 |
| Tunnel 연동 | 있음 (sequence-status 자동 갱신) | 없음 (독립 라이브러리) |
| 에이전트 설계 | 5개 병렬 서브에이전트 참조 (파일 미존재) | 서브에이전트 없음, 순차 실행 |

> **중요 관찰:** Tunnel GEO는 `agents/geo-ai-visibility.md`, `agents/geo-platform-analysis.md` 등 5개 에이전트 파일과 `skills/geo-audit/` 등 하위 스킬을 참조하지만, 실제 `00_tunnel/90_skills/geo/` 디렉토리에는 SKILL.md 단 1개만 존재한다. 참조 파일들이 별도 위치에 있거나 미구현 상태다.

---

## 1. 분석 범위 (A. 범위 — 비중 20%)

### 공통 영역 (10개)

| 영역 | Tunnel GEO 명령어 | KR GEO 스킬 |
|---|---|---|
| 전체 감사 | `/geo audit` | `geo-audit` |
| 인용 가능성 | `/geo citability` | `geo-citability` |
| AI 크롤러 | `/geo crawlers` | `geo-crawlers` |
| llms.txt | `/geo llmstxt` | `geo-llmstxt` |
| 브랜드 언급 | `/geo brands` | `geo-brand-mentions` |
| 플랫폼 최적화 | `/geo platforms` | `geo-platform-optimizer` |
| 스키마 | `/geo schema` | `geo-schema` |
| 기술 SEO | `/geo technical` | `geo-technical` |
| 콘텐츠·E-E-A-T | `/geo content` | `geo-content` |
| 보고서 | `/geo report` + `/geo report-pdf` | `geo-report` + `geo-report-pdf` |

### 독자 영역

| 독자 기능 | Tunnel GEO | KR GEO |
|---|---|---|
| 60초 빠른 스냅샷 | `/geo quick` | — |
| 단일 페이지 심층 분석 | `/geo page` | — |
| AI 브랜드 Gap 추적 | — | `geo-brand` |
| 경쟁사 GEO 비교 | — | `geo-compare` |
| 잠재 고객 빠른 스캔 | — | `geo-prospect` |
| GEO 개선 제안서 | — | `geo-proposal` |

**범위 판정: KR GEO 우위**
- 공통 10개 영역은 동일하나 KR GEO가 4개 고부가 독자 스킬 보유
- Tunnel GEO의 `/geo quick`·`/geo page`는 운영 편의 명령어에 가까움

---

## 2. 분석 깊이 (B. 깊이 — 비중 25%)

### 공통 영역별 깊이 비교

#### geo-crawlers (AI 크롤러 접근)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| 추적 AI 봇 수 | 명시 없음 (에이전트에 위임) | **10개** (GPTBot·ChatGPT-User·ClaudeBot·anthropic-ai·Google-Extended·PerplexityBot·Bingbot·GrokBot·xAI-Grok·Grok-DeepSearch) |
| 봇 용도 구분 | 없음 | **학습용 / 검색용** 명시 |
| 허용 전략 | 없음 | **A(전체 허용) / B(검색만 허용) / C(선택적 허용)** 3가지 시나리오 + GEO 영향 설명 |
| 점수 공식 | 없음 | **4차원 가중 공식** (AI봇허용 35% + AI안내파일 25% + 기술접근성 25% + 크롤링효율 15%) |
| robots.txt 코드 예시 | 없음 | 전략별 완성 코드 (`User-agent: GPTBot` 등) |
| 검증 명령어 | 없음 | `curl -A "GPTBot" https://[도메인]/robots.txt` |

**판정: KR GEO 압도적 우위**

---

#### geo-citability (인용 가능성)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| 평가 차원 수 | 5개 (점수 공식 없음) | **4개** (차원당 25점, 합산 100점) |
| 점수 가중 공식 | 없음 | 직접답변구조 35% + 콘텐츠권위성 30% + 기술인용신호 20% + 브랜드명확성 15% |
| 실측 연동 | browser-citation 명시 | browser-citation 연계 명시 |
| 등급표 | 없음 | 5단계 (우수/양호/보통/미흡/위험) |

**판정: KR GEO 우위 (점수 공식 명시)**

---

#### geo-content (콘텐츠·E-E-A-T)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| 평가 차원 | 언급만 | **E-E-A-T 4차원** 각 25점 (경험·전문성·권위성·신뢰성) |
| 세부 신호 수 | 없음 | 차원당 5개 이상 구체적 확인 항목 |
| AI 생성 콘텐츠 탐지 | 없음 | 별도 평가 항목 포함 |
| 신선도 평가 | 없음 | 작성일·수정일·1년 이내 업데이트 여부 |

**판정: KR GEO 압도적 우위**

---

#### geo-schema (스키마)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| GEO 영향도별 스키마 우선순위표 | 없음 | **10개 타입** (Organization·Article·FAQPage·speakable·HowTo·BreadcrumbList·Person·WebPage·LocalBusiness·Product) + GEO 영향도(높음/보통/낮음/조건부) |
| JSON-LD 추출 스크립트 | 없음 | Python 코드 포함 |
| L1 차단 | 없음 | 있음 (개발 작업 안내 후 중단) |

**판정: KR GEO 우위**

---

#### geo-audit (전체 감사 오케스트레이션)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| 실행 방식 | 5개 병렬 서브에이전트 (파일 미존재) | 5개 영역 순차 실행 (서브스킬 로드) |
| 비즈니스 유형 감지 | 6개 유형 (SaaS·Local·E-commerce·Publisher·Agency·Other) | 6개 유형 (동일) |
| 종합 점수 공식 | 6개 카테고리 가중 합산 | **동일한 6개 카테고리** 가중 합산 |
| 레벨별 보고서 | 없음 | L1(비즈니스 언어) / L2(FTP 수정 안내) / L3(코드 명세) 3종 출력 템플릿 |

**판정: KR GEO 우위 (L1/L2/L3 분기 + 서브스킬 실제 구현)**

---

**깊이 종합 판정: KR GEO 압도적 우위**

---

## 3. 정량화 체계 (C. 정량화 — 비중 20%)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| 종합 GEO 점수 공식 | 있음 (6개 카테고리 가중치) | 있음 (동일) |
| 서브스킬별 점수 공식 | **없음** | **있음** (citability·crawlers·content 각각 4차원 가중 공식) |
| 차원별 배점 | 없음 | 있음 (차원당 25점, 명시적 합산) |
| 등급 기준 (5단계) | 없음 | 있음 (80-100 우수 / 60-79 양호 / 40-59 보통 / 20-39 미흡 / 0-19 위험) |
| geo-brand 5가지 지표 | 없음 | 포지셔닝반영률·SOV·BCI·채널인용률·맥락일치율 (각 0~100점) |
| geo-compare 이중 점수 | 없음 | 사이트 설정 30점 + 페이지 콘텐츠 30점 (성격 달라 비합산) |

**판정: KR GEO 압도적 우위**

---

## 4. 실행 가능성 (D. 실행 가능성 — 비중 15%)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| 사용자별 액션 아이템 | 없음 (단일 출력) | **L1: 담당자 요청 문구 / L2: FTP·CMS 수정 단계 / L3: 코드 스니펫** |
| robots.txt 수정 코드 | 없음 | 전략 A·B 완성 코드 제공 |
| llms.txt 생성 템플릿 | 없음 | 완성 템플릿 + 배포 방법 + 검증 curl 명령어 |
| WordPress 수정 안내 | 없음 | Yoast SEO 경로 안내 포함 |
| 소요 시간 예측 | 없음 | 각 작업별 예상 시간 (예: robots.txt 5분, llms.txt 10분) |
| 우선순위 매트릭스 | 있음 (Critical/High/Medium/Low) | 있음 (즉시/단기/중장기 분류) |

**판정: KR GEO 압도적 우위**

---

## 5. 도구 연계 (E. 도구 연계 — 비중 10%)

| 항목 | Tunnel GEO | KR GEO |
|---|---|---|
| browser-citation 연동 | 있음 (citability 2단계) | 있음 (citability + geo-brand) |
| Claude Code / 웹 환경 분기 | 없음 | **있음** (Bash vs WebFetch + httpstatus.io 외부 도구 안내) |
| Tunnel Framework 연동 | **있음** ($TUNNEL 경로·sequence-status·step 코드) | 없음 |
| Python 스크립트 | PDF 생성 (`generate_pdf_report.py`) | PDF 생성 (별도 스킬) |
| 외부 도구 안내 | 없음 | `httpstatus.io`, `pagespeed.web.dev` 명시 |

**판정: 동등 (각각 다른 강점 보유)**

---

## 6. 독자 기능 (F. 독자 기능 — 비중 10%)

### Tunnel GEO 전용

| 기능 | 설명 |
|---|---|
| `/geo quick` | 60초 GEO 가시성 스냅샷 — 빠른 사전 진단 |
| `/geo page` | 단일 페이지 심층 분석 — 특정 URL 집중 점검 |

### KR GEO 전용

| 기능 | 설명 |
|---|---|
| `geo-brand` | AI 브랜드 Gap 추적 — 원하는 포지셔닝 vs 실제 AI 인식 수치화, 4주 순환 추적 |
| `geo-compare` | 자사 vs 경쟁사 GEO 신호 항목별 비교, 격차 도출 |
| `geo-prospect` | 잠재 고객 빠른 스캔 — 영업 전 사이트 현황 30초 파악 |
| `geo-proposal` | GEO 개선 제안서 자동 생성 — 감사 결과 → 납품 문서 |

**판정: KR GEO 우위 (4개 독자 스킬, 비즈니스 가치 높음)**

---

## 7. Tunnel Framework 적용 적합도 (G. Tunnel 적합도 — 추가 차원)

### Tunnel GEO

| 항목 | 상태 |
|---|---|
| `$TUNNEL` 경로 변수 사용 | 있음 |
| sequence-status.md / CSV 갱신 | 있음 (06.1·06.2 step 코드) |
| Exit Signal 정의 (success / partial) | 있음 |
| 다음 Step 연결 | 있음 (step_7 콘텐츠 파이프라인) |
| 10_projects/{domain} 경로 규칙 | 있음 |
| 병렬 서브에이전트 | 설계 있음 (파일 미구현) |

**Tunnel GEO Tunnel 적합도: 매우 높음 — 이미 통합 완료**

### KR GEO

| 항목 | 상태 |
|---|---|
| Tunnel 경로·변수 | 없음 (독립 라이브러리) |
| sequence-status 갱신 | 없음 |
| Exit Signal | 없음 |
| Step 코드 | 없음 |
| 10_projects 경로 규칙 | 없음 |
| 통합 난이도 | **낮음** — 각 스킬 말미에 아래 3개 블록 추가만 하면 됨: ① `$TUNNEL` 기반 파일 저장 경로 ② sequence-status 갱신 코드 ③ Exit Signal 정의 |

**KR GEO Tunnel 적합도: 현재 낮음 → 통합 시 높음 (통합 시 Tunnel GEO 대체 가능)**

---

## 8. 종합 평가표

| 기준 | 비중 | Tunnel GEO | KR GEO | 우위 |
|---|---|---|---|---|
| A. 분석 범위 | 20% | 10개 영역 | 15개 영역 | **KR GEO** |
| B. 분석 깊이 | 25% | 개략적 지침 | 차원별 점수 공식 명시 | **KR GEO** |
| C. 정량화 체계 | 20% | 종합 공식만 | 전 스킬 점수 공식 | **KR GEO** |
| D. 실행 가능성 | 15% | 단일 출력 | L1/L2/L3 액션 분기 | **KR GEO** |
| E. 도구 연계 | 10% | Tunnel 통합 | 환경 분기 + 외부도구 | **동등** |
| F. 독자 기능 | 10% | quick·page | brand·compare·prospect·proposal | **KR GEO** |
| G. Tunnel 적합도 | — | 현재 통합 완료 | 현재 미통합 | **Tunnel GEO** (현재 기준) |

---

## 9. 최종 결론

### 분석 능력 종합: KR GEO 압도적 우위

Tunnel GEO는 단일 SKILL.md로 전체 GEO 분석 흐름을 설계했지만, 실제 분석 로직(점수 공식, 차원별 지침, 레벨별 출력)은 대부분 참조 에이전트 파일에 위임되어 있고 그 파일들이 존재하지 않는다. 실질적으로 실행 가능한 분석 내용은 KR GEO가 훨씬 더 풍부하다.

KR GEO는 15개 전문 스킬이 각각 독립적으로 완전 구현되어 있으며, 모든 스킬이 세부 점수 공식, 레벨별 출력 템플릿, 실행 코드를 포함한다.

### 목적별 사용 지침

| 상황 | 권장 선택 | 이유 |
|---|---|---|
| Tunnel Framework 내 GEO 실행 | Tunnel GEO | sequence-status 연동, step 코드 내장 |
| 정밀 분석·납품 보고서 필요 | **KR GEO** | 점수 공식·레벨별 출력·4개 독자 스킬 |
| L1 마케팅 담당자 대응 | **KR GEO** | 비즈니스 언어 출력 분기 |
| 경쟁사 비교·브랜드 Gap 추적 | **KR GEO** | geo-compare·geo-brand 전용 스킬 |
| 빠른 현황 파악 (60초) | Tunnel GEO | `/geo quick` 전용 명령어 |

---

## 10. 권장 액션

### 단기 (바로 가능)

KR GEO 스킬을 Tunnel Framework에 통합하면 두 시스템의 장점을 모두 확보할 수 있다.

**통합 방법 (스킬당 3개 블록 추가):**

```bash
# 1. 파일 저장 경로를 Tunnel 규칙으로 변경
TUNNEL="/Users/seomkt/Library/CloudStorage/GoogleDrive-seomkt.kr@gmail.com/내 드라이브/00_tunnel"
OUTPUT="$TUNNEL/10_projects/$DOMAIN/03_geo/"

# 2. sequence-status 갱신
python3 "$TUNNEL/10_projects/update-status.py" $DOMAIN 06.1 완료 "" "GEO-감사-보고서.md 생성"

# 3. Exit Signal
# success: GEO-감사-보고서.md 존재 시
# partial: 03_geo/ 폴더만 생성된 경우
```

### 중기

- KR GEO에 `/geo quick` 명령어(60초 스냅샷) 추가
- Tunnel GEO의 5개 에이전트 파일 구현 또는 삭제 (참조 파일 미존재 상태 해소)
