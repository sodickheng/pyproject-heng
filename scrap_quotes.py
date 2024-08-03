import requests
from bs4 import BeautifulSoup
import csv

URL = "http://quotes.toscrape.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
quotes = soup.find_all("div", class_="quote")

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        writer.writerow([text, author])

print("Quotes have been saved to quotes.csv")
