import contextlib 
from urllib.parse import urlencode
from urllib.request import urlopen  

def shorten_url(url): 

    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))     

    with contextlib.closing(urlopen(request_url)) as response:                       

        return response.read().decode('utf-8 ')                                       

ip=input("Enter url to shorten : ")

print(shorten_url(ip))
