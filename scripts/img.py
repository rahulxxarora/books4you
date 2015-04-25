import requests
from bs4 import BeautifulSoup

f = open('search.txt','r')
word = f.readline()
word = word.replace(' ','+')
word = word.replace('\n','')
f.close()

def fun(k):
   flag = 0
   url = "http://www.flipkart.com/search?q=" + str(k) + "&as=off&as-show=on&otracker=start"
   page = requests.get(url)
   src = page.text
   ob = BeautifulSoup(src)

   for div in ob.findAll('div',{'class':'lu-image'}):
      download = div.find('a')['href']
      download =  "http://www.flipkart.com" + download
      flag = 1
      break

   if flag==1:
      page2 = requests.get(download)
      src2 = page2.text
      ob2 = BeautifulSoup(src2)

      for div2 in ob2.findAll('div',{'class':'imgWrapper'}):
         download = div2.find('img')['data-src']
         break

      r = requests.get(download)
      f2 = open('static/images/pic.jpg','w')
      f2.write(r.content)
      f2.close()

   else:
      for div in ob.findAll('div',{'class':'pu-visual-section'}):
         download = div.find('a')['href']
         download =  "http://www.flipkart.com" + download
         flag = 1
         break

      page2 = requests.get(download)
      src2 = page2.text
      ob2 = BeautifulSoup(src2)

      for div2 in ob2.findAll('div',{'class':'imgWrapper'}):
         download = div2.find('img')['data-src']
         break

      r = requests.get(download)
      f2 = open('static/images/pic.jpg','w')
      f2.write(r.content)
      f2.close()

fun(word)
