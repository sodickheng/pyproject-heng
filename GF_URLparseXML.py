import urllib.request
import xml.etree.ElementTree as ET

# specify the URL of the XML file
url = 'https://smstestbed.nist.gov/vds/current'

# download the XML file and store it in a variable
xml_data = urllib.request.urlopen(url).read()

# parse the XML data using ElementTree
tree = ET.fromstring(xml_data)

# iterate over the elements in the XML file and print their text
for element in tree.iter():
    print(element.tag, element.text)
    
