#! /usr/bin/env python
import sys
from typing import List


def file_to_list(file: str) -> List[str]:
    with open(file) as infile:
        contents = infile.read()
    li = contents.strip().split('\n')
    return [elem.strip() for elem in li if elem.strip() != '']


def list_to_file(file: str, li: List):
    with open(file, 'w') as outfile:
        outfile.write('\n'.join(li))


def dedupe_from_file(file: str):
    """Read in the file $FILE as newline-separated list,
    dedupe list and write to $FILE.deduped"""
    elems = file_to_list(file)
    print('Elems before dedupe: {}'.format(len(elems)))
    deduped = list(set(elems))
    print('Elems after dedupe: {}'.format(len(deduped)))

    outfile = '{}.deduped'.format(file)
    list_to_file(outfile, elems)


def dedupe_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you dedupe to the same file?
        raise Exception('`dedupe` requires exactly one arg (path to file to dedupe)')
    dedupe_from_file(args[0])


CMDS_TO_FUNCS = {'dedupe': dedupe_cmd}


def main():
    # TODO: help menu
    args = sys.argv
    script = args.pop(0)
    print('Running {}'.format(script))

    if len(args) == 0:
        raise Exception('No command provided')

    cmd = args.pop(0)
    func = CMDS_TO_FUNCS.get(cmd)
    if func is None:
        raise Exception('Unrecognized command: `{}` (available commands: {})'.format(cmd, ", ".join(CMDS_TO_FUNCS.keys())))

    func(args)


if __name__ == '__main__':
    main()
