import requests
from bs4 import BeautifulSoup
from datetime import datetime

f = open('search.txt','r')
f2 = open('results.txt','a')
word = f.readline()

def uread(k):
    url = "http://www.infibeam.com/search?q=" + str(k)
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)
    f2.write("INFIBEAM\n") 

    for find in ob.findAll('span',{'class':'final-price'}):
      price = find.text
      price = price.replace('Rs.','Rupees')
      f2.write(price.strip())
      f2.write("\n")
      break

uread(word)
f2.close()
