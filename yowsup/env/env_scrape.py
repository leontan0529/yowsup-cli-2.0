from bs4 import BeautifulSoup
import requests
import re
import wget
import time

url = 'https://www.whatsapp.com/android'
req = requests.get(url)
content = req.text
soup = BeautifulSoup(content, features="lxml")

def download(extract):
    tries = 3
    for i in range(tries):
        try:
            wget.download(extract, "WhatsApp.apk")
        except KeyError as e:
            if i < tries - 1:
                time.sleep(10)
                continue
            else:
                raise
        break

def scrappy(input):
    project_href = [i['href'] for i in soup.find_all('a', href=True)]

    for x in project_href:
        if re.search('WhatsApp.apk', x):
            link = x

    download(link)


scrappy(soup)
