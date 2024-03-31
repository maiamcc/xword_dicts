#! /usr/bin/env python
import sys

from anagram import anagram_cmd
from before_after import before_after_cmd
from contains_in_order import contains_in_order_cmd
from combinate import combinate_cmd
from dedupe import dedupe_cmd
from diff import diff_cmd
from new_entries import new_entries_cmd
from score import score_cmd
from sort import sort_cmd
from transform import transform_cmd
from vet import vet_cmd
from wiki import wikisort_cmd
from wordbank import wordbank_cmd


CMDS_TO_FUNCS = {
    'anagram': anagram_cmd,
    'before_after': before_after_cmd,
    'combinate': combinate_cmd,
    'contains_in_order': contains_in_order_cmd,
    'dedupe': dedupe_cmd,
    'diff': diff_cmd,
    'new': new_entries_cmd,
    'score': score_cmd,
    'sort': sort_cmd,
    'transform': transform_cmd,
    'vet': vet_cmd,
    'wikisort': wikisort_cmd,
    'wordbank': wordbank_cmd,
}

AVAILABLE_CMDS = ", ".join(CMDS_TO_FUNCS.keys())


def main():
    # TODO: help menu
    args = sys.argv
    script = args.pop(0)
    print('Running {}'.format(script))

    if len(args) == 0:
        raise Exception('No command provided (available commands: {})'.format(AVAILABLE_CMDS))

    cmd = args.pop(0)
    func = CMDS_TO_FUNCS.get(cmd)
    if func is None:
        raise Exception('Unrecognized command: `{}` (available commands: {})'.format(cmd, AVAILABLE_CMDS))

    func(args)


if __name__ == '__main__':
    main()
