import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.sg/Owala-FreeSip-Insulated-Stainless-BPA-Free/dp/B0C59CLN29?pd_rd_w=IlzG5&content-id=amzn1.sym.11079857-0102-48e6-9566-cd773a0fdaf4&pf_rd_p=11079857-0102-48e6-9566-cd773a0fdaf4&pf_rd_r=F1TTE6J6FBMK22VGH20E&pd_rd_wg=ZMACt&pd_rd_r=5b709d18-cbbc-4cdc-8106-e10a932b59d5&pd_rd_i=B0C59CLN29&ref_=oct_dx_dotd_B0C59CLN29&th=1"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

# Fetch the product title
try:
    title = soup.find(id="productTitle").get_text().strip()
    print(title[:52])  # Print the first 52 characters of the title
except AttributeError:
    print("Product title not found.")

# Fetch the price
try:
    price = soup.find("span", {"class": "a-price-whole"}).get_text().strip()
    print(price)
except AttributeError:
    print("Product price not found.")

