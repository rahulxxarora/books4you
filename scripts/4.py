import requests
from bs4 import BeautifulSoup
from datetime import datetime

f = open('search.txt','r')
f2 = open('results.txt','a')
f3 = open('title.txt','w')
word = f.readline()

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def junglee(k):
    flag=0
    url = "http://www.junglee.com/mn/search/junglee/ref=nav_sb_gw_noss?field-keywords=" + str(k) + "&rush=g&url=search-alias%3Daps"
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)
    f2.write("JUNGLEE\n") 

    for find,find2 in zip(ob.findAll('a',{'class':'title'}),ob.findAll('span',{'class':'price'})):
      title = find.text
      price = find2.text
      price = strip_non_ascii(price)
      price = price.replace('Rs.','Rupees')
      f2.write("Rupees " + price.strip().split('.')[0])
      f2.write("\n")
      f3.write(title)
      break

junglee(word)
f2.close()
f3.close()
