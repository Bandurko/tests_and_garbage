import requests
from bs4 import BeautifulSoup
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# Задаем нужный район города
distr = 'Первомайский'
# Задаем площадь квартиры (кв. м)
flat_area = 45
# Задаем кол-во комнат в квартире
flat_rooms = 2

floats = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36"
}


for i in range(0, 3): # Задаем количество страниц сайта Циан со ссылками на квартиры

    # if flat_rooms == 1:
    #     r = '&room1=1'
    # elif flat_rooms == 2:
    #     r = '&room2=1'
    # elif flat_rooms == 3:
    #     r = '&room3=1'
    # elif flat_rooms == 4:
    #     r = '&room4=1'
    # elif flat_rooms >= 5:
    #     r = '&room5=1'

    url = f'https://vladivostok.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&offer_type=flat&p={i}&region=4701&room1=1&room2=1&room3=1&room4=1&room5=1&type=4'
    # url = f'https://vladivostok.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&offer_type=flat&p={i}&region=4701{r}&type=4'

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

with open('links.txt', 'w', encoding='utf-8') as file: # Создаем файл с ссылками на квартиры (построчно)
    for line in floats:
        file.write(f'{line}\n')

# ======================

with open('links.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    data_flats = []
    count = 0

    area = []
    rooms = []
    price = []

    for line in lines: # Построчно считывем ссылки из файла
        print(line)
        q = requests.get(line, headers=headers)
        result = q.text

        soup = BeautifulSoup(result, 'lxml')

        print(q.status_code) # Печатаем ответ сервера на запрос

        address = soup.find('meta', property='og:description') # Парсим полный адрес

        # ==================

        words = address['content'].split()  # Парсим район в котором находится квартира
        find_word = "р-н"
        index_word = -1
        if find_word in words:
            index_word = words.index(find_word)
        district = (words[index_word + 1][:-1:])


        if district == distr: # Определяем совпадает-ли район, где находится квартира с заданным айоном


            rooms_and_area = soup.find('div', {'data-name': 'OfferTitleNew'})

            for el in rooms_and_area:
                title = el.text.replace(" ", "")

                # print(title)

                if "Продается" in title: # Определяем кол-во комнат
                    idk1 = title[title.find("Продается") + 9:]
                    r = int(idk1[:idk1.find("-")])
                    rooms.append(r) # Добавляем кол-во комнат в список
                else:
                    continue

                if "квартира," in title: # Определяем площадь квартиры
                    idk2 = title[title.find("квартира,") + 9:]
                    a = float((idk2[:idk2.find("м²")]).replace(',', '.'))
                    area.append(a) # Добавляем площадь квартиры в список
                else:
                    continue

            elements_with_class_example = soup.find_all('div', {'data-name': 'ObjectFactoidsItem'})

            for element in elements_with_class_example:
                dat = element.text.replace(" ", "")

                # print(dat)

            price_parse = (soup.find('div', {'data-testid': 'price-amount'})).text[:-2:]

            p = int("".join(price_parse.split()))
            price.append(p)

            # print(price.text[12:-5:])
            # time.sleep(1)

        else:
            continue

        count += 1
        time.sleep(3)
        print(f'#{count}: {line} is done!')

        if count % 11 == 0: # "Защита" от определения парсинга
            time.sleep(10)
        else:
            continue

# print(area)
# print(rooms)
# print(price)
print('\n ========================== \n')


# ========== LinearRegression ============


# Площадь квартир в квадратных метрах
X_area = np.array(area)
# Количество комнат в квартире
X_rooms = np.array(rooms)
# Цены на недвижимость
y = np.array(price)
# Создаем объект модели линейной регрессии
model = LinearRegression()
# Обучаем модель на данных
# Объединяем два предиктора в одну матрицу
X = np.column_stack((X_area, X_rooms))
model.fit(X, y)
# Теперь модель обучена и может делать прогноз
# Давайте спрогнозируем цену для квартиры заданной площади и кол-ва комнат
# Задаем площадь квартиры (смотри в начале кода)
house_area = flat_area
# Задаем кол-во комнат в квартире (смотри в начале кода)
house_rooms = flat_rooms
predicted_price = model.predict(np.array([[house_area, house_rooms]]))
print(f'Прогнозируемая цена квартиры площадью {house_area} кв. метров и {house_rooms} комнатами(ой): {predicted_price[0]:.2f} руб.')