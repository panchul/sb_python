
# urllib, urllib2, urllib3
# https://docs.python.org/3/howto/urllib2.html

#
#	$ python -m pip install urllib3
#

# https://www.facebook.com/panchul/videos/10156791602064936
import re
import requests
import urllib.request

link = input("url: ")
#link = "https://www.facebook.com/panchul/videos/10156791602064936"
html = requests.get(link)

try:
    url = re.search('hd_src:"(.+?)"',html.text)[1]
    print("hd")
except:
    url = re.search('sd_src:"(.+?)"',html.text)[1]
    print("sd")

print(f"downloading {url}...")
urllib.request.urlretrieve(url,"test.mp4")
print("Done")
