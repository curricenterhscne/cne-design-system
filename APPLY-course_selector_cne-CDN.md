# course_selector_cne 적용 — Claude Code 프롬프트 묶음 (CDN 참조 방식)

꾸꾸클럽 디자인 시스템 v1.0을 **course_selector_cne**(학교별 시간표 시뮬레이션)에
점진 적용하기 위한 순서별 프롬프트입니다.

이 버전은 **별도 레포(cne-design-system) + CDN 참조** 방식입니다.
- 실제 사이트가 불러오는 CSS/캐릭터 = jsDelivr CDN 링크 (사본 중복 없음)
- Claude Code가 변수·클래스를 읽을 수 있도록 = 디자인 시스템 레포를 형제 폴더로 클론만 해둠

**위에서부터 차례대로**, 각 단계가 끝나고 확인한 뒤 다음 단계로. `<...>`만 채우면 됩니다.

> 핵심 원칙: 한 번에 다 바꾸지 않습니다. 토큰 → 확인 → 컴포넌트 → 확인 → bridge → 확인.
> 기존 기능(187개교 데이터, 834과목 courseDB.json, 6계열 프리셋, URL 공유, 그룹 충족 배지,
> bridge 연동)은 절대 깨지면 안 됩니다.

---

## 확정된 경로 (이 묶음에서 계속 사용)

```
디자인 시스템 레포:   https://github.com/curricenterhscne/cne-design-system
GitHub Pages:        https://curricenterhscne.github.io/cne-design-system/
CDN (jsDelivr):      https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/...
```

사이트 `<head>`에 넣을 링크 3줄:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/tokens/design-tokens.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/components/components.css">
```

캐릭터:
```html
<img src="https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/assets/characters/paenkkumi.svg" alt="팬꾸미" style="height:48px">
```

> `@main` = main 브랜치 최신. 안정화되면 버전 태그(예: `@v1.0`)로 고정 권장. 캐시가 깔끔하게 갱신됨.
> jsDelivr 캐시가 안 갱신되면 https://www.jsdelivr.com/tools/purge 에서 해당 URL을 purge.

---

## 0단계 — 준비 (Git Bash에서 직접, 프롬프트 아님)

디자인 시스템 레포를 course_selector_cne **옆에 클론**합니다 (복사·커밋 아님, 읽기용 참고).

```bash
cd /g/curricenterhscne
git clone https://github.com/curricenterhscne/cne-design-system.git
```

폴더 구조가 이렇게 됩니다:
```
/g/curricenterhscne/
├─ cne-design-system/      ← 방금 클론 (Claude Code가 읽을 참고용)
└─ course_selector_cne/    ← 실제 작업 레포 (여기서 claude 실행)
```

그다음 작업 레포로 이동해 Claude Code 실행:
```bash
cd /g/curricenterhscne/course_selector_cne
claude
```

---

## 1단계 — 디자인 시스템 파악 + 적용 계획 (코드 변경 없음)

> 가장 중요한 단계. Claude Code가 실제 파일을 자기 눈으로 확인하게 만들어, 추측을 막습니다.

```
이 레포(course_selector_cne)는 충남 고교학점제 가족 사이트 중 하나로, 학교별 시간표
시뮬레이션 웹앱이야. 꾸꾸클럽 디자인 시스템 v1.0을 점진 적용하려고 해.

디자인 시스템은 별도 레포로 운영하고, 실제로는 CDN으로 참조할 거야. 단, 너가 변수명과
클래스명을 정확히 알 수 있도록 디자인 시스템 레포를 이 레포 바로 옆(../cne-design-system)에
클론해뒀어.

작업을 시작하기 전에, 코드는 아직 하나도 바꾸지 말고 파악만 해줘:

1. ../cne-design-system/README.md, DESIGN-GUIDE.md 를 읽어.
2. ../cne-design-system/tokens/design-tokens.css 의 CSS 변수(--color-*, --text-*, --space-* 등)와
   ../cne-design-system/components/components.css 의 클래스(kk-*)를 목록으로 파악해.
3. ../cne-design-system/assets/characters/ 의 캐릭터 SVG 4종(paenkkumi, tokkumi, kkumi,
   kkukkuk-club-logo)을 확인해.
4. 이 레포(course_selector_cne)의 현재 구조를 훑어봐. 특히:
   - 메인 HTML/CSS 진입점과 현재 색·서체 정의 위치
   - courseDB.json (834과목 마스터)와 187개교+학과 분기 데이터의 위치/형식
   - 6개 계열 프리셋, URL 공유, 그룹 충족 배지 관련 코드
   - bridge.js (selector용) 와 bridge.css 의 위치/역할

그런 다음, 디자인 시스템을 이 레포에 어떻게 점진 적용할지 단계별 계획을 세워줘.
참조는 CDN 링크로 할 거야:
  https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/tokens/design-tokens.css
  https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/components/components.css
어떤 파일부터 손댈지, 기존 기능을 안 깨려면 뭘 조심해야 할지 포함해서.
계획만 보여주고 멈춰. 내 확인을 받은 뒤에 실제 작업을 시작하자.
```

---

## 2단계 — 디자인 토큰 적용 (색·서체 통일)

> 1단계 계획을 확인한 뒤 진행. 컴포넌트 교체는 아직 안 합니다.

```
좋아, 계획대로 시작하자. 이번엔 디자인 토큰만 적용해:

1. 메인 진입점 <head>에 아래 3줄을 가장 먼저 로드되도록 추가해:
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/tokens/design-tokens.css">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/components/components.css">
   (변수·클래스 정의는 옆 폴더 ../cne-design-system 에서 확인하되, 실제 link는 CDN URL로.)
2. 기존 색·서체·간격 정의를 디자인 토큰으로 치환해:
   - 기존 적색/베이지 톤은 폐기.
   - 배경은 --color-bg (라이트블루), 강조·헤더·버튼은 --color-brand (진블루),
     '권장/행운/성공' 의미는 --color-accent (그린).
   - 본문 폰트는 --font-sans (Pretendard), 위계는 --text-* 사용.
3. 원시 색(--kkuk-blue-500)은 직접 쓰지 말고 의미 토큰(--color-*)을 우선 사용해.

중요: 이번 단계에서는 컴포넌트 마크업/클래스는 바꾸지 마. 색·서체·간격만 토큰으로 치환해서,
토큰만으로도 전체가 꾸꾸클럽 가족 톤으로 보이는지 먼저 확인하자.
기존 기능(187개교 데이터, 프리셋, URL 공유, 그룹 충족 배지)은 절대 건드리지 말고,
변경은 작은 diff로 유지해. 끝나면 멈추고, 어떤 파일을 어떻게 바꿨는지 요약해줘.
```

다 되면 로컬에서 미리보기로 확인. (또는: `로컬에서 어떻게 미리보기 하면 되는지 알려줘`)

---

## 3단계 — 컴포넌트를 kk- 클래스로 교체 (화면 단위)

> 한 번에 한 영역만. 아래는 예시로 "과목 편제표 카드". 영역명만 바꿔 반복하세요.

```
토큰 적용은 끝났어. 이제 컴포넌트를 kk- 클래스로 교체하자. 이번엔 <과목 편제표 카드> 영역만.
클래스 정의는 ../cne-design-system/components/components.css 에서 확인해.

- 카드 컨테이너는 .kk-card, 과목 카드는 .kk-card--course
- 버튼은 .kk-btn--primary / .kk-btn--secondary (크기 --sm/--lg)
- 입력/검색은 .kk-field .kk-input .kk-searchbar
- 표가 있으면 .kk-table (.kk-table-wrap 으로 감싸고, 숫자 셀 .num, 강조 .num--emph)

원래 마크업 구조와 데이터 바인딩(JS 로직, 이벤트, courseDB 연결)은 그대로 두고,
클래스와 스타일만 교체해. 한 영역 끝나면 멈추고 확인하자.
```

반복할 영역 예시: 학교/학과 선택 UI · 편제표 · 사이드바(미개설 안내) · 계열 프리셋 버튼 ·
URL 공유 버튼 · 결과 없음(빈 상태).

---

## 4단계 — ★권장/◆핵심 표시를 배지로 통일 (bridge 연동)

```
majors → selector bridge 연동에서 넘어오는 ★(권장)·◆(핵심) 표시를 디자인 시스템 배지로
통일해줘. bridge.js 가 URL 파라미터(want, core, from, majorId)를 받아 편제표에 표시하는
로직은 그대로 두고, 표시 UI만 배지 클래스로 바꿔:

- core (진로선택) → .kk-badge--core  (◆)
- want (일반선택 + 융합선택) → .kk-badge--recommend  (★, 그린)
- 미개설 과목 사이드바 안내 → .kk-badge--online + 안내 문구

분류 규칙(core=진로선택만 / want=일반+융합)과 ?want=...&core=...&from=majors&majorId=...
파라미터 처리는 절대 바꾸지 마. 표시 모양만 통일하는 거야.
```

---

## 5단계 — 빈 상태 / 캐릭터 (선택)

```
결과 없음·로딩·시작 화면에 꾸꾸클럽 캐릭터를 넣자. 캐릭터는 CDN URL의 SVG를 <img>로 써:
  https://cdn.jsdelivr.net/gh/curricenterhscne/cne-design-system@main/assets/characters/<이름>.svg

- 빈 상태는 .kk-empty 구조 + tokkumi.svg.
  카피는 토꾸미 톤으로 ("관심 학과를 고르면 토꾸미가 권장 과목으로 시간표를 짜드릴게요" 등).
- 헤더가 있으면 마스코트로 paenkkumi.svg.
캐릭터는 height 40px 이상으로, 어두운 배경 위엔 흰 카드 안에 넣어 윤곽선이 묻히지 않게 해.
```

---

## 매 단계 공통 주의 (필요하면 프롬프트에 덧붙이기)

- 디자인 시스템 레포(../cne-design-system)의 파일은 **수정하지 마**. 그건 별도 레포의 단일
  진실원이야. 색이 안 맞으면 이 레포(course_selector_cne) 쪽에서 의미 토큰 매핑을 조정하거나,
  정말 필요한 신규 토큰은 나에게 알려줘 (디자인 시스템 레포는 내가 따로 갱신할게).
- 원시 색(--kkuk-blue-500) 직접 사용 금지, 의미 토큰(--color-*) 우선.
- 그린 액센트는 '권장/행운/성공' 의미일 때만. 남용 금지.
- 캐릭터는 CDN의 SVG를 `<img>` 로 사용 (옛 `<use href="#...">` 방식 아님).
- 변경은 작은 diff로, 한 화면/영역 단위로 확인하며 진행.
- 작업 중 기존 기능이 깨지면 즉시 멈추고 알려줘.

---

## 디자인 시스템을 수정해야 할 때 (별도 레포 운영의 핵심)

토큰이나 컴포넌트를 고쳐야 하면 **course_selector_cne가 아니라 cne-design-system 레포에서**
수정 → 커밋 → 푸시합니다. 그러면 CDN(@main)이 갱신되어 모든 사이트에 한 번에 반영됩니다.

```bash
cd /g/curricenterhscne/cne-design-system
# 파일 수정 후
git add . && git commit -m "토큰 조정: ..." && git push
# jsDelivr 캐시 즉시 갱신이 필요하면 https://www.jsdelivr.com/tools/purge 에서 URL purge
```

안정화되면 버전 태그를 찍고(`git tag v1.0 && git push --tags`), 각 사이트의 CDN 링크를
`@main` → `@v1.0` 으로 바꿔 고정하면 의도치 않은 변경이 사이트에 새지 않습니다.

2022-curriculum-majors 에도 0단계(클론)부터 같은 순서를 그대로 반복하면 됩니다.
다만 majors 쪽 bridge(majors용)는 selector로 보내는 URL을 만드는 쪽이라, 4단계가
"학과 상세에 ★권장/◆핵심 미리보기 + 시간표 짜기 버튼" 형태로 달라집니다.
```
