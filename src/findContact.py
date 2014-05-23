#libraries
import urllib2
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import traceback
import sys

#output intialisation
dict_email=defaultdict(lambda: 'NULL')
dict_contactUrl=defaultdict(lambda: 'NULL')
dict_data={}
#find email
#This function takes the entire webpage and searches for the email addresses given by the
#formulated regular expression.

def validate_email(text):
    reg_ex=re.compile(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+', re.IGNORECASE)
    temp=re.findall(reg_ex,str(text))
    if len(temp)>=1:
        email=list(set(temp))
    return email


#find contactUrl
#This function takes the entire webpage and searches for the contact page given by the
#formulated regular expression in the href of anchor tags. If the contact word is not
#there in the href,it checks the text and if found captures the url

def validate_contactUrl(text):    
    hrefTags=text.find_all('a')
    regEx=re.compile(r'.*contact.*',re.IGNORECASE)
    for key in range(0,len(hrefTags)):
        searchText=re.findall(regEx,str(hrefTags[key].get('href')))
        if searchText:
             contactUrl=hrefTags[key].get('href')
             break;
        else:
            text="".join(hrefTags[key](text=True))
            searchText=re.findall(regEx,text.encode('utf-8'))
            if searchText:
                contactUrl=hrefTags[key].get('href')
                break;
    return contactUrl
            
data=[]
data1=[]

#read file
f=open("extractedUrl.txt",'r')
for line in f:
    
    words=line.strip().split('\t')
    words[0]=int(words[0])
    print words[0]
    
    dict_data[words[0]]=line.strip()

    #if homepage url exists
    if words[2]!='NULL':
        
        try:
            #read content of homepage
            urlContent = urllib2.urlopen(words[2]).read()
            soup = BeautifulSoup(urlContent)

            #find contact
            ContactUrl=validate_contactUrl(soup)
            dict_contactUrl[words[0]]=ContactUrl
            if ContactUrl is not None and 'http' not in ContactUrl and ContactUrl!='NULL':
                dict_contactUrl[words[0]]=words[2]+'/'+ContactUrl

            #if contact page present find email from the contact page    
            if ContactUrl is not None and ContactUrl!='NULL':
                try:
                    urlContent = urllib2.urlopen(dict_contactUrl[words[0]]).read()
                    soupcontact = BeautifulSoup(urlContent)
                    dict_email[words[0]]=validate_email(soupcontact)
                    if dict_email=='NULL':
                        #if email not found in contact page search in homepage
                        dict_email[words[0]]=validate_email(soup)
                except Exception as e:
                    continue
                
        except Exception as e:
            continue
    

#write into file
data=[]
for key in sorted(dict_data.keys()):
    words=dict_data[key].split("\t")
    if dict_email[key]!='NULL':
        data.append("business"+str(key)+"\t"+words[1]+"\t"+words[3]+"\t"+words[2]+"\t"+str(dict_contactUrl[key])+"\t"+"\t".join(dict_email[key]))
    else:
        data.append("business"+str(key)+"\t"+words[1]+"\t"+words[3]+"\t"+words[2]+"\t"+str(dict_contactUrl[key])+"\t"+str(dict_email[key]))
f=open("result.txt",'w')
f.write("\n".join(data))
f.close()



        
        
            
                    
        
