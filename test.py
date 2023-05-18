import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen, Request


my_list = []

def ParserUkrNet():
    url = 'https://www.pravda.com.ua/'
    req = Request(url)
    response = urlopen(req)
    print(response.code)

    soup = BeautifulSoup(response, "html.parser")
    mydiv = soup.find("div", {"class": "article_content"})
    links = list(mydiv('a'))

    for i in links:
         if 'https://www.pravda.com.ua' + i['href'] not in my_list:
             my_list.append('https://www.pravda.com.ua' + i['href'])

ParserUkrNet()

for i in my_list:
    url = i
    req = Request(url)
    response = urlopen(req)
    print(response.code)

    soup = BeautifulSoup(response, "html.parser")






















