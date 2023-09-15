import re

import httplib2
import mysql.connector
import requests
db = mysql.connector.connect(host='localhost', user='root', password='', database='test')
cur = db.cursor()
# h = httplib2.Http('.cache')
img = 'https://store77.net/upload/resize_cache/iblock/87d/220_180_0/87dcb45c342a0d1ca4e7e0bd6e703824.png'
# response, content = h.request(img)
# print(content)
# out = open('img/img1.png', 'wb')
# out.write(content)
# out.close()
# image = requests.get(img, verify=False).content
#
# out = open('img.png', 'wb')
# out.write(image)
a = open('img/img.png', 'rb')
print(a.read())
cur.execute(f"INSERT INTO `photos`(photo) VALUES({a.read()})")
# db.commit()
# def add_img(url):
#     image = requests.get(img, verify=False).content
#     a = url[url.rfind("/"):]
#     out = open('img'+a, 'wb')
#     out.write(image)
# add_img()



