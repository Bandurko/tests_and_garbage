import requests
import re
from bs4 import BeautifulSoup
import time
import json



distr = 'Первомайский'

floats = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36"
}


for i in range(0, 1):
    url = f'https://vladivostok.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&offer_type=flat&p={i}&region=4701&room1=1&room2=1&type=4'

    q = requests.get(url=url, headers=headers)
    result = q.text

    soup = BeautifulSoup(result, 'lxml')
    links = soup.find_all(class_='_93444fe79c--link--eoxce')

    for link in links:
        float_page_link = link.get('href')
        floats.append(float_page_link)

    # print(floats)
    # time.sleep(1)

sorter = []
for link in floats:
    if link not in sorter:
        sorter.append(link)

floats = sorter

# print(floats)
# time.sleep(1)

with open('links.txt', 'w', encoding='utf-8') as file:
    for line in floats:
        res = file.write(f'{line}\n')

# ======================

with open('links.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    # distr = 'Первомайский'
    data_flats = []
    count = 0
    for line in lines:
        print(line)
        q = requests.get(line, headers=headers)
        result = q.text

        soup = BeautifulSoup(result, 'lxml')

        print(q.status_code)

        address = soup.find('meta', property='og:description')

        elements_with_class_example = soup.find_all('div', {'data-name': 'ObjectFactoidsItem'})

        for element in elements_with_class_example:
            dat = element.text.replace(" ", "")

            # print(dat)

            if "Этаж" in dat:
                idk = dat[dat.find("Этаж") + 4:]
                etaz = int(idk[:idk.find("из")])
            else:
                continue

        words = address['content'].split()
        find_word = "р-н"
        index_word = -1
        if find_word in words:
            index_word = words.index(find_word)
        district = (words[index_word + 1][:-1:])

        price_parse = (soup.find('div', {'data-name': 'OfferFactItem'})).text[12:-5:]

        price = int("".join(price_parse.split()))

        # print(price.text[12:-5:])
        # time.sleep(1)

        if district == distr:

            data = {
                'address': address['content'],
                'district': district,
                'etaz': etaz,
                'price': price,
            }
        else:
            continue

        count += 1
        print(f'#{count}: {line} is done!')

        data_flats.append(data)

        with open('flats.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_flats, json_file, indent=4, ensure_ascii=False)
            
