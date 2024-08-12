import requests
from bs4 import BeautifulSoup

url = ""

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

