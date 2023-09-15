import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
# db = mysql.connector.connect(host='localhost', user='root', password='', database='labbs4')
#
# cur = db.cursor()
list_link = []
#
#
# cur.execute('SELECT `id` FROM `phones` ')
# list_id = cur.fetchall()


def get_photo(URL):
    r = requests.get(URL, verify=False)
    context = r.text
    soup = BeautifulSoup(context, 'lxml')
    html_name = soup.find_all('div', class_='bp_product_img')
    for a in html_name:
        link = re.findall('src="[^"]{0,}', str(a))
        link = str(link).replace("['src=", "").replace("']", "").replace('"', "")
        if link[0] == "/":
            link = "https://store77.net"+link
        list_link.append(link)
for i in range(1, 2):
    URL_TEMPLATE = "https://store77.net/telefony/?PAGEN_1=" + str(i)
    get_photo(URL_TEMPLATE)
def add_img(url):
    image = requests.get(url, verify=False).content
    a = url[url.rfind("/"):]
    print(a)
    out = open('img'+a, 'wb')
    out.write(image)
    img = open('img'+a, 'rb')
    # cur.execute(f"INSERT INTO photos (id, img) VALUES('{id}', {img.read()})")
    # db.commit()

# i = 0
# for link in list_link:
#     id = list_id[i]
#     add_img(link, id)
#     i = i+1
# print(list_link)
add_img('https://store77.net/upload/w247/imageCache/716/f5c/8b6476ac043df649c341b6dc4e9f0b79.png',)