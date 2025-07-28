import requests
import csv
from itertools import zip_longest
from bs4 import BeautifulSoup

query = 'python'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

jobs_title = []
jobs_location = []
companies = []
jobs_type = []
jobs_place = []

for i in range(3):
    url = f'https://wuzzuf.net/search/jobs/?q={query}&start={i}'
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')

    titles = soup.find_all('h2', {'class': 'css-m604qf'})
    locations = soup.find_all('span', {'class': 'css-5wys0k'})
    comps = soup.find_all('a', {'class': 'css-17s97q8'})
    types = soup.find_all('span', {'class': 'css-1ve4b75'})
    places = soup.find_all('span', {'class': 'css-o1vzmt'})

    for t in titles:
        jobs_title.append(t.text.strip())

    for l in locations:
        jobs_location.append(l.text.strip())

    for c in comps:
        companies.append(c.text.split('-')[0].strip())

    for ty in types:
        jobs_type.append(ty.text.strip())

    for p in places:
        jobs_place.append(p.text.strip())

jobs = {
    'title': jobs_title,
    'location': jobs_location,
    'company': companies,
    'type': jobs_type,
    'place': jobs_place
}

import pandas as pd

df = pd.DataFrame(jobs)
df.to_excel("jobs.xlsx", index=False)