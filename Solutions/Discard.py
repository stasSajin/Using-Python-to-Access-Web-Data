import json
import urllib


url='http://python-data.dr-chuck.net/comments_42.json'
html=urllib.urlopen(url)
data=html.read()

info = json.loads(str(data))
#find everything between square brackets

#find the length of all counts
counts=len(info["comments"])
sum=0
for number in range(counts):
    x=info["comments"][number]["count"]
    sum=sum+x

print sum



