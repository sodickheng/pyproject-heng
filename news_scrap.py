import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.sg/Owala-FreeSip-Insulated-Stainless-BPA-Free/dp/B0C59CLN29?pd_rd_w=IlzG5&content-id=amzn1.sym.11079857-0102-48e6-9566-cd773a0fdaf4&pf_rd_p=11079857-0102-48e6-9566-cd773a0fdaf4&pf_rd_r=F1TTE6J6FBMK22VGH20E&pd_rd_wg=ZMACt&pd_rd_r=5b709d18-cbbc-4cdc-8106-e10a932b59d5&pd_rd_i=B0C59CLN29&ref_=oct_dx_dotd_B0C59CLN29&th=1"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
page = requests.get(url, headers=headers)
soup1 = BeautifulSoup(page.content,"html.parser" )
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id ="productTitle").get_text()
price = soup2.find(id ="corePriceDisplay_desktop_feature_div").get_text()
print(title.strip()[0:52])
print(price.strip()[0:7])

# webpage select inspect
#copy selector
#corePriceDisplay_desktop_feature_div
