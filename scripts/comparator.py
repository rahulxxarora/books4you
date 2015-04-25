import os
f = open('results.txt','w')
f.close()
os.system('python scripts/5.py &')
os.system('python scripts/4.py &')
os.system('python scripts/3.py &')
os.system('python scripts/2.py &')
os.system('python scripts/1.py &')
os.system('python scripts/img.py')
