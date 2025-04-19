import requests
from bs4 import BeautifulSoup
import re

# https://www.mcdfoodforthoughts.com/

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
        }

url = 'https://www.mcdfoodforthoughts.com/'
response = requests.get(url, headers=headers)

# print headers returned
print(response.headers)

# add returned headers to a dictionary from the set-cookie under the cookie header
cookies = response.headers['set-cookie']
# remove the path and expires from the cookies
cookies = re.sub(r'Path=.*?; ', '', cookies)
headers.update({
    'cookie': cookies
})

print(headers)

response = requests.get(url, headers=headers)
print(response.text)
