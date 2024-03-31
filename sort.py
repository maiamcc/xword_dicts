import os.path
from typing import List

import utils

def fname_sorted(file: str) -> str: return '{}.sorted'.format(file)


def sort_file(basefile: str):
    """
    Output a new version of the file with its elements xword-sorted
    (i.e. be length, then alphabetically)
    """
    frontmatter, elems = utils.file_to_list(basefile)

    utils.list_to_file(fname_sorted(basefile), frontmatter + utils.sorted_xwd(elems))


def sort_cmd(args: List[str]):
    if len(args) != 1:
        raise Exception('`sort` requires exactly one arg (path to file to sort)')
    sort_file(args[0])
