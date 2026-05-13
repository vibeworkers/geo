# 언어별 AI 플랫폼·봇 매핑표

작성일: 2026-05-09
용도: `geo-crawlers`, `geo-lang-platform`, `geo-platform-optimizer` 스킬 작성 기준 문서

근거 기준: 이 문서는 실행 라우팅용 working map이다. 플랫폼·봇·제품 상태에 관한
핵심 주장은 `source-index.md`의 외부 근거를 따라야 하며, 출처가 없거나 변동성이
큰 항목은 `requires live verification`으로 취급한다.

근거 등급:
- `official`: 운영사/표준/공식 문서 기반
- `local-official`: 한국/중국/지역 기관 공식 문서 기반
- `secondary-local`: 지역 시장 보도 또는 해설 기반
- `heuristic`: 문서화된 원리에서 도출한 실무 추론
- `requires live verification`: 릴리스 또는 고객 보고 전 최신 확인 필요

---

## 1. 전체 봇 목록 (robots.txt 허용 대상)

### 1-1. 글로벌 AI 봇

| 봇 이름 | User-agent | 운영사 | 서비스 | 용도 | 허용 전략 |
|---|---|---|---|---|---|
| GPTBot | `GPTBot` | OpenAI | ChatGPT | 학습 | 전략 A·G |
| OAI-SearchBot | `OAI-SearchBot` | OpenAI | ChatGPT Search | 검색 | 전략 A·B·G |
| ChatGPT-User | `ChatGPT-User` | OpenAI | ChatGPT 사용자 요청 | 사용자 트리거 | 전략 A·B·G |
| ClaudeBot | `ClaudeBot` | Anthropic | Claude | 학습 | 전략 A·G |
| anthropic-ai | `anthropic-ai` | Anthropic | Claude 데이터 수집 | 학습 | 전략 A·G |
| Google-Extended | `Google-Extended` | Google | Google AI data-use control | 학습 제어 | 전략 A·B·G |
| PerplexityBot | `PerplexityBot` | Perplexity | Perplexity AI | 검색 | 전략 A·B·G |
| Bingbot | `Bingbot` | Microsoft | Bing/Copilot search surface | 검색 | 전략 A·B·G |
| GrokBot | `GrokBot` | xAI | Grok | 학습 | 전략 A·G |
| xAI-Grok | `xAI-Grok` | xAI | Grok 실시간 검색 | 검색 | 전략 A·B·G |
| Grok-DeepSearch | `Grok-DeepSearch` | xAI | Grok 심층 검색 | 검색 | 전략 A·B·G |
| AppleBot | `Applebot` | Apple | Spotlight·Siri·Safari | 검색/렌더링 | 전략 A·G |
| Applebot-Extended | `Applebot-Extended` | Apple | Apple foundation models | 학습 제어 | 전략 A·B·G |
| Meta-ExternalAgent | `Meta-ExternalAgent` | Meta | Meta AI | 학습 | 전략 A·G |

근거: OpenAI, Anthropic, Perplexity, Google, Apple은 `source-index.md`의 공식 문서
행을 우선한다. xAI/Grok 및 Meta AI crawler 명칭은 공식 문서 확인 전
`requires live verification`이다.

### 1-2. 한국 시장 봇

| 봇 이름 | User-agent | 운영사 | 서비스 | 용도 | 허용 전략 |
|---|---|---|---|---|---|
| Yeti | `Yeti` | NAVER | AI 브리핑·AI 탭·일반 검색 | 검색+학습 | 전략 D·G |
| NaverBot | `NaverBot` | NAVER | 네이버 검색 | 검색 | 전략 D·G |

> **주의:** NAVER 검색로봇 `Yeti` 관련 권고는 네이버 서치어드바이저 공식 문서를
> 근거로 한다. 클로바X 종료 및 AI 탭 재편은 지역 시장/제품 상태 claim이므로
> 릴리스 전 NAVER 공식 공지 또는 dated local-market source로 재확인한다.

### 1-3. 일본 시장 봇

| 봇 이름 | User-agent | 운영사 | 서비스 | 용도 | 허용 전략 |
|---|---|---|---|---|---|
| YahooSeeker | `YahooSeeker` | Yahoo Japan | Yahoo! Japan AI 검색 | 검색 | 전략 E·G |

### 1-4. 중국 시장 봇

| 봇 이름 | User-agent | 운영사 | 서비스 | 용도 | 허용 전략 |
|---|---|---|---|---|---|
| Baiduspider | `Baiduspider` | Baidu | Baidu Ernie·일반 검색 | 검색+학습 | 전략 F·G |
| Baiduspider-render | `Baiduspider-render` | Baidu | 바이두 렌더링 봇 | 검색 | 전략 F·G |
| SogouBot | `Sogou web spider` | Sogou | Sogou AI | 검색 | 전략 F·G |
| 360Spider | `360Spider` | 360 | 360 AI | 검색 | 전략 F·G |

### 1-5. 기타 글로벌 봇

| 봇 이름 | User-agent | 운영사 | 서비스 | 용도 | 허용 전략 |
|---|---|---|---|---|---|
| ia_archiver | `ia_archiver` | Internet Archive | AI 학습 데이터 소스 | 학습 | 전략 A·G (선택적) |

---

## 2. 허용 전략 정의

| 전략 | 명칭 | 허용 봇 | 차단 봇 | 적합 상황 |
|---|---|---|---|---|
| **A** | 글로벌 전체 허용 | 글로벌 AI 봇 전체 | — | 영어 사이트 GEO 최대화 |
| **B** | 검색만 허용 (학습 차단) | 검색용 봇만 | GPTBot·ClaudeBot·anthropic-ai·GrokBot·AppleBot | 콘텐츠 저작권 보호 우선 |
| **C** | 선택적 허용 | 특정 서비스만 | 나머지 | 특정 AI 파트너십 |
| **D** | 한국 시장 추가 | 전략 A + Yeti·NaverBot | — | 한국어 사이트 네이버 AI 브리핑 최적화 |
| **E** | 일본 시장 추가 | 전략 A + YahooSeeker | — | 일본어 사이트 Yahoo! Japan AI 최적화 |
| **F** | 중국 시장 추가 | 전략 A + Baiduspider·SogouBot·360Spider | — | 중국어 사이트 바이두 AI 최적화 |
| **G** | 글로벌 전체 허용 | 전략 A + D + E + F | — | 다국어 사이트 전체 AI 가시성 최대화 |

---

## 3. 언어별 AI 플랫폼 매핑

### 3-1. 한국어 (ko)

| 플랫폼 | 운영사 | 유형 | 봇 | 최적화 핵심 | 비고 |
|---|---|---|---|---|---|
| 네이버 AI 브리핑 | NAVER | 검색 내 AI 요약 | Yeti·NaverBot | C-rank + D.I.A. + FAQ 구조 | local-official + requires live verification |
| 네이버 AI 탭 | NAVER | 대화형 에이전틱 검색 | Yeti·NaverBot | AI 브리핑 최적화 기반 + FAQPage 스키마 | secondary-local + requires live verification |
| ChatGPT | OpenAI | 대화형 AI | GPTBot·OAI-SearchBot | GPTBot 허용 + 콘텐츠 깊이 | 한국 점유율 높음 |
| Gemini | Google | 검색 통합 AI | Google-Extended | E-E-A-T + Google Search 최적화 | Google AI Overviews 연동 |

> **제거 후보:** 클로바X — 2026년 4월 9일 종료 보도 존재. 고객 보고서나 릴리스
> 문서에서는 NAVER 공식 공지 또는 최신 dated source 확인 후 확정 표현을 사용한다.

**한국 시장 특화 최적화 포인트:**
- robots.txt에 `Yeti`, `NaverBot` Allow 명시
- Naver Search Advisor 등록 및 sitemap 제출
- C-rank 향상: 네이버 블로그·포스트·지식iN 채널 콘텐츠 운영
- D.I.A. 구조: 첫 문단에 직접 답변, H3 질문 형식 FAQ, 목록·표·단계별 가이드
- 작성일·수정일 명시 (신선도 신호)

---

### 3-2. 영어 (en)

| 플랫폼 | 운영사 | 유형 | 봇 | 최적화 핵심 |
|---|---|---|---|---|
| ChatGPT | OpenAI | 대화형 AI + 브라우징 | GPTBot·OAI-SearchBot·ChatGPT-User | GPTBot 허용, 콘텐츠 깊이, 외부 링크 |
| Perplexity AI | Perplexity | 실시간 검색 AI | PerplexityBot | 직접 답변 구조, 출처 명확성 |
| Google Gemini / AI Overviews | Google | 검색 통합 AI | Google-Extended | E-E-A-T, FAQPage 스키마, Core Web Vitals |
| Microsoft Copilot | Microsoft | Bing 기반 AI | Bingbot | Bing Webmaster Tools 등록, Bingbot 허용 |
| Grok | xAI | 대화형 AI + 검색 | GrokBot·xAI-Grok·Grok-DeepSearch | X(Twitter) 계정 연결, 실시간 콘텐츠 |
| Apple Intelligence | Apple | 디바이스 AI + Siri | Applebot | Applebot 허용, 구조화 데이터 |
| Meta AI | Meta | 소셜 통합 AI | Meta-ExternalAgent | Facebook·Instagram 채널 연계 |

**영어 시장 특화 최적화 포인트:**
- Wikipedia 등재 또는 언급
- Reddit·Quora 브랜드 언급 확보
- 외부 권위 사이트 백링크
- E-E-A-T 저자 바이라인·자격증명 명시

---

### 3-3. 일본어 (ja)

| 플랫폼 | 운영사 | 유형 | 봇 | 최적화 핵심 |
|---|---|---|---|---|
| ChatGPT | OpenAI | 대화형 AI | GPTBot·OAI-SearchBot | 일본어 FAQ 구조, GPTBot 허용 |
| Yahoo! Japan AI | Yahoo Japan (LY Corp.) | 검색 통합 AI | YahooSeeker | Yahoo! Japan Search Console 등록 |
| Perplexity AI | Perplexity | 실시간 검색 AI | PerplexityBot | 일본어 직접 답변 구조 |
| Google Gemini | Google | 검색 통합 AI | Google-Extended | Google Japan 검색 최적화 |

**일본 시장 특화 최적화 포인트:**
- Yahoo! Japan Search Console 등록 및 sitemap 제출
- YahooSeeker Allow 명시 (robots.txt)
- 일본어 날짜 형식: `2026年5月9日`
- 일본어 FAQ 구조 (H3 질문 + 답변)
- Yahoo! Japan 디렉토리 등록 검토

---

### 3-4. 중국어 (zh)

| 플랫폼 | 운영사 | 유형 | 봇 | 최적화 핵심 |
|---|---|---|---|---|
| Baidu Ernie (文心一言) | Baidu | 검색 통합 AI | Baiduspider·Baiduspider-render | 바이두 검색 최적화, ICP 번호 필수 |
| Kimi AI | MoonShot | 대화형 AI | 전용 봇 미확인 | 콘텐츠 깊이, 출처 명확성 |
| Qwen (通义千问) | Alibaba | 대화형 AI | 전용 봇 미확인 | Alibaba 생태계 연계 |
| DeepSeek | DeepSeek | 대화형 AI | 전용 봇 미확인 | 오픈소스 기반, 학술·기술 콘텐츠 강세 |
| 360 AI | 360 | 검색 통합 AI | 360Spider | 360Spider Allow, 중국어 스키마 |
| Sogou AI | Sogou (Tencent) | 검색 통합 AI | Sogou web spider | SogouBot Allow |

**중국 시장 특별 고려사항:**
- ICP 번호(互联网内容提供商) 없으면 중국 내 AI 플랫폼 인덱싱 불가
- 바이두 검색자원플랫폼(搜索资源平台) 등록 필수
- CDN: 중국 내 서버 또는 중국 CDN 노드 필요 (글로벌 CDN 차단 가능)
- Great Firewall 접근 가능 여부 외부 도구로 사전 확인
- zh-CN(간체) vs zh-TW(번체) hreflang 분리 필수
- robots.txt: Baiduspider·SogouBot·360Spider 허용 별도 명시

---

### 3-5. 스페인어 (es)

| 플랫폼 | 운영사 | 유형 | 봇 | 최적화 핵심 |
|---|---|---|---|---|
| ChatGPT | OpenAI | 대화형 AI | GPTBot·OAI-SearchBot | 스페인어 직접 답변 구조 |
| Perplexity AI | Perplexity | 실시간 검색 AI | PerplexityBot | 출처 명확성, 권위 신호 |
| Google Gemini / AI Overviews | Google | 검색 통합 AI | Google-Extended | E-E-A-T, 라틴아메리카 로컬 신호 |
| Microsoft Copilot | Microsoft | Bing 기반 AI | Bingbot | Bing Webmaster Tools 등록 |

**스페인어 시장 특화 최적화 포인트:**
- hreflang 지역 분리: `es-ES`(스페인) vs `es-MX`(멕시코) vs `es-AR`(아르헨티나) vs `es-CO`(콜롬비아)
- x-default는 `es-ES` 또는 `en` 중 주요 타겟 기준으로 설정
- 통화·단위 로컬라이즈: EUR(스페인) vs MXN(멕시코) vs USD(일부 중남미)
- 날짜 형식: `9 de mayo de 2026`

---

## 4. 다국어 사이트 봇 허용 전략 권장

| 사이트 유형 | 권장 전략 | robots.txt 허용 봇 수 |
|---|---|---|
| 영어 단일 사이트 | 전략 A | 13개 |
| 한국어 단일 사이트 | 전략 D | 15개 |
| 한·영 2개 언어 | 전략 A + D | 15개 |
| 한·영·일 3개 언어 | 전략 A + D + E | 16개 |
| 한·영·일·중 4개 언어 | 전략 A + D + E + F | 19개 |
| 전체 다국어 (5개 언어) | 전략 G | 19개 |
| 학습 봇 차단 원하는 경우 | 전략 B + 지역 전략 | 검색 봇만 |

---

## 5. 변경 이력

| 날짜 | 변경 내용 |
|---|---|
| 2026-05-09 | 최초 작성. 클로바X 제거, 네이버 AI 브리핑·AI 탭·OAI-SearchBot·Meta-ExternalAgent 추가 |
| 2026-05-13 | 외부 근거 계약 추가. 플랫폼 상태·봇 명칭 중 변동성 큰 항목을 `requires live verification`으로 격하 |
