# import requests
import json

ITEMS = 'items'
VIEWS = 'views'
# https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Albert_Einstein/monthly/2020010100/3030090100

# POPULARITY CHECK:
# for every name, search on wiki. If page, get views for last x months and calculate views per month (or total views?)
# if no page, will check manually
# order by page views and see if we care

# Dan Castellaneta
# Kevin Dillon

raw = '''{"items":[{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020010100","access":"all-access","agent":"user","views":55489},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020020100","access":"all-access","agent":"user","views":44984},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020030100","access":"all-access","agent":"user","views":51493},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020040100","access":"all-access","agent":"user","views":66431},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020050100","access":"all-access","agent":"user","views":66785},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020060100","access":"all-access","agent":"user","views":57096},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020070100","access":"all-access","agent":"user","views":49455},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020080100","access":"all-access","agent":"user","views":65651},{"project":"en.wikipedia","article":"Dan_Castellaneta","granularity":"monthly","timestamp":"2020090100","access":"all-access","agent":"user","views":10907}]}'''

payload = json.loads(raw)

items = payload[ITEMS]
total_views = 0
num_months = 0
for item in items:
    num_months += 1
    total_views += int(item[VIEWS])

print('DAN CAST...')
print('total views: {}'.format(total_views))
print('views per month: {}'.format(total_views/num_months))
