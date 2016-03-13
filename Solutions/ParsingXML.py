import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter URL:')
uh = urllib.urlopen(address)
data = uh.read()
commentinfo = ET.fromstring(data)
lst = commentinfo.findall('.//comment')

sum=0
for item in lst:
    a=item.find('count').text
    sum=sum+int(a)

print sum