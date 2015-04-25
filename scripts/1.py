import requests
from bs4 import BeautifulSoup
from datetime import datetime

f = open('search.txt','r')
f2 = open('results.txt','a')
word = f.readline()

def flipkart(k):
    flag=0
    url = "http://www.flipkart.com/search?q=" + str(k) + "&as=off&as-show=on&otracker=start"
    page = requests.get(url)
    src = page.text
    ob = BeautifulSoup(src)
    f2.write("FLIPKART\n") 

    for find in ob.findAll('div',{'class':'pu-final fk-font-17 fk-bold'}):
      if flag==0:
         flag=1
      price = find.text
      price = price.replace('Rs.','Rupees')
      f2.write(price.strip())
      f2.write("\n")
      break
      
    if flag!=1:
      for temp in ob.findAll('div',{'class':'pu-final'}): 
         price = temp.text
         price = price.replace('Rs.','Rupees')
         f2.write(price.strip())
         f2.write("\n")
         break

flipkart(word)
f2.close()
