#!/usr/bin/env python3

"""
Symbols are all typed on the left side.
Right side then decides if theres a space on the left, right, both, or neither side of the symbol.
Heavily inspired by https://stenomod.blogspot.com/2020/03/a-pattern-for-stroking-symbols-with.html.

Star key is used to insert two of the symbol (without space between them).

Spaces:
| Outline | Left | Right |
|---------+------+-------|
| -RGBS   | No   | No    |
| -FPLT   | Yes  | Yes   |
| -RPLT   | No   | Yes   |
| -FPGS   | Yes  | No    |

Syms:
| Outline | Sym | Explanaition           |
|---------+-----+------------------------|
| KPR     | ^   | shape                  |
| TP      | !   | used in TP-BG          |
| H       | ?   | used in H-F            |
| KPH     | /   | shape                  |
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
| TK      | $   | Dollar                 |
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
            'stroke': ['T-', 'K-'],
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
            'stroke': ['-R', '-B', '-G', '-S'],
            'prefix': '^',
            'suffix': '^',
        },
        # both sides
        {
            'stroke': ['-F', '-P', '-L', '-T'],
            'prefix': '',
            'suffix': '',
        },
        # left
        {
            'stroke': ['-F', '-P', '-G', '-S'],
            'prefix': '',
            'suffix': '^',
        },
        # right
        {
            'stroke': ['-R', '-P', '-L', '-T'],
            'prefix': '^',
            'suffix': '',
        },
    ]

    res = {}

    for sym in syms:
        for sp in spaces:
            if sym['sym'] == '&' and build_stroke(sp['stroke']) == "-FPGS":
                res["SKP-FPGS"] = "&{^}"
                continue

            if sym['sym'] == '^':
                res["KPR-FPLT"] = "^"
                res["KPR*FPLT"] = "^^"

                res["KPR-RBGS"] = "{^}^{^}"
                res["KPR*RBGS"] = "{^}^^{^}"

                res["KPR-FPGS"] = "^{^}"
                res["KPR*FPGS"] = "^^{^}"

                res["KPR-RPLT"] = "{^}^"
                res["KPR*RPLT"] = "{^}^^"

                continue


            if sp['prefix'] == sp['suffix'] == '':
                res[build_stroke(sym['stroke'] + sp['stroke'])] = \
                    sp['prefix'] + sym['sym'] + sp['suffix']
            else:
                res[build_stroke(sym['stroke'] + sp['stroke'])] = \
                    '{' + sp['prefix'] + sym['sym'] + sp['suffix'] + '}'

            if sp['prefix'] == sp['suffix'] == '':
                res[build_stroke(sym['stroke'] + sp['stroke'] + ['*'])] = \
                    sp['prefix'] + (sym['sym'] * 2) + sp['suffix']
            else:
                res[build_stroke(sym['stroke'] + sp['stroke'] + ['*'])] = \
                    '{' + sp['prefix'] + (sym['sym'] * 2) + sp['suffix'] + '}'

    return res


write_dict(build_dict())
