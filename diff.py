import os.path
from typing import List

import utils


def fname_diffed(file1: str, file2: str) -> str: return f'{file1}.diff'


def diff_files(file1: str, file2: str):
    """
    Read in the files as newline-separated list, writes a file of all elements in file1 not in file2
    (ignoring scores and order).
    """

    print(f"diffing: {file1} / {file2}")
    _, elems1 = utils.file_to_list(file1, strip_scores=True)
    _, elems2 = utils.file_to_list(file2, strip_scores=True)

    set1 = {utils.clean(elem) for elem in elems1}
    set2 = {utils.clean(elem) for elem in elems2}

    result = utils.sorted_xwd(list(set1.difference(set2)))

    utils.list_to_file(fname_diffed(file1, file2), result)

    print(f'{len(elems1)} in input file --> {len(result)} after diff')


def diff_cmd(args: List[str]):
    if len(args) != 2:
        raise Exception('`diff` requires exactly 2 args (two files to diff)')
    diff_files(args[0], args[1])
