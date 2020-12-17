#!/usr/bin/env python3

"""
Transform the last N words into an identifier.

Relies on https://github.com/buffet/plover_retro_stringop.

All chords defined here use KWR-.
The casing style is selected with a combination of -RBG.
The number of words can either be increased by repeating the chord, or by adding a number.

Note that KWR-R (why are) gets lost.

Case style:
snake_case:  -R
camelCase:   -B
PascalCase:  -G
UPPER_SNAKE: -RB
kebap-case:  -BG

Numbers:
These use a binary encoding using the left hand, similar to the left hand modifier dict.

1:  H-
2:  P-
3:  PH-
4:  T-
5:  TH-
6:  TP-
7:  TPH-
8:  S-
9:  SH-
10: STPH- (special case, easier to press than SP-)
"""

from steno import build_stroke, write_dict


def build_dict():
    # stolen from left hand modifiers
    numbers = [
        [],  # 0 not bound
        ['H-'],
        ['P-'],
        ['P-', 'H-'],
        ['T-'],
        ['T-', 'H-'],
        ['T-', 'P-'],
        ['T-', 'P-', 'H-'],
        ['S-'],
        ['S-', 'H-'],
        ['S-', 'T-', 'P-', 'H-'],  # actually 15, but it's nice to press
    ]

    # keys used in all strokes
    common = ['K-', 'W-', 'R-']

    cases = [
        # snake_case
        {
            'stroke': ['-R'],
            'expr': r'"_".join([w.lower() for w in words])',
        },
        # camelCase
        {
            'stroke': ['-B'],
            'expr': r'"".join([w.lower() if i == 0 else w.lower().capitalize() for i, w in enumerate(words)])',
        },
        # PascalCase
        {
            'stroke': ['-G'],
            'expr': r'"".join([w.lower().capitalize() for w in words])',
        },
        # UPPER_SNAKE_CASE
        {
            'stroke': ['-R', '-B'],
            'expr': r'"_".join([w.upper() for w in words])',
        },
        # kebap-case
        {
            'stroke': ['-B', '-G'],
            'expr': r'"-".join([w.lower() for w in words])',
        },
    ]

    res = {}

    for case in cases:
        keys = common + case['stroke']

        for n in range(1, 11):
            command = f"{{:retro_stringop:{n}:{case['expr']}}}"
            num_stroke = build_stroke(keys + numbers[n])
            multi_stroke = "/".join([build_stroke(keys)] * n)

            res[num_stroke] = command
            res[multi_stroke] = command

    return res


write_dict(build_dict())
