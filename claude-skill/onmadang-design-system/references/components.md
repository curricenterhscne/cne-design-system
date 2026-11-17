# 부품 예시 — `components.css` (v2.0)

클래스 이름은 v1과 같다. 아래 마크업은 `design-tokens.css` → `components.css` 순서로 불러온 상태를 전제로 한다.

## 머리글

```html
<header class="kk-header">
  <div class="kk-header__inner">
    <a class="kk-header__brand" href="./">
      <span class="kk-header__mascot"><img src=".../assets/characters/tokkumi.svg" alt=""></span>
      <span><span class="kk-header__title">온마당</span><span class="kk-header__subtitle">충남 고교학점제 종합지원</span></span>
    </a>
    <nav class="kk-header__nav" aria-label="주 메뉴">
      <a href="./about/">고교학점제</a>
      <a href="./design/" aria-current="page">진로·학업 설계</a>
    </nav>
  </div>
</header>
```
현재 위치는 `aria-current="page"`로 표시한다. 색만이 아니라 스크린 리더에도 전달된다.

## 단추

```html
<a class="kk-btn kk-btn--primary" href="...">사용 설명서 보기 →</a>      <!-- Button03 -->
<a class="kk-btn kk-btn--secondary" href="...">자세히 보기 →</a>          <!-- Button01 -->
<a class="kk-btn kk-btn--accent kk-btn--sm" href="...">검사하러 가기 →</a> <!-- Button04 -->
<button class="kk-btn kk-btn--primary" disabled>신청 기간이 아닙니다</button>
```
- 크기: `kk-btn--sm` / 기본 / `kk-btn--lg`
- 링크는 `<a>`, 동작은 `<button>`이다. 비활성 링크는 `aria-disabled="true"`를 붙이고 `href`를 지운다.

## 카드

```html
<article class="kk-card kk-card--hover">
  <p class="kk-card__eyebrow">의약보건계열 · 권장</p>
  <h3 class="kk-card__title">생명과학Ⅱ</h3>
  <p class="kk-card__body">생명 현상을 분자 수준에서 탐구하는 진로선택 과목입니다.</p>
  <div class="kk-card__footer">
    <span class="kk-badge kk-badge--recommend">★ 권장</span>
    <span class="kk-badge kk-badge--core">◆ 핵심</span>
    <span class="kk-badge kk-badge--online">온라인 개설</span>
  </div>
</article>
```
카드 전체가 링크면 `<a class="kk-card kk-card--hover">`로 감싼다. 포커스 테두리(3px)가 카드에 그려진다.

## 입력 칸

```html
<div class="kk-field">
  <label class="kk-label" for="q">학과명 검색 <span class="kk-label__hint">예: 간호학과</span></label>
  <div class="kk-searchbar">
    <input class="kk-input" id="q" type="search" placeholder="관심 학과를 입력하십시오">
    <button class="kk-btn kk-btn--primary">검색</button>
  </div>
</div>

<div class="kk-field kk-field--invalid">
  <label class="kk-label" for="no">학번</label>
  <input class="kk-input" id="no" aria-invalid="true" aria-describedby="no-err">
  <p class="kk-field__error" id="no-err">오류: 학번은 5자리 숫자입니다.</p>
</div>
```
오류 칸에는 `aria-invalid`와 `aria-describedby`를 함께 단다. 빨간 테두리만으로는 화면 읽기 프로그램에 전달되지 않는다.

## 배지

| 클래스 | 의미 | 예 |
|---|---|---|
| `kk-badge--recommend` | 권장(그린) | ★ 권장 |
| `kk-badge--core` | 핵심(브랜드) | ◆ 핵심 |
| `kk-badge--online` | 온라인 개설(라이트 블루) | 온라인 |
| `kk-badge--neutral` | 일반 | 일반선택 |
| `kk-badge--unit` | 학점·단위 | 4학점 |
| `kk-badge--warn` | 주의 | 순증 |
| `kk-badge--err` | 오류 | 미이수 |

## 표

```html
<div class="kk-table-wrap">
  <table class="kk-table">
    <caption class="sr-only">학교별 개설 현황</caption>
    <thead><tr><th scope="col">학교</th><th scope="col" class="num">개설 과목</th></tr></thead>
    <tbody><tr><td>천안고등학교</td><td class="num">42</td></tr></tbody>
  </table>
</div>
```
넓은 표는 `kk-table-wrap`이 가로 스크롤을 맡는다. 페이지 전체가 가로로 밀리지 않게 하려는 것이다.

## 빈 상태

```html
<div class="kk-empty">
  <img class="kk-empty__char" src=".../assets/characters/paenkkumi.svg" alt="">
  <h3 class="kk-empty__title">찾는 학과가 없습니다</h3>
  <p class="kk-empty__body">다른 낱말로 검색하거나 계열을 골라 보십시오.</p>
</div>
```
불러오는 중에는 `kk-empty--loading`을 붙이면 캐릭터가 흔들린다(「동작 줄이기」 설정이면 멈춤).

## 섹션 제목

```html
<div class="kk-section-title">
  <span class="kk-section-title__eyebrow">STEP 1</span>
  <h2 class="kk-section-title__heading">나에게 맞는 과목 찾기</h2>
</div>
```

## 관리자 화면

행정용 화면은 바깥 요소에 `class="surface-admin"`을 건다. 같은 색조에서 차분한 표면으로 바뀐다.
