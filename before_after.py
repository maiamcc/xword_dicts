from collections import defaultdict
from typing import Dict, List

import utils


def fname_before_after(s: str) -> str:
    return 'before_after-{}'.format(s)


def before_after(s: str):
    """
    For all elements in all dictionaries, find elements that, if split on string s, form two valid words
    """
    # minchars = sum(wdbnk_counts.values())
    all_elems = utils.get_all_dicts()

    valid = []
    for elem in all_elems:
        # if len(elem) < minchars:
        #     continue
        if matches_before_after(elem, s, all_elems):
            valid.append(pretty(elem, s))

    print('found {} valid elems matching before_after {}'.format(len(valid), s))
    if valid:
        utils.list_to_file(fname_before_after(s), valid)
        if len(valid) < 100:
            for wd in valid:
                print('\t-', wd)


def before_after_cmd(args: List[str]):
    if len(args) != 1:
        raise Exception('`before_after` requires exactly one args (the string to split on)')
    before_after(args[0].lower())


def matches_before_after(wd: str, s: str, all_elems: set) -> bool:
    if s not in wd:
        return False
    splits = wd.split(s, 1)
    return len(splits[0]) >= 3 and len(splits[1]) >= 3 and splits[0] in all_elems and splits[1] in all_elems


def pretty(wd: str, s: str) -> str:
    splits = wd.split(s, 1)
    return '{} --> {} / {}'.format(wd, splits[0], splits[1])