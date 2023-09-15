import requests
from bs4 import BeautifulSoup
import re
from phone import phone
from connect import db


cur = db.cursor()


listphone = []
def get_info(URL):
    r = requests.get(URL, verify=False)
    context = r.text
    soup = BeautifulSoup(context, 'lxml')
    html_name = soup.find_all('h2', class_='bp_text_info bp_width_fix')
    for a in html_name:
        name = re.findall("name': '[^']{0,}", str(a))
        name = str(name).replace("name': '", "").replace('["', "").replace('"]', "")
        id = re.findall("id': '[^']{0,}", str(a))
        id = str(id).replace("id': '", "").replace('["', "").replace('"]', "")
        prince = re.findall("price': [0-9]{0,}", str(a))
        prince = str(prince).replace("price': ", "").replace('["', "").replace('"]', "")
        brand = re.findall("brand': '[^']{0,}", str(a))
        brand = str(brand).replace("brand': '", "").replace('["', "").replace('"]', "")
        fone = phone(id, name, prince, brand)
        listphone.append(fone)

def add_values():
    for phone in listphone:
        cur.execute(f"INSERT INTO `phones`(`id`, `name`, `prince`, `brand`) VALUES('{phone.id}', '{phone.name}',"
                    f" '{phone.prince}', '{phone.brand}')")

for i in range(1,27):
     get_info(f"https://store77.net/telefony/?PAGEN_1={i}")


add_values()
print(len(listphone))
#add_values()
db.commit()