import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    tag=str(tag.contents[0])
    sum=sum+int(tag)

print sum


