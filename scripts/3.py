import requests
from bs4 import BeautifulSoup
from datetime import datetime

f = open('search.txt','r')
f2 = open('results.txt','a')
word = f.readline()

def bookadda(k):
    url = "http://www.bookadda.com/general-search?searchkey=" + str(k)
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)
    f2.write("BOOKADDA\n")   

    for find in ob.findAll('span',{'class':'new_price'}):
      price = find.text
      price = price.replace('Rs.','Rupees ')
      f2.write(price.strip())
      f2.write("\n")
      break

bookadda(word)
f2.close()
