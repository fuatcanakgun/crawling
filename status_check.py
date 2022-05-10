import pandas as pd
import requests
from lxml import html
from datetime import date
import numpy as np
import time

def check_status(df):
    today = str(date.today())
    for x in range(len(df)):
        if df.loc[x,'is_active'] == True:
            url = df.loc[x,'url']
            api_url = str(url)
            time.sleep(0.5)
            try:   
                req = requests.get(api_url)
            except:
                continue
            tree = html.fromstring(req.content)
            if req.status_code == 404 or (tree.xpath('//*[@id="classifiedId"]/text()')) == []:
                df.loc[x,'is_active'] = False
                df.loc[x,'pasive_date'] = today
            elif df['Kategori'].isna()[x] == True:
                df.loc[x,'is_active'] = np.nan
                df.loc[x,'pasive_date'] = np.nan
            else:
                df.loc[x,'is_active'] = True
                df.loc[x,'pasive_date'] = np.nan
    return df