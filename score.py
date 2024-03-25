import os.path
from typing import List

import utils

SCORES = {
    "0": 100,
    "9": 90,
    "8": 80,
    "7": 70,
    "6": 60,
    "5": 50,
    "4": 40,
    "3": 30,
    "2": 20,
    "1": 10,
    "x": 0

}
def fname_scored(file: str) -> str: return '{}.scored'.format(file)
def fname_in_prog_score(file: str) -> str: return '{}.in_prog_score'.format(file)


def score_file(basefile: str):
    """
    Read in the file $BASEFILE as newline-separated list, offers elements
    to user one by one to vet via cmd line to score.
    Approved elements are stored in $BASEFILE.scored.

    Elements-to-score stored in $BASEFILE.in_prog_score. If this file
    exists when `score` is called, user has the option of continuing
    the in-progress score or starting a new one.
    """
    in_prog_file = fname_in_prog_score(basefile)
    scored = []
    use_existing_score = False
    if os.path.isfile(in_prog_file):
        print('Score in progress, continue existing? [Y/n]')
        answer = utils.ask_user_yn()
        if answer:
            frontmatter, elems = utils.file_to_list(in_prog_file)
            _, scored = utils.file_to_list(fname_scored(basefile))
            use_existing_score = True
        else:
            os.remove(in_prog_file)
    # if no in-prog file but there exist a .scored file?
    if not use_existing_score:
        frontmatter, elems = utils.file_to_list(basefile)

    print('Elems to score: {}'.format(len(elems)))
    finished = False
    i = 0
    try:
        for i, elem in enumerate(elems):
            print(elem)
            score = ask_user_score()
            scored.append('{};{}'.format(elem, score))
        print('hooray, finished scoring!')
        finished = True
    finally:
        if len(scored) > 0:
            utils.list_to_file(fname_scored(basefile), frontmatter + scored)
        if finished:
            print('Scored {} candidates'.format(len(scored)))
            if os.path.isfile(in_prog_file):
                os.remove(in_prog_file)
        else:
            utils.list_to_file(in_prog_file, frontmatter + elems[i:])
            print('Scored {} candidates ({} remaining)'.format(len(scored), len(elems)-i))


def ask_user_score() -> int:
    val = input('> ')
    if not val:
        return 0
    if val.lower() in SCORES:
        return SCORES[val.lower()]
    return ask_user_score()


def score_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you set in-prog vet file/output file/resume or restart vet?
        raise Exception('`vet` requires exactly one arg (path to file to vet)')
    score_file(args[0])
