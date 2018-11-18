from bs4 import BeautifulSoup
import requests
import csv
import re
import sys

arr=[]
site_add = "https://www.hindustantimes.com"
a=BeautifulSoup(requests.get(site_add).text, "lxml")
for x in a.find_all(re.compile('^h[1-6]$')):

    arr.append(x.text.strip())
   
with open('head_line.csv','w') as f:
    
        ryt= csv.writer(f)
        for i in arr:
           ryt.writerow([i])

with open('head_line.csv','r')as q:
    read=csv.reader(q) 
    for y in read:
       print(y)

 
