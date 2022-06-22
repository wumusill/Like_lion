import requests
from bs4 import BeautifulSoup

url = "http://wwww.daum.net"
response = requests.get(url)

# print(response)     # Response [200]
# print(response.text)      # html

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)