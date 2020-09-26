from typing import List

CROSSFILE_DEFAULT_DICT_PATH = '/Library/CrossFire/default.dict'


def file_to_list(file: str, do_dedupe=True) -> (List[str], List[str]):
    """Returns frontmatter (list of comment lines) and list of elements."""
    with open(file) as infile:
        contents = infile.read()
    li = contents.strip().split('\n')
    frontmatter = get_frontmatter(li)
    elems = [elem.strip() for elem in li if elem.strip() != '' and not elem.startswith('#')]
    if do_dedupe:
        elems = dedupe(elems)
    return frontmatter, elems


def list_to_file(file: str, li: List, do_dedupe=True):
    if do_dedupe:
        li = dedupe(li)
    with open(file, 'w') as outfile:
        outfile.write('\n'.join(li))


def get_frontmatter(lines: List[str]) -> List[str]:
    """Given a list of lines from a file, return any comment lines at the beginning."""
    frontmatter = []
    for ln in lines:
        if ln.startswith('#'):
            frontmatter.append(ln)
        elif ln.strip() != '':
            # we're reached a non-comment, non-whitespace line; done collecting frontmatter
            break

    return frontmatter


def dedupe(li: List[str], verbose: bool=False) -> List[str]:
    # Not the MOST efficient so we can retain order as much as possible
    seen = set()
    unique = []
    for item in li:
        cleaned = clean(item)
        if cleaned in seen:
            if verbose:
                print('~ X:', item)
            continue
        seen.add(cleaned)
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
    print('\r{prefix} |{bar}| {percent}% {suffix}'.
        format(prefix=prefix, bar=bar, percent=percent, suffix=suffix),
        end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()


def clean(s: str) -> str:
    for ch in ['.', '-', '"', '\'', ',', '/', ' ', '\'']:
        s = s.replace(ch, '').lower()
    return s


def get_crossfire_default_dict() -> set:
    _, entries = file_to_list(CROSSFILE_DEFAULT_DICT_PATH)
    # TODO: make sure tiny common words like "THE" end up in here
    return set(clean(entry.split(';')[0].lower()) for entry in entries)

# import utils
# xfire = utils.get_crossfire_default_dict()
# _, wds = utils.file_to_list('nltk-words-full.dict')
# megadict = xfire|set(wds)
# from nltk.corpus import gutenberg
# notin = set()
# for wd in gutenberg.words('austen-emma.txt'):
#     if wd.isalpha() and utils.clean(wd) not in megadict:
#         notin.add(wd)
