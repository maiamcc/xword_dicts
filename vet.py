import os.path
from typing import List

import utils

def fname_vetted(file: str) -> str: return '{}.vetted'.format(file)
def fname_in_prog_vet(file: str) -> str: return '{}.in_prog_vet'.format(file)


def vet_file(basefile: str):
    """
    Read in the file $BASEFILE as newline-separated list,
    offers elements to user one by one to vet via cmd line.
    Approved elements are stored in $BASEFILE.vetted.

    Elements-to-vet stored in $BASEFILE.in_prog_vet. If this file
    exists when `vet` is called, user has the option of continuing
    the in-progress vet or starting a new one.
    """
    in_prog_file = fname_in_prog_vet(basefile)
    accepted = []
    use_existing_vet = False
    if os.path.isfile(in_prog_file):
        print('Vet in progress, continue existing? [Y/n]')
        answer = utils.ask_user_yn()
        if answer:
            elems = utils.file_to_list(in_prog_file)
            accepted = utils.file_to_list(fname_vetted(basefile))
            use_existing_vet = True
        else:
            os.remove(in_prog_file)
    # if no in-prog file but there exist a .vetted file?
    if not use_existing_vet:
        elems = utils.file_to_list(basefile)

    print('Elems to vet: {}'.format(len(elems)))
    finished = False
    i = 0
    try:
        for i, elem in enumerate(elems):
            print('{} -- approve? [y/N]'.format(elem))
            answer = utils.ask_user_yn(default=False)
            if answer:
                accepted.append(elem)
        print('hooray, finished vet!')
        finished = True
    finally:
        if len(accepted) > 0:
            utils.list_to_file(fname_vetted(basefile), accepted)
        if finished:
            print('Accepted {} candidates'.format(len(accepted)))
            if os.path.isfile(in_prog_file):
                os.remove(in_prog_file)
        else:
            utils.list_to_file(in_prog_file, elems[i:])
            print('Accepted {} candidates ({} remaining)'.format(len(accepted), len(elems)-i))


def vet_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you set in-prog vet file/output file/resume or restart vet?
        raise Exception('`vet` requires exactly one arg (path to file to vet)')
    vet_file(args[0])
