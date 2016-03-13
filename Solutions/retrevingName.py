import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
html = urllib.urlopen(url).read()


# Retrieve all of the anchor tags
repeats=1
while repeats<8:
    soup = BeautifulSoup(html)
    tags = soup('a')
    count=0
    for tag in tags:
        if count==18:
            break
        url=tag.get('href',None)
        count=count+1
    print url
    html = urllib.urlopen(url).read()
    repeats=repeats+1
 




