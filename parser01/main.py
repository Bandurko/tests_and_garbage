images = []

from bs4 import BeautifulSoup
import re
import requests
import time
import asyncio
from prisma import Prisma

db = Prisma()


cookies = {"srv_id":"owtiufI3Hg3Mgsa_.7uquCApI_ivrHsL21cJSXuqt0cnTmFCo_MGknwKrt36lNd52DvMsaLdTdrK_2tUcYxqz.OUkPMxfSbJlzao2BY71ne6AoYslE2wU0p3d19OXpGpA=.web",
"u": "32ehlssx.ugvk5m.ti1hdo0zpcg0",
"luri": "pskov",
"buyer_location_id": "645450",
"_gcl_au": "1.1.666925776.1711122003",
"tmr_lvid": "a783a9255c7c3dd4d551cec20fcdbefb",
"tmr_lvidTS": "1707669694413",
"_ga": "GA1.1.1255096629.1711122004",
"gMltIuegZN2COuSe": "EOFGWsm50bhh17prLqaIgdir1V0kgrvN",
"_ym_uid": "1707669695626606869",
"_ym_d": "1711122004",
"_ym_isad": "2",
"f": "5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a7b0d53c7afc06d0b2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112f12b79bbb67ac37d46b8ae4e81acb9fae2415097439d4047fb0fb526bb39450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264edd50b96489ab264ed46b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c84df0fd22b85d35fc34238d0bd261b67cb5ec09fa5c57cfa4e2921b48ec0870dee812aac015f93eb17c7721dca45217bc8bec9d424510011ba695b4034544747e2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fa69e329d33b579992b6c9122eda0b0e572da10fb74cac1eabb3ae333f3b35fe91de6c39666ae9b0d7312f8fecc8ca5e543486a07687daa291",
"ft": "vDDm41n9gXa8mqxSY7vrSwCqWrx6SMOTx3cyhiUNTDUYLF+kYAO89EngqAV2Rx3LmEbRebD7fWsTEyU140mIfCr9MDAkV68iuO0MZK0BIWRlzC2bucRfuIHKeJjTGfc72aPBnRg0empKQexNqRe5mhXRvBkkXvRsHoXhFaO0XLLZHOgrv7wR+98Ih59KR7HH",
"uuid": "9704319e4a3651fe%3A1",
"__upin": "qLl+vQ1HKgpVLqO9RI8I2Q",
"SEARCH_HISTORY_IDS": "1",
"v": "1711133803",
"_ga_WW6Q1STJ8M": "GS1.1.1711133814.3.0.1711133814.0.0.0",
"_ga_ZJDLBTV49B": "GS1.1.1711133814.3.0.1711133814.0.0.0",
"abp": "0",
"dfp_group": "26", "_buzz_fpc": "JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyU2F0JTJDJTIwMjIlMjBNYXIlMjAyMDI1JTIwMTklM0EzMSUzQTQ2JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnVmcCU1QyUyMiUzQSU1QyUyMjE1MzkxYTVhOTgzZWI4ZDUwYzQ2Y2YwMWEyMTU1ZWI0JTVDJTIyJTJDJTVDJTIyYnJvd3NlclZlcnNpb24lNUMlMjIlM0ElNUMlMjIxMjIuMCU1QyUyMiU3RCUyMiU3RA==",
"_buzz_aidata": "JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyU2F0JTJDJTIwMjIlMjBNYXIlMjAyMDI1JTIwMTklM0EzMSUzQTQ2JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnVmcCU1QyUyMiUzQSU1QyUyMnFMbCUyQnZRMUhLZ3BWTHFPOVJJOEkyUSU1QyUyMiUyQyU1QyUyMmJyb3dzZXJWZXJzaW9uJTVDJTIyJTNBJTVDJTIyMTIyLjAlNUMlMjIlN0QlMjIlN0Q=",
"tmr_detect": "0%7C1711136106079",
"sx": "H4sIAAAAAAAC%2F0zOS7KqMBAA0L1k7KA73Z2Pu8kXUOC9KxIUi73fugOr2MCp81HWOitiMDogCKKj9ymQCUwsaDWp60c1dVXzBlu%2F86tv9Iy3hcdXLQuM3VT68Wcq6qKKuqJF1FoLyHFRHjGnjMQUrKYMVDElDNVBlCBQvnJ%2B9e2dcH2I7F0CVzt4rHeRNkBtNJ1kRE18XFQBwEI%2BMpscSAhjLQYpcy3k0OivvO5mriLL3Q9zN2e7mOe7bv%2B3haf%2BZtbzGTTQn%2BylSiYoLjlXkvMpWqt9ABeZSaev%2FE88PsIwhi20WbsBbOq47fnelgxrPcngGPA4fgMAAP%2F%2FNneeh2kBAAA%3D",
"_ga_M29JC28873": "GS1.1.1711135902.3.1.1711136106.55.0.0"}

f = open("links.txt", "r", encoding="utf-8")

async def main():
    await db.connect()  # Connecting to database
    for line in f:
        response = requests.get(line[:-1], headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}, cookies=cookies)
        print("----------------------------------------------------------------------")
        print(f"parsed url {line[:-1]} with code {response.status_code}")
        if response.status_code != 200:
            print(f"status is {response.status_code} skipping...")
            continue

        soup = BeautifulSoup(response.content.decode("utf-8"), 'html.parser')

        elements_with_class_example = soup.find_all(class_=re.compile(r'^params-paramsList-'))

        images = []
        description = ""
        addres = ""
        price = 0
        etaz = 0
        ploshad = 0
        rooms = 1
        lat = 0
        lon = 0
        # Выведем найденные элементы

        for element in elements_with_class_example:
            dat = element.text.replace(" ", "")
            # print(dat)
            if "Количествокомнат" in dat:
                try:
                    rooms = float(dat[dat.find("Количествокомнат") + 17:dat.find("Количествокомнат") + 18])
                except Exception as e:
                    print(e)
            if "Этаж:" in dat:
                try:
                    idk = dat[dat.find("Этаж:") + 5:]
                    etaz = float(idk[:idk.find("из")])
                except Exception as e:
                    print(e)
            if "Общаяплощадь" in dat:
                try:
                    idk2 = dat[dat.find("Общаяплощадь") + 13:]
                    ploshad = float(idk2[:idk2.find("м²")])
                except Exception as e:
                    print(e)

        adress = soup.find_all(class_=re.compile(r'^style-item-map-wrapper'))
        for element in adress:
            try:
                print("lat:", lat := element.get('data-map-lat'))
                print("lon:", lon := element.get('data-map-lon'))
            except Exception as e:
                print(e)

        adress = soup.find_all(class_=re.compile(r'^style-item-address__string'))
        for element in adress:
            try:
                print("addres:", element.text)
                addres = element.text
            except Exception as e:
                print(e)

        adress = soup.find_all(class_=re.compile(r'^style-price-value-main'))
        for element in adress:
            try:
                price = element.find('span').get("content")
                print("price:", price)
                break
            except Exception as e:
                print(e)

        description = soup.find_all(class_=re.compile(r'^style-item-description-text'))
        for element in description:
            try:
                print("description:", element.text)
                description = element.text
            except Exception as e:
                print(e)

        if not description:
            description = soup.find_all(class_=re.compile(r'^style-item-description-html'))
            for element in description:
                try:
                    print("description:", element.text)
                    description = element.text
                except Exception as e:
                    print(e)

        photos = soup.find_all(class_=re.compile(r'^images-preview-previewImageWrapper'))
        for element in photos:
            try:
                image = element.find('img')
                images.append(str(image.get('src')))
            except Exception as e:
                print(e)

        print("rooms:", rooms)
        print("square:", ploshad)
        print("floor:", etaz)

        try:
            await db.record.create(data={"addres": addres,
                                         "description": description,
                                         "floor": int(etaz),
                                         "lat": float(lat),
                                         "lon": float(lon),
                                         "photos": '","'.join(images),
                                         "price": int(price),
                                         "rooms": int(rooms),
                                         "square": float(ploshad),
                                         "link": line[:-1]
                                         })
        except Exception as e:
            print(e)

        time.sleep(0.5)


asyncio.run(main())
