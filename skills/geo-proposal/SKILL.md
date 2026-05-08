---
name: geo-proposal
description: >
  GEO 분석 결과를 바탕으로 개선 제안서를 작성한다.
  현황 요약, 개선 범위, Sprint별 구현 로드맵, 예상 효과를
  클라이언트 또는 내부 팀에 제출할 수 있는 문서로 정리한다.
  GEO-*.md 분석 파일이 있으면 자동으로 수집하여 반영한다.
  L3(개발자) 전용 스킬.
  트리거: "제안서", "proposal", "개선 계획서".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-proposal — GEO 개선 제안서 작성

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정한다.
> `L1` 또는 `L2`로 판단되면 아래 안내 메시지를 출력하고 실행을 중단한다.
> `L3`로 판단되면 아래 단계를 순서대로 실행한다.
> 결과는 `GEO-제안서-[도메인]-[날짜].md`로 저장한다.

---

## L1 / L2 접근 안내 (L1·L2이면 이 메시지 출력 후 중단)

```
GEO 제안서는 분석 결과 파일을 종합하여 기술 구현 계획을 작성하는 작업입니다.

현재 레벨에서는 직접 실행이 어렵습니다.

선택 사항:
1. 이 작업을 다시 요청할 때 `L3 개발자 프로필로 진행해 주세요.`처럼 수신자 레벨을 직접 명시하세요.
2. 개발팀에 아래 내용을 전달하세요:

   "GEO 분석이 완료되었습니다. 분석 결과를 바탕으로
    Sprint별 구현 계획과 예상 효과를 포함한 제안서를 작성해 주세요."
```

---

## 실행 단계

### 0단계: 제안 범위와 완료 조건 잠금

제안서는 개선 작업을 약속하는 문서이므로 아래 참조를 먼저 적용한다.

- 플랫폼별 crawler/action 메커니즘:
  `../../references/platform-truth-registry.md`
- 측정 계획과 before/after capture:
  `../../references/measurement-capture-template.md`
- commerce/action readiness:
  `../../references/commerce-audit-worksheet.md`
- private/logged-in/connector/user-provided context:
  `../../references/private-surface-routing.md`
- regional/vertical/brand-maturity routing:
  `../../references/regional-situational-routing.md`
- robots, terms, privacy, regulated claims, brand claims, commerce eligibility:
  `../../references/policy-risk-gate.md`
- 제안서 metadata와 claim labels:
  `../../references/report-template-contract.md`

제안서의 Sprint 완료 기준은 readiness, heuristic, observed_answer,
observed_citation, referral_signal, conversion_signal 중 무엇을 목표로
하는지 명시해야 한다.

### 1단계: 분석 파일 수집

현재 디렉토리에서 기존 GEO 분석 결과 파일을 수집한다.

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import glob, os

patterns = ['GEO-*.md', 'geo-*.md']
files = []
for p in patterns:
    files.extend(glob.glob(p))

if not files:
    print('분석 파일 없음 — 전체 감사 결과 먼저 필요')
else:
    for f in sorted(files):
        size = os.path.getsize(f)
        print(f'  {f}  ({size} bytes)')
"
```

**Claude 웹 환경**

> 현재 대화에서 공유된 GEO 분석 결과나 전체 감사 결과를 참조한다.
> 분석 결과가 없는 경우 사용자에게 대상 URL의 전체 감사 결과를 먼저 준비하도록 안내한다.

**파일이 없는 경우:**

```
분석 결과 파일이 없습니다.

제안서 작성 전에 아래 분석을 먼저 준비하세요:

  https://[도메인] 전체 감사
  https://[도메인] 기술 SEO 검토      ← L3
  https://[도메인] 스키마 점검        ← L3
  https://[도메인] llms.txt 진단      ← L3

분석 완료 후 다시 이 제안서 workflow를 실행하세요.
```

---

### 2단계: 현황 점수 취합

수집한 분석 파일에서 각 영역 점수를 추출한다.

| 영역 | 참조 파일 | 점수 |
|---|---|---|
| GEO 종합 | GEO-감사-보고서.md | [X]/100 |
| 콘텐츠 | GEO-콘텐츠-분석.md | [X]/100 |
| 인용 가능성 | GEO-인용가능성-분석.md | [X]/100 |
| 크롤러 접근 | GEO-크롤러-분석.md | [X]/100 |
| 브랜드 언급 | GEO-브랜드언급-분석.md | [X]/100 |
| 플랫폼 최적화 | GEO-플랫폼-분석.md | [X]/100 |
| 기술 SEO | GEO-기술SEO-분석.md | [X]/100 |

누락된 파일은 "미실행"으로 표시하고 제안서에 해당 분석 실행을 포함시킨다.

---

### 3단계: 개선 항목 분류

각 분석 파일의 Critical Issues와 구현 우선순위를 수집하여 3단계로 분류한다.

**분류 기준:**

| 단계 | 기준 | 예시 |
|---|---|---|
| Sprint 1 (즉시) | 난이도 낮음 + GEO 영향 높음 | llms.txt 생성, Organization 스키마 추가, robots.txt 수정 |
| Sprint 2 (단기) | 난이도 보통 + GEO 영향 높음 | FAQPage 스키마, speakable 설정, 콘텐츠 구조 개선 |
| Sprint 3 (중장기) | 난이도 높음 또는 외부 의존성 있음 | 언론 보도 확보, llms-full.txt 자동화, Core Web Vitals 개선 |

---

### 4단계: 공수 추정

각 작업 항목에 예상 공수를 산정한다.

**공수 기준표:**

| 작업 유형 | 예상 공수 |
|---|---|
| 텍스트 파일 생성·수정 (robots.txt, llms.txt) | 0.5~1시간 |
| JSON-LD 스키마 추가 (1개 타입) | 1~2시간 |
| CMS 플러그인 설정 (WordPress SEO 플러그인) | 1~2시간 |
| 콘텐츠 구조 개선 (FAQ 블록, 제목 재구성) | 2~4시간/페이지 |
| 페이지 성능 개선 (이미지 최적화, 캐시) | 4~8시간 |
| 외부 언급 확보 (언론, 디렉토리 등록) | 지속적 활동 |
| llms-full.txt 자동화 파이프라인 | 8~16시간 |

---

### 5단계: 제안서 출력

아래 템플릿에 따라 제안서를 작성하고 저장한다.

---

## 출력 템플릿 (L3 전용)

```markdown
# GEO 개선 제안서

**대상 사이트:** [도메인]
**작성일:** [날짜]
**작성자:** [담당자 또는 팀명]
**버전:** v1.0

---

## 1. 현황 요약

### GEO 점수 현황

| 영역 | 현재 점수 | 등급 | 비고 |
|---|---|---|---|
| GEO 종합 | [X]/100 | 우수·양호·보통·미흡·위험 | |
| 콘텐츠 품질 | [X]/100 | [등급] | |
| AI 인용 가능성 | [X]/100 | [등급] | |
| AI 크롤러 접근 | [X]/100 | [등급] | |
| 브랜드 언급 | [X]/100 | [등급] | |
| 플랫폼 최적화 | [X]/100 | [등급] | |
| 기술 SEO | [X]/100 | [등급] | |

### 핵심 문제 요약

1. **[Critical Issue 1]** — [영역]: [한 줄 설명]
2. **[Critical Issue 2]** — [영역]: [한 줄 설명]
3. **[Critical Issue 3]** — [영역]: [한 줄 설명]

---

## 2. 개선 범위

### 포함 항목

| 번호 | 작업 | 영역 | Sprint | 담당 | 예상 공수 |
|---|---|---|---|---|---|
| 1 | [작업 제목] | [영역] | S1 | [FE/BE/콘텐츠] | [X]h |
| 2 | [작업 제목] | [영역] | S1 | [담당] | [X]h |
| 3 | [작업 제목] | [영역] | S2 | [담당] | [X]h |
| 4 | [작업 제목] | [영역] | S2 | [담당] | [X]h |
| 5 | [작업 제목] | [영역] | S3 | [담당] | [X]h |
| | **합계** | | | | **[합계]h** |

### 미포함 항목 (별도 협의 필요)

- [항목]: [이유]
- [항목]: [이유]

---

## 3. Sprint별 구현 로드맵

### Sprint 1 — 즉시 적용 (1~2주)

**목표:** 난이도 낮고 효과 높은 항목 완료, GEO 점수 [예상 향상]점 개선

| 작업 | 상세 | 담당 | 완료 기준 |
|---|---|---|---|
| [작업] | [상세 설명] | [담당] | [검증 방법] |
| [작업] | [상세 설명] | [담당] | [검증 방법] |

**검증:**
```bash
# Sprint 1 완료 후 확인
curl -I https://[도메인]/llms.txt          # llms.txt 존재 확인
curl -s https://[도메인]/robots.txt        # robots.txt 수정 확인
# Google Rich Results Test로 스키마 확인
```

---

### Sprint 2 — 단기 개선 (3~4주)

**목표:** 콘텐츠·스키마 구조 강화, GEO 점수 추가 [예상 향상]점 개선

| 작업 | 상세 | 담당 | 완료 기준 |
|---|---|---|---|
| [작업] | [상세 설명] | [담당] | [검증 방법] |
| [작업] | [상세 설명] | [담당] | [검증 방법] |

---

### Sprint 3 — 중장기 강화 (1~3개월)

**목표:** 외부 권위 확보, 자동화 파이프라인 구축

| 작업 | 상세 | 담당 | 완료 기준 |
|---|---|---|---|
| [작업] | [상세 설명] | [담당] | [검증 방법] |
| [작업] | [상세 설명] | [담당] | [검증 방법] |

---

## 4. 예상 효과

### GEO 점수 개선 예상

| 단계 | 완료 후 예상 점수 | 주요 향상 영역 |
|---|---|---|
| Sprint 1 완료 | [현재+X]/100 | [영역 1], [영역 2] |
| Sprint 2 완료 | [현재+Y]/100 | [영역 3], [영역 4] |
| Sprint 3 완료 | [현재+Z]/100 | [영역 5], [영역 6] |

### AI 검색 노출 기대 효과

- **ChatGPT·Perplexity 인용 가능성:** [현재 수준] → Sprint 2 완료 후 [향상 수준]
- **Google AI Overviews 노출:** [현재 상태] → Sprint 1 완료 후 [향상 상태]
- **AI 크롤러 학습 데이터 포함:** Sprint 1 robots.txt 수정 완료 시 즉시 적용

---

## 5. 미실행 분석 항목

아래 분석은 제안서 작성 시점에 실행되지 않았습니다.
Sprint 진행 중 또는 완료 후 재분석을 권고합니다.

| 분석 | 요청 예시 | 권고 시점 |
|---|---|---|
| [미실행 분석명] | `https://[도메인] [필요한 분석 요청]` | Sprint [N] 완료 후 |

---

## 6. 재분석 일정

| 시점 | 요청 예시 | 목적 |
|---|---|---|
| Sprint 1 완료 후 | `https://[도메인] 전체 감사` | 즉시 개선 항목 효과 확인 |
| Sprint 2 완료 후 | `https://[도메인] 종합 보고서 생성` | 중간 성과 보고서 생성 |
| Sprint 3 완료 후 | `https://[도메인] 전체 감사` | 최종 GEO 점수 측정 |
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
