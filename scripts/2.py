import requests
from bs4 import BeautifulSoup
from datetime import datetime

f = open('search.txt','r')
f2 = open('results.txt','a')
word = f.readline()

def amazon(k):
    url = "http://www.amazon.in/s/ref=nb_sb_noss/276-0458272-7880320?url=search-alias%3Daps&field-keywords=" + str(k)
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)
    f2.write("AMAZON\n")   

    for find in ob.findAll('span',{'class':'a-size-base a-color-price s-price a-text-bold'}):
      price = find.text
      price = price.replace('Rs.','Rupees')
      f2.write("Rupees " + price.strip().split('.')[0])
      f2.write("\n")
      break

amazon(word)
f2.close()
