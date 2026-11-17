# Claude 스킬 — onmadang-design-system

이 디자인 시스템(v2.0)을 Claude가 새 페이지·앱·아티팩트·문서에 적용할 때 쓰는 스킬이다.
「온마당 디자인으로」「고교학점제 사이트처럼」 같은 요청에서 저절로 불린다.

## 설치

**Claude Code (데스크탑·노트북 각각 한 번)**
```bash
git clone git@github-work:curricenterhscne/cne-design-system.git   # 이미 있으면 git pull
mkdir -p ~/.claude/skills
cp -R cne-design-system/claude-skill/onmadang-design-system ~/.claude/skills/
```
새 Claude Code 세션부터 적용된다.

**claude.ai (웹·앱)**
스킬 폴더를 zip으로 묶은 `onmadang-design-system.skill`을 설정의 기능(스킬) 화면에서 올린다.
```bash
cd cne-design-system/claude-skill && zip -qr -X onmadang-design-system.skill onmadang-design-system
```

## 갱신

DS 값을 바꾸면(v2.1 등) 이 스킬도 함께 고친다.
- `onmadang-design-system/assets/design-tokens.css` · `components.css` 사본을 새 파일로 바꾼다.
- `references/palette.md` 표와 SKILL.md의 CDN 태그(`@v2.0`)를 고친다.
- 그다음 위 설치 명령으로 각 컴퓨터에 다시 복사한다.
