import requests
import xmltodict
import pandas as pd
from datetime import date, timedelta

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.9,tr;q=0.8',
    'cache-control':'max-age=0',
    'sec-ch-ua':'"Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"macOS"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'none',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36', 
    }
payload={}
files={}

def get_ads():
    today = date.today().strftime('%Y-%m-%d')
    yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    month = date.today().strftime('%B')
    year = date.today().strftime('%Y')
    list=[]
    for i in range(0,40):
        response = requests.get(f'https://www.sahibinden.com/sitemap/auctions/daily{i}.xml', headers=headers, data=payload, files=files)
        if response.status_code != 404:
            raw = xmltodict.parse(response.text)
            for x in raw['urlset']['url']:
                if ('is-makineleri-sanayi-is-makineleri-' in x['loc']) and str(yesterday) in x['lastmod']:
                    ad = {'url':x['loc'], 'date':x['lastmod'], 'year':x['lastmod'].split('-')[0], 'month':x['lastmod'].split('-')[1], 'day':x['lastmod'].split('-')[2]}
                    list.append(ad)
    df = pd.DataFrame(list)
    list1 = []
    list2 = []
    for i in range(len(df)):
        list1.append((df['url'][i][75:-6].split('-')[-1]))
        if df['url'][i][67:-6].split('-')[0] == 'satilik':
            list2.append('for_sale')
        else:
            list2.append('for_rent')
    df['id'] = list1
    df['type'] = list2
    df['ad_collect_date'] = today
    df.reset_index(drop=True,inplace=True)
    filepath = (f'/crawling/archive/{year}_{month}/{yesterday}.csv')
    df.to_csv(filepath, index=False)
get_ads()