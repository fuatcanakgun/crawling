import requests
from lxml import html
import pandas as pd
import numpy as np

def get_details (csv_loc):
    result_list = []
    ilan_no_list = pd.read_csv(csv_loc, usecols = ['ilan_no'])['ilan_no']
    ilan_url_list = pd.read_csv(csv_loc, usecols = ['url'])['url']

    for x, link in enumerate(ilan_url_list):

        link = str(link)
        page = requests.get(link)
        tree = html.fromstring(page.content)

        if page.status_code == 200 and (tree.xpath('//*[@id="searchContainer"]/div[4]/div[2]/p/span/span[2]/text()')) == []:

            try:    
                row2_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[2]/strong/text()')[0].strip()
                row2_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[2]/span/text()')[0].strip()
            except:
                row2_key = ""
                row2_value = ""

            try:
                row3_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[3]/strong/text()')[0].strip()
                row3_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[3]/span/text()')[0].strip()
            except:
                row3_key = ""
                row3_value = ""

            try:
                row4_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[4]/strong/text()')[0].strip()
                row4_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[4]/span/text()')[0].strip()
            except: 
                row4_key = ""
                row4_value = ""

            try:
                row5_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[5]/strong/text()')[0].strip()
                row5_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[5]/span/text()')[0].strip()
            except:
                row5_key = ""
                row5_value = ""

            try:    
                row6_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[6]/strong/text()')[0].strip()
                row6_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[6]/span/text()')[0].strip()
            except:
                row6_key = ""
                row6_value = ""

            try:
                row7_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[7]/strong/text()')[0].strip()
                row7_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[7]/span/text()')[0].strip()
            except: 
                row7_key = ""
                row7_value = ""

            try:
                row8_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[8]/strong/text()')[0].strip()
                row8_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[8]/span/text()')[0].strip()
            except:
                row8_key = ""
                row8_value = ""

            try:
                row9_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[9]/strong/text()')[0].strip()
                row9_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[9]/span/text()')[0].strip()
            except:
                row9_key = ""
                row9_value = ""

            try:
                row10_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[10]/strong/text()')[0].strip()
                row10_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[10]/span/text()')[0].strip()
            except: 
                row10_key = ""
                row10_value = ""

            try:
                row11_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[11]/strong/text()')[0].strip()
                row11_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[11]/span/text()')[0].strip()
            except:
                row11_key = ""
                row11_value = ""

            try:
                row12_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[12]/strong/text()')[0].strip()
                row12_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[12]/span/text()')[0].strip()
            except:
                row12_key = ""
                row12_value = ""

            try:
                row13_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[13]/strong/text()')[0].strip()
                row13_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[13]/span/text()')[0].strip()
            except:
                row13_key = ""
                row13_value = ""

            try:
                row14_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[14]/strong/text()')[0].strip()
                row14_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[14]/span/text()')[0].strip()
            except:
                row14_key = ""
                row14_value = ""

            try:
                row15_key = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[15]/strong/text()')[0].strip()
                row15_value = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/ul/li[15]/span/text()')[0].strip()
            except:
                row15_key = ""
                row15_value = ""

            try:
                row16_key = tree.xpath('//*[@id="classified-detail"]/div[1]/div[1]/h3/a/text()')[0].strip()
                row16_value = tree.xpath('//*[@id="classifiedDescription"]/p/text()')[0].strip()
            except:
                row16_key = ""
                row16_value = ""
            
            try:
                company = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[3]/div[1]/div[2]/div[1]/a/span/span/text()')[0].strip()
            except:
                company = np.NaN

            city = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/h2/text()')[0].strip()
            
            price = tree.xpath('//*[@id="classifiedDetail"]/div/div[2]/div[2]/h3/text()')[0].strip()

            title = tree.xpath('//*[@id="classifiedDetail"]/div/div[1]/h1/text()')[0].strip()

            ilan_no = ilan_no_list[x]

            xjson = {
            row2_key : row2_value,
            row3_key : row3_value,
            row4_key : row4_value,
            row5_key : row5_value,
            row6_key : row6_value,
            row7_key : row7_value,
            row8_key : row8_value,
            row9_key : row9_value,
            row10_key : row10_value,
            row11_key : row11_value,
            row12_key : row12_value,
            row13_key : row13_value,
            row14_key : row14_value,
            row15_key : row15_value,
            row16_key : row16_value,
            'Firma' : company,
            'Konum' : city,
            'Fiyat' : price,
            'İlan No' : ilan_no,
            'Başlık' : title
            }
            result_list.append(xjson)

    df = pd.DataFrame(result_list)
    df = df.set_index('İlan No')
    return df
