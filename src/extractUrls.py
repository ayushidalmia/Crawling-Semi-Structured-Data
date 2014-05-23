#it takes as input the html files and returns the following attributes
# Business Id, Name, Homepage Url and Phone Number

#import required libraries
import re
from collections import defaultdict

#initialise output variables
url=defaultdict(lambda: 'NULL')
name=defaultdict(lambda: 'NULL')
phone=defaultdict(lambda: 'NULL')

#find attributes
for i in range(1,2001):

    #read file
    print i
    fileName='Dataset\\business'+str(i)+'.html'
    f=open(fileName,'r')

    #for every file find the required urls
    for line in f:
        if 'bizUrl' in line:
            nextLine=f.next()
            dirtyUrl=nextLine[nextLine.index('url=')+4:nextLine.index('src')-5]
            url[i]=dirtyUrl.replace('%2F','/').replace('+',' ').replace('%3A', ':').replace('%7C','|')
        if 'og:title' in line:
            words=line.strip().split("=")
            name[i]=words[2][1:-2]
            name[i]=name[i].replace('&#39;','\'').replace('&amp;','&') 
        if 'bizPhone' in line:
            words=line.strip().split(">")
            phone[i]=words[1][:-6]
            
    f.close()

#write into file
data=[]
for key in sorted(name.keys()):
    data.append(str(key)+"\t"+name[key]+"\t"+url[key]+"\t"+phone[key])
f=open("extractedUrl.txt",'w')
f.write("\n".join(data))
f.close()


   

