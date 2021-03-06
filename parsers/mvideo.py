import requests
import smtplib
from bs4 import BeautifulSoup
import time

URL = 'https://www.mvideo.ru/products/fotoapparat-sistemnyi-sony-alpha7-iii-ilce-7m3-10014055'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/88.0.4324.150 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', class_="fl-h1").get_text().strip()

    price = soup.find('div', class_="fl-pdp-price__current").get_text()
    converted_price = int(price[:7].replace("\xa0", ""))

    if converted_price < 149990:
        send_mail()

    # print(title)
    # print(converted_price)


def send_mail():
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.ehlo()

    smtp_obj.login('Yourmail@.gmail.com', 'password')

    subject = 'Price fell down!'
    body = 'Check the link https://www.mvideo.ru/products/fotoapparat-sistemnyi-sony-alpha7-iii-ilce-7m3-10014055'
    msg = f"Subject: {subject}\n\n {body}"

    smtp_obj.sendmail(
        'carden.ruby@gmail.com',
        'denisovv89@yandex.ru',
        msg
    )

    print("HEY EMAIL HAS BEEN SENT!")

    smtp_obj.quit()


while True:
    check_price()
    time.sleep(86400)
