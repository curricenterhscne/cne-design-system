# 적용 방법별 안내와 함정

## 1. Claude 아티팩트 · 외부 CSS를 못 불러오는 환경

아티팩트는 외부 스타일시트를 Google Fonts에서만 받는다. jsDelivr의 CSS는 막히므로 다음과 같이 한다.
- `assets/design-tokens.css`(필요하면 `assets/components.css`까지)를 읽어 `<style>` 안에 그대로 넣는다.
- 글꼴은 Pretendard를 받을 수 없으니 `font-family`에 `"Pretendard Variable", Pretendard, "Apple SD Gothic Neo", "Malgun Gothic", system-ui, sans-serif`를 그대로 두면 설치된 글꼴로 대체된다.
- 캐릭터 SVG는 `<img src="data:image/svg+xml;base64,...">`로 넣는다(외부 이미지도 막힌다).
- 아티팩트는 어두운 화면 모드도 고려해야 한다. 이 DS는 밝은 화면 전용이므로, 페이지 전체를 밝은 모드로 고정하고 `body`에 `--color-bg`를 명시한다.

## 2. 정적 HTML (빌드 도구 없음)

CDN 3줄(SKILL.md 「빠른 시작」)을 `<head>`에 넣는다. 토큰 → 컴포넌트 순서를 지킨다. 페이지 고유 스타일은 그 아래 `<style>`에 두어 덮어쓰게 한다.

## 3. React · Vue

- 진입점(`main.jsx`, `App.vue` 등)이나 `index.html`에서 토큰 CSS를 한 번만 불러온다.
- 컴포넌트 스타일은 `kk-` 클래스를 그대로 쓰거나, CSS Modules 안에서 `var(--color-brand)`처럼 토큰을 참조한다.
- npm 패키지는 없다. CDN 주소를 쓰거나 `assets/design-tokens.css`를 프로젝트에 복사한다. 복사했다면 맨 위 주석에 **어느 버전(v2.1, 커밋 d095eef)을 복사했는지** 적어 둔다.

## 4. Tailwind

토큰을 전역 CSS로 불러온 뒤 테마에서 CSS 변수를 가리킨다.

```js
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        brand: { DEFAULT: 'var(--color-brand)', hover: 'var(--color-brand-hover)', soft: 'var(--color-brand-soft)', text: 'var(--color-text-brand)' },
        bg: { DEFAULT: 'var(--color-bg)', subtle: 'var(--color-bg-subtle)' },
        ink: { DEFAULT: 'var(--color-text)', muted: 'var(--color-text-muted)', subtle: 'var(--color-text-subtle)' },
        line: 'var(--color-border)',
        accent: 'var(--color-accent)',
      },
      borderRadius: { btn: 'var(--radius-btn)', card: 'var(--radius-card)', input: 'var(--radius-input)' },
      boxShadow: { hover: 'var(--shadow-hover)' },
      fontFamily: { sans: ['Pretendard Variable', 'Pretendard', 'system-ui', 'sans-serif'] },
    },
  },
};
```

Tailwind v4는 `@theme { --color-brand: var(--color-brand); }` 꼴로 쓰고, 임의 값은 `bg-(--color-brand)`처럼 괄호로 쓴다(`bg-[--color-brand]`는 v4에서 동작하지 않는다).

## 5. 브리지 레이어 — 이미 자체 CSS가 있는 사이트

자체 변수 이름을 그대로 두고 값만 DS 토큰에 연결한다. 온마당의 학과 탐색·과목 선택 실습이 이 방식이다.

```css
:root {
  /* 자체 이름 → DS 토큰 */
  --bg: var(--color-bg);
  --panel: var(--color-surface);
  --ink: var(--color-text);
  --ink-2: var(--color-text-muted);
  --brand: var(--color-brand);
  --line: var(--color-border);
  --r: var(--radius-btn);
  --r-lg: var(--radius-card);
}
```
이렇게 하면 화면 코드는 한 줄도 고치지 않고 색과 모서리가 바뀐다. 그다음 화면 단위로 `kk-` 클래스로 바꿔 간다.

## 함정 — 온마당에서 실제로 겪은 것

1. **CSS 변수 안의 `url()`은 그 변수를 「쓰는」 CSS 파일 기준으로 풀린다.** 페이지에서 `--ic:url("../assets/img/a.svg")`를 정하고 공용 CSS(`assets/css/common.css`)가 `mask: var(--ic)`로 쓰면, 경로가 `assets/css/` 기준이 되어 `assets/assets/img`가 된다. 온마당 수강신청 입구 아이콘 4개가 이렇게 깨졌다. 변수를 쓰는 파일 기준으로 경로를 적거나, 변수를 쓰는 규칙을 같은 파일에 둔다.
2. **글꼴 전체판은 2MB다.** 반드시 `dynamic-subset`판을 쓴다(SKILL.md).
3. **비동기로 그리는 목록은 자리를 먼저 잡는다.** 스크립트가 틀을 그리기 전에 바깥 요소에 `min-height`를 주지 않으면 바닥글이 올라왔다가 밀려 CLS가 0.25까지 나온다. 안쪽 목록이 아니라 **바깥 틀**에 준다.
4. **공용 CSS가 요소 선택자에 스타일을 걸면 이식한 문서가 깨진다.** 예: `header{position:sticky}`면 본문 속 `<header>`가 화면 위에 붙는다. 이식할 때는 `<div>`로 바꾸거나 스타일을 감싸는 클래스 아래로 가둔다.
5. **`:has()` 같은 새 선택자를 다른 선택자와 쉼표로 묶지 않는다.** 모르는 브라우저에서는 그 규칙 전체가 무시된다.
6. **`hidden` 속성을 `display:flex`가 덮어쓴다.** 직접 만든 화면에는 `[hidden]{display:none!important}`를 넣는다.

## 버전을 올릴 때 (DS 관리자용)

1. `cne-design-system`에서 토큰 **값**만 바꾼다. 이름을 바꾸거나 지우면 쓰는 앱이 깨진다.
2. 새로 필요한 값은 새 토큰으로 더한다.
3. `CHANGELOG.md`에 바뀐 값과 근거를 적고 태그(`v2.1` 등)를 붙인다.
4. 쓰는 앱은 고정 해시를 올리기 전에 미리 보기로 확인한다.
