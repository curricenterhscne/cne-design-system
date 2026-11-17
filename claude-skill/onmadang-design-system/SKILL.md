---
name: onmadang-design-system
description: 충남교육청 고교학점제 포털 「온마당」 디자인 시스템(cne-design-system v2.0, 꾸꾸클럽 캐릭터)을 새 웹페이지·웹앱·Claude 아티팩트·React/Tailwind 프로젝트·슬라이드·문서에 적용할 때 쓴다. 「온마당 디자인으로」「온마당 스타일」「온마당이랑 같은 모양」「고교학점제 사이트처럼」「꾸꾸클럽 캐릭터 넣어서」「cne-design-system」「kk- 클래스」「디자인 토큰 v2」 같은 요청, 충남 고교학점제·공동교육과정·수강신청 관련 화면을 새로 만들거나 기존 화면을 온마당과 통일하려는 경우에는 이름을 말하지 않아도 반드시 이 스킬을 쓴다. 색값·모서리·단추 상태·대비 기준을 추측하지 말고 여기 값을 쓸 것.
---

# 온마당 디자인 시스템 v2.0 적용

온마당(onmadang.or.kr)과 그 가족 사이트가 한눈에 같은 가족으로 보이게 하는 디자인 시스템이다.
원본 저장소: `curricenterhscne/cne-design-system` (태그 `v2.0`, 커밋 `18b0232`, 2026-11-18).
값의 근거는 디자인 업체 최종 가이드(2026-11-17)이고, 글자로 쓰는 색은 모두 대비 4.5:1 이상으로 맞춰 두었다.

## 먼저 정할 것 — 어디에 적용하나

| 대상 | 방법 | 읽을 파일 |
|---|---|---|
| 정적 HTML 사이트·웹앱 (외부 CDN 허용) | CDN 3줄 연결 후 `kk-` 클래스와 `--color-*` 토큰 사용 | 아래 「빠른 시작」, `references/components.md` |
| Claude 아티팩트 · 외부 CSS를 못 불러오는 곳 | `assets/design-tokens.css`(+필요하면 `components.css`)를 `<style>` 안에 그대로 넣는다 | `references/components.md` |
| React · Vue · Tailwind 프로젝트 | 토큰 CSS를 전역으로 넣고, Tailwind면 `theme.extend`에 CSS 변수를 연결 | `references/frameworks.md` |
| 이미 자체 CSS가 있는 사이트 | 자체 변수를 DS 토큰에 연결하는 **브리지 레이어**로 점진 적용 | `references/frameworks.md` 「브리지」 |
| 슬라이드·문서·포스터·엑셀 등 웹이 아닌 것 | 색값·글꼴·크기 표만 가져다 쓴다 | `references/palette.md` |

## 빠른 시작 (정적 HTML)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@v2.0/tokens/design-tokens.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@v2.0/components/components.css">
```

- **글꼴은 `dynamic-subset` 판을 쓴다.** `pretendardvariable.min.css`(전체판)는 글꼴 파일이 2MB라, 온마당에서 측정했을 때 모바일 첫 화면이 12~13초 걸리고 글꼴이 바뀌며 화면이 밀렸다(CLS 0.2). subset판으로 바꾸자 페이지 무게가 1/3~1/4이 됐다.
- **CDN은 태그(`@v2.0`)나 커밋 해시로 고정한다.** `@main`은 디자인 시스템이 바뀌는 즉시 모든 사이트에 퍼진다. 고정해 두면 미리 확인한 뒤 해시만 올려 반영할 수 있다.

## 핵심 원칙 — 왜 이렇게 하나

1. **색·모서리·그림자는 토큰으로만 쓴다.** `#526ADC`를 직접 박지 말고 `var(--color-brand)`를 쓴다. 온마당은 디자인 업체가 「껍데기」를 바꿀 수 있게 만들어져 있어서, raw 값이 섞이면 다음 리뉴얼 때 그 자리만 옛 모습으로 남는다.
2. **의미 토큰(`--color-*`)을 먼저, 원색 램프(`--kkuk-*`)는 필요할 때만 쓴다.** 의미 토큰은 바뀌어도 이름이 유지된다. v1 → v2 때도 이름은 그대로 두고 값만 바꿔서, 쓰는 앱을 하나도 고치지 않았다.
3. **글자색 대비 4.5:1을 지킨다(KWCAG).** 가이드 색 중 글자로 쓰면 안 되는 것이 있다.
   - 라임그린 `#78F8A3`·라이트 블루 `#61DFFF` 위에는 **검정 글자만** 쓴다(흰 글자 1.33·1.55).
   - 오류색 `#FF2B2E`는 **테두리 전용**이다(흰 바탕 글자 3.73). 오류 문구는 `--kkuk-danger`(#C41E22)를 쓴다.
   - 옅은 바탕 위 작은 브랜드 글자는 `--color-text-brand`(#3F54C4)를 쓴다. `#526ADC`는 옅은 바탕에서 4.08~4.4라 미달이다.
   - 보조 글자는 `--color-text-subtle`(#6B6B6B)을 쓴다. 가이드의 #727272는 비활성 전용(`--color-text-disabled`)이다.
   - 새 색 조합을 만들면 `scripts/contrast.py`로 확인한다.
4. **상태는 색만으로 구분하지 않는다.** 권장·핵심·오류에는 늘 글자나 기호를 함께 쓴다(★권장, ◆핵심, 「오류:」).
5. **포커스는 3px 브랜드 테두리다.** 가이드의 키보드 포커스 규격이고, 마우스 사용자에게는 보이지 않도록 `:focus-visible`에 건다.

## 부품 규격 (가이드 상태표)

| 부품 | 모서리 | 기본 | 마우스오버 | 포커스 | 비활성 |
|---|---|---|---|---|---|
| 단추 `.kk-btn--primary` (Button03) | 15 `--radius-btn` | 브랜드 채움·흰 글자 | `#D7F3FF` 바탕 + 브랜드 글자 | 3px 브랜드 | `#C8C8C8` |
| 단추 `.kk-btn--secondary` (Button01) | 15 | 흰 바탕 + 브랜드 테두리 | `#D7F3FF` | 3px | `#C8C8C8` |
| 단추 `.kk-btn--accent` (Button04) | 15 | `#61DFFF` + 검정 글자 | 브랜드 + 흰 글자 | 3px | `#C8C8C8` |
| 카드 `.kk-card` | 20 `--radius-card` | 흰 바탕 | 그림자 `0 4px 7px rgba(0,0,0,.3)` + 브랜드 테두리 | 3px | — |
| 입력 칸 `.kk-input` | 30 `--radius-input` | 연한 브랜드 테두리 | 브랜드 3px | 브랜드 3px | — |
| 메뉴 `.kk-header__nav a` | 알약 | 브랜드 테두리 | `#D7F3FF` | 3px | 현재 위치: 브랜드 채움 |

- 입력 칸 오류는 `.kk-field--invalid`(2px `#FF2B2E`), 경고는 `.kk-field--warn`(`#FFDDC8` 바탕)이다.
- 배지·태그는 알약(`--radius-pill`)이고, 단추는 알약이 아니다. 가이드가 단추를 모서리 15로 정했다.

## 글자 (Pretendard Variable)

| 용도 | 토큰 | PC → 모바일 | 굵기 |
|---|---|---|---|
| 메인 대제목 | `--text-hero` | 55 → 40px | 800 |
| 섹션 제목 | `--text-section` | 40 → 25px | 800 |
| 섹션 내용 | `--text-lead` | 25 → 15px | 500 |
| 카드 제목 | `--text-card` | 20 → 15px | 800 |
| 본문 | `--text-body` | 16px | 400 |

한글 제목은 `word-break: keep-all`을 걸어야 낱말 중간에서 줄이 바뀌지 않는다.

## 캐릭터 (꾸꾸클럽)

`assets/`에 토꾸미(토끼, `tokkumi.svg`)·팬꾸미(판다, `paenkkumi.svg`)·꾸미(애벌레, `kkumi.svg`)·로고가 있다. CDN: `https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@v2.0/assets/characters/<파일>`.
- 캐릭터는 **장식**이다. `alt=""`와 `aria-hidden="true"`를 붙이거나, 의미가 있으면 이름을 `alt`로 쓴다.
- 작은 아이콘·판정 결과 자리에는 캐릭터 대신 단순한 아이콘을 쓴다. 캐릭터가 많으면 정보가 묻힌다.

## 온마당 본체(onmadang 저장소)에서 작업할 때

본체 페이지는 이 DS가 아니라 `assets/css/common.css`(같은 v2 값, 이름은 `--brand`·`--bg`·`--ink`…)를 쓴다. 본체에서는 **`var(--color-*)`가 없다.** 저장소의 `CLAUDE.md`를 먼저 읽고 그 토큰 이름을 쓴다. DS(`--color-*`, `kk-`)는 `design/majors/`·`design/selector/`와 새 앱에서 쓴다.

## 하지 말 것

- 글꼴 전체판(`pretendardvariable.min.css`) 연결 — 2MB
- CDN `@main` 연결 — 예고 없이 바뀐다
- 라임·라이트 블루 바탕에 흰 글자, `#FF2B2E` 글자
- 토큰 이름 바꾸기 — 쓰는 앱이 모두 깨진다. 값만 바꾼다
- 단추를 알약 모양으로 — 가이드는 모서리 15

## 참고 파일

- `references/palette.md` — 전체 색표(원색 램프·의미 토큰·대비값), 웹이 아닌 곳에 쓸 때
- `references/components.md` — 부품별 HTML 예시
- `references/frameworks.md` — React·Tailwind·브리지 레이어·아티팩트 적용법과 함정
- `assets/design-tokens.css` · `assets/components.css` — v2.0 원본 사본(인라인용)
- `scripts/contrast.py` — `python3 scripts/contrast.py 526ADC D7F3FF` → 대비값과 통과 여부
