from itertools import permutations
from typing import List

import utils


def fname_anagram(anag: str) -> str:
    return 'anagram-{}'.format(anag)


def anagram(anag: str):
    """
    For all elements in all dictionaries, find words that contain any anagram of `anag` as a substring.

    For "non-consecutive anagrams" you just want a word bank: see wordbank.py.
    """
    found = []

    try:
        all_elems = utils.get_all_dicts()

        perms = perm_strs(anag)
        num_perms = len(perms)
        utils.print_progress_bar(0, num_perms)
        for i, perm in enumerate(perms):
            found.extend([elem for elem in all_elems if perm in elem])
            utils.print_progress_bar(i+1, num_perms)

    finally:
        print('found {} elems after containing an anagram'.format(len(found)))
        if found:
            utils.list_to_file(fname_anagram(anag), found)
            if len(found) < 100:
                for elem in found:
                    print('\t-', elem)


def anagram_cmd(args: List[str]):
    if len(args) != 1:
        raise Exception('`anagram` requires exactly one args (the string to find anagrams of)')
    anagram(utils.clean(args[0]))


def perm_strs(anag: str) -> List[str]:
    return [''.join(perm) for perm in permutations(anag)]
