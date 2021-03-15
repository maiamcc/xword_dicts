from collections import defaultdict
from typing import Dict, List

import utils


def fname_wordbank(wdbnk: str) -> str:
    return 'wordbank-{}'.format(wdbnk)


def wordbank(wdbnk_counts: Dict[str, int], wdbnk: str):
    """
    For all elements in all dictionaries, find elements that contain all of the letters
    in the given wordbank
    """
    minchars = sum(wdbnk_counts.values())
    all_elems = utils.get_all_dicts()

    valid = []
    for elem in all_elems:
        if len(elem) < minchars:
            continue
        if matches_wordbank(elem, wdbnk_counts):
            valid.append(elem)

    print('found {} valid elems matching wordbank {}'.format(len(valid), wdbnk))
    if valid:
        utils.list_to_file(fname_wordbank(wdbnk), valid)
        if len(valid) < 100:
            for wd in valid:
                print('\t-', wd)


def wordbank_cmd(args: List[str]):
    if len(args) != 1:
        raise Exception('`wordbank` requires exactly one args (the wordbank to use)')
    wdbnk = args[0]
    if any([not ch.isalpha() for ch in wdbnk]):
        raise Exception('Wordbank must contain only alphabetical characters (got: {})'.format(wdbnk))
    wordbank(charcount(wdbnk.lower()), wdbnk)


def matches_wordbank(wd: str, bank: Dict[str, int]) -> bool:
    wd_chars = charcount(wd)
    if len(wd_chars) != len(bank):
        return False
    for k, v in bank.items():
        if not wd_chars.get(k, 0) >= v:
            return False

    return True


def charcount(wd: str) -> Dict[str, int]:
    d = defaultdict(int)
    for ch in wd:
        d[ch] += 1
    return d
