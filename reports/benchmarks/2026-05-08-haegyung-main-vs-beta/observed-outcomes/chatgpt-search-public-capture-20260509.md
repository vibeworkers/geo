# ChatGPT Search Public Capture - 2026-05-09

## Capture Metadata

| field | value |
| --- | --- |
| platform | `ChatGPT Search` |
| surface | `chatgpt.com public browser with model=search query parameter` |
| access_profile | `public signed-out (non-authenticated)` |
| captured_at | `2026-05-09T14:04:42Z` |
| region_language | `English UI; public session without account` |
| session | Firecrawl browser session `019e0d0d-0c18-706e-9410-708134b60311`, destroyed after capture |
| target | `Haegyung (해경)` at `https://haegyung.com` |

## Boundary

이 캡처는 `model=search` 쿼리 파라미터로 접근한 공개 세션에서 `chatgpt.com` 응답을 수집한 행이다.
실질적인 검색 모드 동작이 보장되었는지에 대한 인터페이스 표식은 남지 않았으나,
결과는 전부 `해양경찰` 방향으로 치우쳤고 `haegyung.com` 관측 target은 나타나지 않았다.

## Prompt Outcome Summary

| prompt_id | answer status | visible target URL | citation status | classification |
| --- | --- | --- | --- | --- |
| `P1` | wrong entity | `https://www.kcg.go.kr` | wrong entity source cited | `not_observed_target_answer_or_citation` |
| `P2` | wrong entity / wrong official-source answer | `https://www.kcg.go.kr/` | wrong entity source cited | `not_observed_target_answer_or_citation` |
| `P3` | source absent / not live browsing path | `https://www.kcg.go.kr` | wrong / non-target source cited | `not_observed_target_answer_or_citation` |

## P1

Prompt:

```text
Who is Haegyung (해경)? Give a concise summary and cite the official website if you can verify it.
```

Observed outcome:

- 답변은 `해경`을 한국어로는 Coast Guard 축약어로 해석하고 `https://www.kcg.go.kr`를 공식 사이트로 제시했다.
- `https://haegyung.com`은 응답, 인용, 근거 URL로 나타나지 않았다.

## P2

Prompt:

```text
Find the official website or official source for Haegyung (해경) and explain why you believe it is official.
```

Observed outcome:

- 답변은 한국 해양경찰청(해경) 쪽을 대상으로 설정하고 `https://www.kcg.go.kr/`와
  `.go.kr` 근거를 제시했다.
- `haegyung.com` 타겟 URL은 목표 응답·인용에 포함되지 않았다.

## P3

Prompt:

```text
Show me a source from Haegyung (해경)'s official website that describes its music, activities, or recent updates.
```

Observed outcome:

- `live browsing`이 불가능하다는 진술 뒤 Coast Guard/군악대 맥락의 안내로 응답했다.
- `https://www.kcg.go.kr`를 권고했고 타겟 `haegyung.com` 링크/인용은 보이지 않았다.

## Measurement Impact

`ChatGPT Search` 공개 캡처는 현재 상태에서 target-positive evidence를 만들지 못했고,
`haegyung.com`은 미확인으로 남는다. 현재 `Gemini / AI Overviews`와 마찬가지로
negative 측정으로 기록한다.
