#! /usr/bin/env python
from datetime import date
import sys

import requests

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

    print('total views: {}'.format(total_views))
    print('views per month: {}'.format(total_views/num_months))

    return total_views/num_months

if __name__ == '__main__':
    views_per_month(sys.argv[1])
