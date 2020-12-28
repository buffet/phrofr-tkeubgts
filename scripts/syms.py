#!/usr/bin/env python3

"""
Symbols are all typed on the left side.
Right side then decides if theres a space on the left, right, both, or neither side of the symbol.
Heavily inspired by https://stenomod.blogspot.com/2020/03/a-pattern-for-stroking-symbols-with.html.

Star key is used to insert two of the symbol (without space between them).

Spaces:
| Outline | Left | Right |
|---------+------+-------|
| -RGBS   | Yes  | Yes   |
| -FPLT   | No   | No    |
| -RPLT   | Yes  | No    |
| -FPGS   | No   | Yes   |

Syms:
| Outline | Sym | Explanaition           |
|---------+-----+------------------------|
| TK      | .   | Dot                    |
| KR      | ,   | Comma                  |
| KPR     | ^   | shape                  |
| TP      | !   | used in TP-BG          |
| H       | ?   | used in H-F            |
| KPH     | /   | shape                  |
| K       | :   | Kolon                  |
| SK      | ;   | SemiKolon              |
| KW      | "   | Quote                  |
| KWHR    | =   | eQuaL                  |
| P       | %   | Percent                |
| PHR     | +   | PLus                   |
| PR      | (   | PaRen                  |
| SPR     | )   | cloSing PaRen          |
| PRA     | <   | shape (>)              |
| SPRA    | >   | closing <              |
| PW      | |   | shape                  |
| PWR     | [   | BRacket                |
| SPWR    | ]   | cloSing BRacket        |
| SKP     | &   | "and"                  |
| SKWR    | _   | shape                  |
| STRA    | *   | STAR                   |
| T       | '   | Tick                   |
| THR     | ~   | TilDe                  |
| TKHR    | $   | DoLLar                 |
| TKPW    | @   | shape                  |
| TPH     | #   | Number                 |
| TPR     | {   | FRench bracket         |
| STPR    | }   | cloSing FRench bracket |
| TW      | `   | shape                  |
| TWR     | \   | shape                  |
| WR      | -   | shape                  |
"""

from steno import build_stroke, write_dict


def build_dict():
    syms = [
        {
            'stroke': ['T-', 'K-'],
            'sym': '.',
        },
        {
            'stroke': ['K-', 'R-'],
            'sym': ',',
        },
        {
            'stroke': ['K-', 'P-', 'R-'],
            'sym': '^',
        },
        {
            'stroke': ['T-', 'P-'],
            'sym': '!',
        },
        {
            'stroke': ['H-'],
            'sym': '?',
        },
        {
            'stroke': ['K-', 'P-', 'H-'],
            'sym': '/',
        },
        {
            'stroke': ['K-'],
            'sym': ':',
        },
        {
            'stroke': ['S-', 'K-'],
            'sym': ';',
        },
        {
            'stroke': ['K-', 'W-'],
            'sym': '"',
        },
        {
            'stroke': ['K-', 'W-', 'H-', 'R-'],
            'sym': '=',
        },
        {
            'stroke': ['P-'],
            'sym': '%',
        },
        {
            'stroke': ['P-', 'H-', 'R-'],
            'sym': '+',
        },
        {
            'stroke': ['P-', 'R-'],
            'sym': '(',
        },
        {
            'stroke': ['S-', 'P-', 'R-'],
            'sym': ')',
        },
        {
            'stroke': ['P-', 'R-', 'A'],
            'sym': '<',
        },
        {
            'stroke': ['S-', 'P-', 'R-', 'A'],
            'sym': '>',
        },
        {
            'stroke': ['P-', 'W-'],
            'sym': '|',
        },
        {
            'stroke': ['P-', 'W-', 'R-'],
            'sym': '[',
        },
        {
            'stroke': ['S-', 'P-', 'W-', 'R-'],
            'sym': ']',
        },
        {
            'stroke': ['S-', 'K-', 'P-'],
            'sym': '&',
        },
        {
            'stroke': ['S-', 'K-', 'W-', 'R-'],
            'sym': '_',
        },
        {
            'stroke': ['S-', 'T-', 'R-', 'A'],
            'sym': '*',
        },
        {
            'stroke': ['T-'],
            'sym': "'",
        },
        {
            'stroke': ['T-', 'H-', 'R-'],
            'sym': '~',
        },
        {
            'stroke': ['T-', 'K-', 'H-', 'R-'],
            'sym': '$',
        },
        {
            'stroke': ['T-', 'K-', 'P-', 'W-'],
            'sym': '@',
        },
        {
            'stroke': ['T-', 'P-', 'H-'],
            'sym': '#',
        },
        {
            'stroke': ['T-', 'P-', 'R-'],
            'sym': '\\{',
        },
        {
            'stroke': ['S-', 'T-', 'P-', 'R-'],
            'sym': '\\}',
        },
        {
            'stroke': ['T-', 'W-'],
            'sym': '`',
        },
        {
            'stroke': ['T-', 'W-', 'R-'],
            'sym': '\\',
        },
        {
            'stroke': ['W-', 'R-'],
            'sym': '-',
        },
    ]

    spaces = [
        # neither side
        {
            'stroke': ['-F', '-P', '-L', '-T'],
            'prefix': '^',
            'suffix': '^',
        },
        # both sides
        {
            'stroke': ['-R', '-B', '-G', '-S'],
            'prefix': '',
            'suffix': '',
        },
        # left
        {
            'stroke': ['-R', '-P', '-L', '-T'],
            'prefix': '',
            'suffix': '^',
        },
        # right
        {
            'stroke': ['-F', '-P', '-G', '-S'],
            'prefix': '^',
            'suffix': '',
        },
    ]

    res = {}

    for sym in syms:
        for sp in spaces:
            if sp['prefix'] == sp['suffix'] == '':
                p = s = ''

            elif sym['sym'] in ".,!?^&":
                p = '{' + sp['prefix'] + '}'
                s = '{' + sp['suffix'] + '}'

            else:
                p = '{' + sp['prefix']
                s = sp['suffix'] + '}'

            res[build_stroke(sym['stroke'] + sp['stroke'])] = \
                p + sym['sym'] + s

            res[build_stroke(sym['stroke'] + sp['stroke'] + ['*'])] = \
                p + (sym['sym'] * 2) + s

    return res


write_dict(build_dict())
