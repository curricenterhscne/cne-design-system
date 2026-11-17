# CHANGELOG — cne-design-system

## v2.0 — 2026-11-18

디자인 업체 최종 가이드(「충남교육청_온마당_디자인가이드.pdf」, 2026-11-17)를 반영했다.
**토큰 이름과 컴포넌트 클래스 이름은 v1과 같다.** 값만 바뀌었으므로 v1을 쓰던 앱은 고정 해시만 올리면 따라온다.

### 색

| 토큰 | v1 | v2 | 근거 |
|---|---|---|---|
| `--kkuk-blue-500` (`--color-brand`) | #4F6EBE | **#526ADC** | 가이드 브랜드 블루 (흰 글자 4.72) |
| `--kkuk-blue-600` (`--color-text-brand`) | #41599C | #3F54C4 | 글자용 — 흰 6.41 · 옅은 바탕 5.9 |
| `--kkuk-sky-200` (`--color-bg`) | #DAF2FC | **#D7F3FF** | 가이드 라이트 스카이 블루 |
| `--kkuk-green-300` (`--color-accent`) | #7BCE7C | **#78F8A3** | 가이드 라임그린 (흰 글자 금지) |
| `--kkuk-green-200` | #B6E3B7 | #A8FFC2 | 가이드 라이트 라임그린 |
| `--kkuk-cream-100` | #FFFFE7 | #FFFFC4 | 가이드 레몬 |
| `--kkuk-ink` (`--color-text`, `--color-heading`) | #221F20 / #1E2A45 | **#000000** | 가이드 텍스트(진하게) |
| `--kkuk-gray-700` (`--color-text-muted`) | #5B5B5C | #333333 | 가이드 텍스트(연하게) |
| `--color-text-subtle` | #8A8A8B | #6B6B6B | 4.5:1 확보. 가이드 #727272는 비활성 전용 `--color-text-disabled` |
| `--color-border` | rgba(79,110,190,.18) | #E2E4EE | 가이드 라인 |
| `--kkuk-danger` | #C9453C | #C41E22 | 오류 글자(흰 5.91). 가이드 오류 #FF2B2E는 테두리 전용 |
| `--kkuk-warning` | #D98A2B | #8A4500 | 경고 글자. 가이드 경고 #FFDDC8은 바탕 |
| `--color-focus-ring` | blue-400 · 2px | blue-500 · **3px** (`--focus-width`) | 가이드 키보드 포커스 stroke 3 |

**새로 생긴 토큰**
- 색: `--kkuk-purple-100/500/600`(퍼플 #8B5ED4), `--kkuk-cyan-100/400/700`(라이트 블루 #61DFFF), `--kkuk-pink-200`(#FFD5FF), `--kkuk-gray-600`, `--kkuk-error-line`, `--kkuk-warning-bg`
- 의미: `--color-brand-soft`(마우스오버 #D7F3FF), `--color-disabled`(#C8C8C8), `--color-current`(머리글 현재 위치 라임), `--color-text-disabled`, `--color-error-line`, `--color-warning-bg`

### 서체·모서리·그림자
- `--weight-extrabold: 800`. 가이드 PC/모바일 크기를 `clamp()`로 묶은 `--text-hero`(40→55), `--text-section`(25→40), `--text-lead`(15→25), `--text-card`(15→20).
- 반경 스케일 `--radius-sm/md/lg/xl` 6/10/16/24 → **8/12/20/30**. 새 토큰 `--radius-btn` 15, `--radius-card` 20, `--radius-input` 30.
- 새 토큰 `--shadow-hover: 0 4px 7px rgba(0,0,0,.3)` — 가이드 카드 마우스오버.

### 컴포넌트 (`components.css`)
- `.kk-header`: 브랜드 채움 막대 → **흰 바탕 + 알약 메뉴**(기본 브랜드 테두리 · 마우스오버 #D7F3FF · 현재 위치 브랜드 채움).
- `.kk-btn`: 모서리 15, 굵게, 포커스 3px, 비활성 #C8C8C8.
  - primary(Button03) — 마우스오버 #D7F3FF 바탕 + 브랜드 글자
  - secondary(Button01) — 흰 바탕 + 브랜드 테두리
  - accent(Button04) — 라이트 블루 바탕(검정 글자), 마우스오버 브랜드 + 흰 글자
- `.kk-card`: 모서리 20, 마우스오버 그림자 + 브랜드 테두리, 제목 ExtraBold `--text-card`.
- `.kk-input` · `.kk-select`: 모서리 30, 마우스오버·포커스 브랜드 3px(그림자로 덧대 칸이 흔들리지 않게). `.kk-field--invalid` 오류 2px #FF2B2E, 새 `.kk-field--warn`(#FFDDC8 바탕).
- `.kk-badge`: 권장 `green-100/600`, 온라인 `cyan-100/700`. 새 `.kk-badge--warn` · `.kk-badge--err`.
- 표 머리줄 바탕 sky-100, 관리자 표 머리줄의 raw 색을 토큰으로.

### 쓰는 곳
- 온마당 `design/majors/` · `design/selector/`(+`guide.html`) — 커밋 해시로 고정해 쓴다. 해시를 올려야 반영된다.
- 두 앱은 11월 리뉴얼 때 페이지 쪽에서 이미 v2 색을 덧입혀 두어 화면 변화는 작다(단추 모서리·글자색·선색).

## v1.0 — 2026-05-22

꾸꾸클럽 캐릭터 굿즈 자료집 기반 임시 스킨. 색·서체·간격·핵심 컴포넌트 5·배지·캐릭터 자산·빈 상태·관리자 표면.
