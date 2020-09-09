#! /usr/bin/env python
import sys

from combinate import combinate_cmd
from dedupe import dedupe_cmd
from vet import vet_cmd
from wiki import rank_cmd


CMDS_TO_FUNCS = {
    'dedupe': dedupe_cmd,
    'combinate': combinate_cmd,
    'rank': rank_cmd,
    'vet': vet_cmd,
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
