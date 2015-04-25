from django.shortcuts import render
from django.http import HttpResponse
import os
import time 

def search_form(request):
    return render(request,'one/search_form.html')

def search(request):
    if 'q' in request.GET:
        f = open('search.txt','w')
        f.write(request.GET['q'])
        f.close()
        os.system("python scripts/comparator.py")
        f2 = open('results.txt','r')
        a = []
        b = []
        c = []
        ctr = 0
        check = 0
        time.sleep(1.5)
        while 1:
            ans = ""
            temp = f2.readline()
            if temp and temp!=' ':
               ans = ans + temp + "\n"
               if check==0:
                  a.append(ans)
                  check = check + 1
               elif check==1:
                  b.append(ans)
                  check = 0
               ctr = ctr + 1
               if ctr==10:
                  break
        f2.close()
        ans = ""
        f3 = open('title.txt','r')
        ans = f3.readline()
        c.append(ans)
        f3.close()
        d = zip(a,b)
        return render(request,'one/display.html',{'title':c,'names':d})
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
