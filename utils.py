#! /usr/bin/env python
import os.path
import sys
from typing import List


### File Names
def file_vetted(file: str) -> str: return '{}.vetted'.format(file)
def file_in_prog_vet(file: str) -> str: return '{}.in_prog_vet'.format(file)
def file_deduped(file: str) -> str: return '{}.deduped'.format(file)


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
    deduped = dedupe(elems)
    print('Elems after dedupe: {}'.format(len(deduped)))

    list_to_file(file_deduped(file), elems)


def dedupe(li: List[str]) -> List[str]:
    return list(set(li))


def vet_file(file: str):
    """
    Read in the file $FILE as newline-separated list,
    offers elements to user one by one to vet via cmd line.
    Approved elements are stored in $FILE.vetted.

    Elements-to-vet stored in $FILE.in_prog_vet. If this file
    exists when `vet` is called, user has the option of continuing
    the in-progress vet or starting a new one.
    """
    in_prog_file = file_in_prog_vet(file)
    accepted = []
    use_existing_vet = False
    if os.path.isfile(in_prog_file):
        print('Vet in progress, continue existing? [Y/n]')
        answer = ask_user_yn()
        if answer:
            elems = dedupe(file_to_list(in_prog_file))
            accepted = dedupe(file_to_list(file_vetted(file)))
            use_existing_vet = True
    # if no in-prog file but there exist a .vetted file?
    if not use_existing_vet:
        elems = dedupe(file_to_list(file))
        # delete in-prog vet file?

    print('Elems to vet: {}'.format(len(elems)))
    finished = False
    i = 0
    try:
        for i, elem in enumerate(elems):
            print('`{}` -- approve? [y/N]'.format(elem))
            answer = ask_user_yn(default=False)
            if answer:
                accepted.append(elem)
        print('hooray, finished vet!')
        finished = True
    finally:
        if len(accepted) > 0:
            list_to_file(file_vetted(file), accepted)
        if finished:
            print('Accepted {} candidates'.format(len(accepted)))
            # delete in-prog file
        else:
            list_to_file(in_prog_file, elems[i:])
            print('Accepted {} candidates ({} remaining)'.format(len(accepted), len(elems)-i))


def ask_user_yn(default=True):
    val = input('> ')
    if not val:
        return default
    if val.lower() in ['y', 'yes']:
        return True
    return False


def dedupe_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you dedupe to the same file?
        raise Exception('`dedupe` requires exactly one arg (path to file to dedupe)')
    dedupe_from_file(args[0])


def vet_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you set in-prog vet file/output file/resume or restart vet?
        raise Exception('`vet` requires exactly one arg (path to file to dedupe)')
    vet_file(args[0])


CMDS_TO_FUNCS = {'dedupe': dedupe_cmd, 'vet': vet_cmd}


def main():
    # TODO: help menu
    args = sys.argv
    script = args.pop(0)
    print('Running {}'.format(script))

    if len(args) == 0:
        raise Exception('No command provided (available commands: {})'.format(", ".join(CMDS_TO_FUNCS.keys())))

    cmd = args.pop(0)
    func = CMDS_TO_FUNCS.get(cmd)
    if func is None:
        raise Exception('Unrecognized command: `{}` (available commands: {})'.format(cmd, ", ".join(CMDS_TO_FUNCS.keys())))

    func(args)


if __name__ == '__main__':
    main()
