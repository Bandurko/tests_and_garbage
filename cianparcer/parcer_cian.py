import requests
from bs4 import BeautifulSoup
import time
import json

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

with open('floats.txt', 'w', encoding='utf-8') as file:
    for line in floats:
        res = file.write(f'{line}\n')

# ======================

with open('floats.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    data_flats = []
    count = 0
    for line in lines:
        print(line)
        q = requests.get(line, headers=headers)
        result = q.text

        soup = BeautifulSoup(result, 'lxml')

        print(q.status_code)

        address = soup.find('meta', property='og:description')
        price = soup.find('div', {'data-name': 'OfferFactItem'})

        # print(price.text[12:-5:])
        # time.sleep(1)

        data = {
            'address': address['content'],
            'price': price.text[12:-5:],
        }

        count += 1
        print(f'#{count}: {line} is done!')

        data_flats.append(data)

        with open('flats.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_flats, json_file, indent=4, ensure_ascii=False)
            
