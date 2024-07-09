# request URL and use beautiful soup to find parse xml data directly from MTconnect GF xml live sample file
# pip3 install lxml to read "lxml-xml"

from bs4 import BeautifulSoup
import requests

# specify the URL of the XML data
url = "https://smstestbed.nist.gov/vds/current"

# fetch the data from the URL
response = requests.get(url)

# create a BeautifulSoup object to parse the XML data
soup = BeautifulSoup(response.content, "lxml-xml")

# find all elements with a specific tag
#elements = soup.find_all("EmergencyStop")[0]
elements1 = soup.find_all(dataItemId="GFAgie01-dtop_2")[0]
elements2 = soup.find_all(dataItemId="GFAgie01-X_2")[0]


# iterate over the elements and extract data
for element in elements1:
    # do something with the element
    #print(element)
    print(f'dataItemId : GFAgie01-dtop_2 = {element}')

for element in elements2:
    print(f'dataItemId : GFAgie01-X_2 = {element}')