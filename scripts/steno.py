"""
Common library used by my scripts.
"""

import json
import sys


def build_stroke(keys):
    """
    Transforms an array of keys into a string representing a stroke.

    Example:
    ['R-', '-R', 'W-', 'S-'] -> "SWR-R"
    """

    order = [
        'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
        'A', 'O', '*', 'E', 'U',
        '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
    ]

    translate = {key: idx for idx, key in enumerate(order)}

    keys = [translate[key] for key in keys]
    keys = list(sorted(set(keys)))
    keys = [order[key] for key in keys]

    # use " " as seperator if there is none of AO*EU
    # later this gets replaced with a - when all other - get removed
    for idx, key in enumerate(keys):
        if key in 'AO*EU':
            break

        if key.startswith('-'):
            keys.insert(idx, ' ')
            break

    keys = [key.replace("-", "").replace(" ", "-") for key in keys]

    return "".join(keys)


def write_dict(dict):
    json_dict = json.dumps(dict, sort_keys=True, indent=0)
    with open(sys.argv[1], 'w') as f:
        f.write(json_dict)
