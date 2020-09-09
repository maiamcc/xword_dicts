from typing import List


def file_to_list(file: str, do_dedupe=True) -> List[str]:
    with open(file) as infile:
        contents = infile.read()
    li = contents.strip().split('\n')
    elems = [elem.strip() for elem in li if elem.strip() != '']
    if do_dedupe:
        elems = dedupe(elems)
    return elems


def list_to_file(file: str, li: List, do_dedupe=True):
    if do_dedupe:
        li = dedupe(li)
    with open(file, 'w') as outfile:
        outfile.write('\n'.join(li))


def dedupe(li: List[str]) -> List[str]:
    # Not the MOST efficient so we can retain order as much as possible
    seen = set()
    unique = []
    for item in li:
        if item in seen:
            continue
        seen.add(item)
        unique.append(item)
    return unique


def ask_user_yn(default=True):
    val = input('> ')
    if not val:
        return default
    if val.lower() in ['y', 'yes']:
        return True
    return False
