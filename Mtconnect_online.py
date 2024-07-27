from bs4 import BeautifulSoup
import requests

# specify the URL of the XML data
url = "https://smstestbed.nist.gov/vds/current"

# fetch the data from the URL
response = requests.get(url)

# create a BeautifulSoup object to parse the XML data
# both below xml parser can be used after pip install lxml
#soup = BeautifulSoup(response.content, "lxml-xml")
soup = BeautifulSoup(response.content, "xml")

# find the elements with specific dataItemId attributes
element1 = soup.find(attrs={"dataItemId": "GFAgie01-dtop_2"})
element2 = soup.find(attrs={"dataItemId": "GFAgie01-X_2"})

# Check if elements are found and print their content
if element1:
    print(f'dataItemId : GFAgie01-dtop_2 = {element1.text}')
else:
    print("Element with dataItemId 'GFAgie01-dtop_2' not found.")

if element2:
    print(f'dataItemId : GFAgie01-X_2 = {element2.text}')
else:
    print("Element with dataItemId 'GFAgie01-X_2' not found.")