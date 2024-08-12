import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import pandas as pd

def check_price():
    # connect the website
    url = ""

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content,"html.parser" )
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id ="productTitle").get_text()
    price = soup2.find(id ="corePriceDisplay_desktop_feature_div").get_text()

    today= datetime.date.today()

    # pandas dataframe
    df = pd.read_csv('/Users/heng/PycharmProjects/pythonProject/projects_online/amazon_scrap.csv')
    print(df)

    # append to file
    headers = ['Title', 'Price','Date']
    data = [title.strip()[24:52], price.strip()[0:7], today]
    with open('amazon_scrap.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        #writer.writerow(headers)  # only for first time write headers
        writer.writerow(data)

while True:
    try:
        check_price()
        time.sleep(5)
    except:
        print("an error occurs")

# Remark #
# webpage select inspect
# copy selector or element 
# corePriceDisplay_desktop_feature_div
