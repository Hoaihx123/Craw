from bs4 import BeautifulSoup
import requests
import re
import httplib2

URL_TEMPLATE = 'https://store77.net/telefony_apple/'
r = requests.get(URL_TEMPLATE)
context = r.text
soup = BeautifulSoup(context, 'lxml')
html_name = soup.find_all('h2', class_='bp_text_info bp_width_fix')
#print(html_name)
urls = []
for a in html_name:
    link = re.findall("href=[^\s]{0,}", str(a))
    link = str(link[0]).replace('href="', "").replace('"', "")
    urls.append("https://store77.net"+link)

def get(url):
    req = requests.get(url)
    context = req.text
    soup = BeautifulSoup(context, 'lxml')



