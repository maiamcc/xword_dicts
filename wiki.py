#! /usr/bin/env python
from datetime import date

import requests

import utils

ITEMS = 'items'
VIEWS = 'views'

FIRST_OF_THIS_MONTH = date.today().strftime("%Y%m0100")

def query_url(name: str) -> str:
    # TODO: verify the name is right
    return 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{name}/monthly/2018010100/{end_date}'.format(name=name.replace(' ', '_'), end_date=FIRST_OF_THIS_MONTH)


# POPULARITY CHECK:
# for every name, search on wiki. If page, get views for last x months and calculate views per month (or total views?)
# if no page, will check manually
# order by page views and see if we care
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

    # print('total views: {}'.format(total_views))
    # print('views per month: {}'.format(total_views/num_months))

    return total_views/num_months


if __name__ == '__main__':
    names = utils.file_to_list('simpsons.raw')
    scores = {}
    couldnt_find = []

    utils.print_progress_bar(0, len(names))
    for i, name in enumerate(names):
        try:
            scores[name] = views_per_month(name)
        except Exception as e:
            print(e)
            couldnt_find.append(name)
        finally:
            utils.print_progress_bar(i+1, len(names))

    print()
    print('---FAILED TO FIND---')
    print(couldnt_find)
    print('------')
    print()

    sort_by_views = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for i in sort_by_views:
        print(i[0], i[1])
