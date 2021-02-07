from typing import List

import utils


def fname_transformed(fromstr: str, tostr: str) -> str:
    if not tostr:
        tostr = 'EMPTY'
    return 'transform-{}-{}'.format(fromstr, tostr)


def transform(fromstr: str, tostr: str):
    """
    For all elements in all dictionaries, find words that are valid when transformation
    s/fromstr/tostr applied.
    """
    if tostr == '_':
        tostr = ''

    all_elems = utils.get_all_dicts()

    candidates = [elem for elem in all_elems if fromstr in elem and elem != fromstr]
    print('found {} candidates containing substring: {}'.format(len(candidates), fromstr))

    valid = []
    for cand in candidates:
        transformed = cand.replace(fromstr, tostr)
        if transformed in all_elems:
            valid.append('{} -> {}'.format(cand, transformed))

    print('found {} valid elems after transformation'.format(len(valid)))
    if valid:
        utils.list_to_file(fname_transformed(fromstr, tostr), valid)


def transform_cmd(args: List[str]):
    if len(args) != 2:
        raise Exception('`transform` requires exactly two args (`fromstr` and `tostr`) ' +
                        '(use underscore for empty string)')
    transform(args[0], args[1])
