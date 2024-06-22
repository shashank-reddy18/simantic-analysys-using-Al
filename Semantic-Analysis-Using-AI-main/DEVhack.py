
from difflib import *
import nltk
from nltk.corpus import *
from nltk.util import Index
import pytesseract 
# from flaskapp import flsk
def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None

import os
import difflib
k=dict()
directory = 'images'
 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        pytesseract.pytesseract.tesseract_cmd=r'C:\Users\pooji\OneDrive\Desktop\final\tess\tesseract.exe'
        # q=pytesseract.image_to_string(rf'C:\Users\pooji\OneDrive\Desktop\final\{f}').strip()
        q=pytesseract.image_to_string(rf'C:\Users\pooji\OneDrive\Desktop\final\{f}').strip()
        k[f]=q
print(k)
print()
print()
print()
print()

# C:\Users\pooji\OneDrive\Desktop\hackit\images

#
#
#







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
for i in search(query, tld="co.in", num=10, stop=10, pause=2):
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
    #    print(text)
        mydict[i]=text

    # print(mydict)
except:
    pass
print(mydict)

yd=list(mydict.values())
n=0

liststr=list(k.values())
# print(type(liststr[0]))
# for i in liststr:
#     ss+=i

for i in liststr:
    for j in yd:
        # file1=open('test1.txt').readlines()
        # file1=file1.split()
        # file2=open('test2.txt').readlines()
        # file2=file2.split()
        # str1=''
        # str2=''
        # for i in file1:
        #     str1+=i.strip('\n')

        # for i in file2:
        #     str2+=i.strip('\n')
        y1=''
        file1=i
        file2=j
        y1+=i+j

        plag=SequenceMatcher(None,file1,file2).ratio()
        # print(plag,file1,file2)
        synonyms=[[] for i in range(  len(file1) if len(file1)>len(file2) else len(file2)  ) ] 
        context=0
        n=0

        for i in file1:
            for syn in wordnet.synsets(i):
                for lemma in syn.lemmas():
                        synonyms[n].append(lemma.name())
            n+=1
                
        syndict={i:list(set(v)) for i,v in zip(file1,synonyms)}
        parap=0
        valuelist=list(syndict.values())

        def relist(j):
            for i in valuelist:
                # print(i)
                if j in i:
                    return i
            return []


        for i in set(file1):
            if i in relist(i):
                parap+=1
        # print(parap)

        for i in set(file1):
            if i in file2:
                context+=1
    print('total copied words :',context,'\nparahrased similarity is:',parap,'\npercentile of similiraty is',plag*100,'%','of file' ,'\nfrom website',get_key_from_value(mydict,j),'\n\n\n')
    if(plag>0.1):
            #  first_file = "text_file.txt"
            # second_file="compare_file.txt"
            first_file_lines=file1.split('\n')
            # print(first_file_lines)
            second_file_lines=file2.split('\n')
            diffrence=difflib.HtmlDiff().make_file(first_file_lines,second_file_lines)
            diffrence_report = open('diffrence_report.html','w+')
            diffrence_report.write(diffrence)
            diffrence_report.close()









#
#
#
ss=''


liststr=list(k.values())
# print(type(liststr[0]))
# for i in liststr:
#     ss+=i

for i in liststr:
    for j in liststr[liststr.index(i):]:
        # file1=open('test1.txt').readlines()
        # file1=file1.split()
        # file2=open('test2.txt').readlines()
        # file2=file2.split()
        # str1=''
        # str2=''
        # for i in file1:
        #     str1+=i.strip('\n')

        # for i in file2:
        #     str2+=i.strip('\n')
        
        file1=i
        file2=j
        y1+=i+j

        plag=SequenceMatcher(None,file1,file2).ratio()
        # print(plag,file1,file2)
        synonyms=[[] for i in range(  len(file1) if len(file1)>len(file2) else len(file2)  ) ] 
        context=0
        n=0

        for i in file1:
            for syn in wordnet.synsets(i):
                for lemma in syn.lemmas():
                        synonyms[n].append(lemma.name())
            n+=1
                
        syndict={i:list(set(v)) for i,v in zip(file1,synonyms)}
        parap=0
        valuelist=list(syndict.values())

        def retlist(j):
            for i in valuelist:
                # print(i)
                if j in i:
                    return i
            return []


        for i in set(file1):
            if i in retlist(i):
                parap+=1
        # print(parap)

        for i in set(file1):
            if i in file2:
                context+=1

        print('total copied words :',context,'\nparahrased similarity is:',parap,'\npercentile of similiraty is',plag*100,'%','of file' ,'\n\n\n')
        # print(file1,file2)


        #
        #
        #
        if(plag>0.0):
            #  first_file = "text_file.txt"
            # second_file="compare_file.txt"
            first_file_lines=file1.split('\n')
            # print(first_file_lines)
            second_file_lines=file2.split('\n')
            diffrence=difflib.HtmlDiff().make_file(first_file_lines,second_file_lines)
            diffrence_report = open('nce_report.html','w+') 
            diffrence_report.write(diffrence)
            diffrence_report.close()

#
#
#

print('#'*30*20)
print('this is the frequecy count of the word and the meaning ')
#find the frequenct
wordlist=[i for i in file1+file2]
# wordlist=' '.join(wordlist)
set(wordlist)
for i in set(wordlist):
    print(i,'::',y1.count(i) )