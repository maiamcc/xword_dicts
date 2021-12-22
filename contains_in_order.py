from collections import defaultdict
from typing import Dict, List

import utils


def fname_contains_in_order(wd: str) -> str:
    return 'contains_in_order-{}'.format(wd)


def contains_in_order(wd: str):
    """
    For all elements in all dictionaries, find elements that contain the letters
    of the given word in order (though not necessarily consecutively).
    """
    minchars = len(wd)
    all_elems = utils.get_all_dicts()

    valid = []
    for elem in all_elems:
        if len(elem) < minchars:
            continue
        if wd in elem:  # candidate just contains the word wholesale (not spread out)
            continue
        if _contains_in_order(elem, wd):
            valid.append(elem)

    print('found {} valid elems that contain the ordered characters {}'.format(len(valid), wd))
    if valid:
        utils.list_to_file(fname_contains_in_order(wd), valid)
        if len(valid) < 100:
            for wd in valid:
                print('\t-', wd)


def contains_in_order_cmd(args: List[str]):
    if len(args) != 1:
        raise Exception('`contains_in_order` requires exactly one arg (the word to find within candidates)')
    wd = args[0]
    if any([not ch.isalpha() for ch in wd]):
        raise Exception('contains_in_order must contain only alphabetical characters (got: {})'.format(wd))
    contains_in_order(wd)


def _contains_in_order(candidate: str, wd: str) -> bool:
    start = 0  # index to search from
    last_index = len(candidate) - 1
    for ch in wd:
        if start > last_index:
            # we still have letters left to find, but we've hit the end of the candidate
            return False

        i = candidate.find(ch, start)

        if i == -1:
            # This letter wasn't found in the candidate
            return False

        start = i + 1

    return True
