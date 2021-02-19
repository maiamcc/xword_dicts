from typing import List

import utils


def new_entries(path: str):
    """
    Print all entries from the dict at `path` that are new (i.e. don't appear in any of the other dicts).
    """
    existing = utils.get_all_dicts()
    new_dict = utils.get_dict_at_path(path)

    print('Elements in {} that are new:'.format(path))
    not_new = []
    for elem in new_dict:
        if elem not in existing:
            print('\t- {}'.format(elem))
        else:
            not_new.append(elem)

    print()
    print('Elements that are NOT new:')
    for elem in not_new:
        print('\t- {}'.format(elem))


def new_entries_cmd(args: List[str]):
    if len(args) != 1:
        raise Exception('`new_entries` requires exactly one args (the path of the dict to check). Got {}: {}'.
                        format(len(args), args))

    new_entries(args[0])
