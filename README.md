# Ethical
import requests
import re
import sys

After importing these libraries you use sys.argv[with argument nb] to get the argument placed in the terminal

To get the html code, use requests.get(url above)

Use re.findall to find all the lines containing href then put them in a set to remove the duplicates then reput them in a list to access the information with list[i]

Then open 3 files for each category of subdomains, directories and files

Loop throught the hrefs line then try to find the lines that have a subdomain pattern      ^(http|https|www).*\.com$ or a directory pattern .*\/$ or a file pattern .*\..*

If it is a subdomain you need to check if this subdomain is available so use status=requests.get(url)
then if status.status_code==200 then it is a success save it in a file 

close all the files 
