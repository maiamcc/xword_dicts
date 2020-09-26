from datetime import date
from typing import List

import requests

import utils

ITEMS = 'items'
VIEWS = 'views'

FIRST_OF_THIS_MONTH = date.today().strftime("%Y%m0100")


def fname_ranked(file: str) -> str: return '{}.ranked'.format(file)


def query_url(name: str) -> str:
    # TODO: verify the name is right
    return 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{name}/monthly/2018010100/{end_date}'.format(name=name.replace(' ', '_'), end_date=FIRST_OF_THIS_MONTH)


def views_per_month(name: str) -> int:
    url = query_url(name)
    r = requests.get(url)
    if r.status_code != 200:
        j = r.json()
        raise Exception('Request failed with status {} ({}). Message:\n\t{}'.
                        format(r.status_code, j.get('title', '<no title>'), j.get('detail', '<no detail>')))
    payload = r.json()
    items = payload[ITEMS]
    total_views = 0
    num_months = 0
    for item in items:
        num_months += 1
        total_views += int(item[VIEWS])

    return total_views/num_months


def wikisort_cmd(args: List[str]):
    if len(args) != 1:
        # TODO: let you set in-prog vet file/output file/resume or restart vet?
        raise Exception('`rank` requires exactly one arg (path to file to dedupe)')
    wikisort_file(args[0])


def wikisort_file(file: str):
    _, names = utils.file_to_list(file)
    scores = {}
    couldnt_find = []

    utils.print_progress_bar(0, len(names))
    for i, name in enumerate(names):
        try:
            scores[name] = views_per_month(name)
        except:
            # should probably keep track of the exceptions (so can tell if it's rate limiting etc.)
            couldnt_find.append(name)
        finally:
            utils.print_progress_bar(i+1, len(names))

    print()
    print('---FAILED TO FIND---')
    print(couldnt_find)
    print('------')
    print()

    sort_by_views = ['{}\t{}'.format(k,v) for k, v in sorted(scores.items(), key=lambda x: x[1], reverse=True)]

    utils.list_to_file(fname_ranked(file), sort_by_views, do_dedupe=False)
