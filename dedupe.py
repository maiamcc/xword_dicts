from typing import List

import utils


def fname_deduped(file: str) -> str: return '{}.deduped'.format(file)


def dedupe_from_file(file: str):
    """
    Read in the file $FILE as newline-separated list,
    dedupe list and write to $FILE.deduped
    """
    elems = utils.file_to_list(file, do_dedupe=False)
    print('Elems before dedupe: {}'.format(len(elems)))
    deduped = utils.dedupe(elems)
    print('Elems after dedupe: {}'.format(len(deduped)))

    utils.list_to_file(fname_deduped(file), elems)


def dedupe_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you dedupe to the same file?
        raise Exception('`dedupe` requires exactly one arg (path to file to dedupe)')
    dedupe_from_file(args[0])
