from typing import List

CROSSFILE_DEFAULT_DICT_PATH = '/Library/CrossFire/default.dict'


def file_to_list(file: str, do_dedupe=True) -> List[str]:
    with open(file) as infile:
        contents = infile.read()
    li = contents.strip().split('\n')
    elems = [elem.strip() for elem in li if elem.strip() != '' and not elem.startswith('#')]
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


# Print iterations progress: https://stackoverflow.com/a/34325723
def print_progress_bar(iteration, total, prefix='Progress', suffix='Complete',
                       decimals=1, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()


def get_crossfire_default_dict() -> set:
    entries = file_to_list(CROSSFILE_DEFAULT_DICT_PATH)
    return set(entry.split(';')[0].lower() for entry in entries)
