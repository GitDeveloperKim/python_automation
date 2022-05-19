import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

with urllib.request.urlopen("http://www.naver.com") as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find_all('a'))
