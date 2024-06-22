from urllib.request import urlopen
from googlesearch import search
from bs4 import BeautifulSoup
import requests
links=[]
f=open("data.txt","r")
kk=f.read()
f.close()
query =kk
mydict=dict()
for i in search(query, tld="co.in", num=2, stop=10, pause=3):
    links.append(i)
#print(links) 
try:

    for i in links:
        request_result=requests.get(i)
        html=urlopen(i).read()
        soup= BeautifulSoup(html, features="html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
       # print(text)
        mydict[i]=text

    # print(mydict)
except:
    pass
print(mydict)