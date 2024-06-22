from difflib import *
import nltk
from nltk.corpus import *

# file1=open('test1.txt').readlines()
# file1=file1.split()
# file2=open('test2.txt').readlines()
# file2=file2.split()
str1=''
str2=''
for i in file1:
    str1+=i.strip('\n')

for i in file2:
    str2+=i.strip('\n')

file1=str1
file2=str2


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

print('total copied words :',context,'\nparahrased similarity is:',parap,'\npercentile of similiraty is',plag*100,'%')
# print(file1,file2)