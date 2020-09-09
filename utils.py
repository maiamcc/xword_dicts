#! /usr/bin/env python
import os.path
import sys
from typing import List


### File Names
def file_vetted(file: str) -> str: return '{}.vetted'.format(file)
def file_in_prog_vet(file: str) -> str: return '{}.in_prog_vet'.format(file)
def file_deduped(file: str) -> str: return '{}.deduped'.format(file)
def file_combinated(file: str) -> str: return '{}.combinated'.format(file)


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
    deduped = dedupe_in_place(elems)
    print('Elems after dedupe: {}'.format(len(deduped)))

    list_to_file(file_deduped(file), elems)


def dedupe_in_place(li: List[str]) -> List[str]:
    # Not the MOST efficient so we can retain order as much as possible
    seen = set()
    unique = []
    for item in li:
        if item in seen:
            continue
        seen.add(item)
        unique.append(item)
    return unique


def vet_file(basefile: str):
    """
    Read in the file $BASEFILE as newline-separated list,
    offers elements to user one by one to vet via cmd line.
    Approved elements are stored in $BASEFILE.vetted.

    Elements-to-vet stored in $BASEFILE.in_prog_vet. If this file
    exists when `vet` is called, user has the option of continuing
    the in-progress vet or starting a new one.
    """
    in_prog_file = file_in_prog_vet(basefile)
    accepted = []
    use_existing_vet = False
    if os.path.isfile(in_prog_file):
        print('Vet in progress, continue existing? [Y/n]')
        answer = ask_user_yn()
        if answer:
            elems = dedupe_in_place(file_to_list(in_prog_file))
            accepted = dedupe_in_place(file_to_list(file_vetted(basefile)))
            use_existing_vet = True
    # if no in-prog file but there exist a .vetted file?
    if not use_existing_vet:
        elems = dedupe_in_place(file_to_list(basefile))
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
            list_to_file(file_vetted(basefile), accepted)
        if finished:
            print('Accepted {} candidates'.format(len(accepted)))
            # delete in-prog file
        else:
            list_to_file(in_prog_file, elems[i:])
            print('Accepted {} candidates ({} remaining)'.format(len(accepted), len(elems)-i))


def combinate_file(file: str):
    """
    Read in the file of names $FILE as newline-separated list, and for every name,
    generate crossword candidates: [first last, first, last], etc.

    Stores results in $FILE.combinated.
    """
    names = file_to_list(file)
    results = []
    for name in names:
        results.extend(combinate(name))

    print('{} names resulted in {} combinations'.format(len(names), len(results)))
    list_to_file(file_combinated(file), dedupe_in_place(results))


def combinate(name: str) -> List[str]:
    res = [name]
    chunks = name.split(" ")
    if len(chunks) == 1:
        return res
    res.extend([chunks[0], chunks[-1]])
    if len(chunks) > 2:
        for i in range(len(chunks)-1):
            res.append('{} {}'.format(chunks[i], chunks[i+1]))
    return res


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


def combinate_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you set in-prog vet file/output file/resume or restart vet?
        raise Exception('`vet` requires exactly one arg (path to file to dedupe)')
    combinate_file(args[0])


CMDS_TO_FUNCS = {'dedupe': dedupe_cmd, 'vet': vet_cmd,
                 'combinate': combinate_cmd}


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
