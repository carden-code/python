import json
import time
from datetime import datetime

import requests

after = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages?after=' + str(after)
    )

    # Подсчёт сообщений
    resp = requests.get('http://127.0.0.1:5000/messages')
    arr = resp.json()['messages']

    all_mes = 0
    for mes in arr:
        all_mes += 1
        if mes == arr[-1]:
            break
    # Подсчёт уникальный имён на сервере
    name = []
    for i in arr:
        name.append(i['name'])
    uniq_name = set(name)

    for message in response.json()['messages']:
        dt = datetime.fromtimestamp(message['time'])
        dt = dt.strftime('%H:%M:%S')
        print('Всего сообщений на сервере:', all_mes)
        print('Колличество участников чата:', len(uniq_name))
        print()
        print(dt, message['name'])
        print(message['text'])
        print()

        after = message['time']

    time.sleep(1)
