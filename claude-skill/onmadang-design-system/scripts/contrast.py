#!/usr/bin/env python3
"""글자색·바탕색 대비 확인 (WCAG 2.x 상대 휘도).

사용:
  python3 contrast.py 526ADC D7F3FF          # 한 쌍
  python3 contrast.py 526ADC FFFFFF 000000   # 첫 색을 나머지 바탕들과 비교
본문 글자 4.5 이상, 큰 글자(18pt, 굵게 14pt 이상)는 3.0 이상이면 통과.
"""
import sys


def lum(hexcolor):
    h = hexcolor.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    rgb = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def main(args):
    if len(args) < 2:
        print(__doc__)
        return 1
    fg = args[0]
    for bg in args[1:]:
        r = ratio(fg, bg)
        verdict = '본문 통과' if r >= 4.5 else ('큰 글자만' if r >= 3.0 else '사용 불가')
        print(f'#{fg.lstrip("#").upper()} on #{bg.lstrip("#").upper()}: {r:.2f}:1  {verdict}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
