import requests
import re
import sys

url= sys.argv[1]
response= requests.get(url)
html=response.text
links=re.findall(r'href="([^"]*)"', html)
links=list(set(links))

directory=open("urls","w") 
sub=open("sub","w")
files=open("files","w")

i=0
while(i<len(links)):
    line=links[i]
    print(line)
    if re.match(r'^(http|https|www).*\.com$',line):
         print("sub")
         status=requests.get(line)
         if status.status_code==200 :
            sub.write(url)
            i=i+1
         else:
            i=i+1
    
    elif re.match(r'.*\/$',line):
        print("this is a directory")
        directory.write(line)
        i=i+1
        
    elif re.match(r'.*\..*',line):
        print("this is a file")
        files.write(line)
        i=i+1
    
    

    else:
        i=i+1


directory.close()
files.close()
sub.close()


    
