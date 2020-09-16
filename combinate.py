from typing import List

import utils

WORDS = utils.get_crossfire_default_dict()


def fname_combinated(file: str) -> str:
    return '{}.combinated'.format(file)


def combinate_file(file: str):
    """
    Read in the file of names $FILE as newline-separated list, and for every name,
    generate crossword candidates: [first last, first, last], etc.

    Stores results in $FILE.combinated.
    """
    names = utils.file_to_list(file)
    results = []
    for name in names:
        results.extend(combinate(name))

    print('{} names resulted in {} combinations'.format(len(names), len(results)))
    utils.list_to_file(fname_combinated(file), results)


def combinate(name: str) -> List[str]:
    res = [name]
    chunks = name.split(" ")
    if len(chunks) == 1:
        return res
    res.extend(chunks)
    if len(chunks) > 2:
        for i in range(len(chunks)-1):
            res.append('{} {}'.format(chunks[i], chunks[i+1]))

    # A combination is valid if it's >= 3 chars and not a common word
    return [comb for comb in res if utils.clean(comb).lower() not in WORDS and len(utils.clean(comb)) >= 3]


def combinate_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you set in-prog vet file/output file/resume or restart vet?
        raise Exception('`combinate` requires exactly one arg (path to file to dedupe)')
    combinate_file(args[0])
