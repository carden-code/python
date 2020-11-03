# Дополнить метод status, который будет возвращать JSON object с ключами и значениями:
#
# status - true
# name - произвольное имя вашего мессенджера
# time - текущее время на сервере в виде строки

from flask import Flask, jsonify
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World! <a href='/stats'>Статистика</a>"


@app.route("/stats")
def stats():
    now = datetime.datetime.now()

    snt = {
        'messages_count': 500,
        'status': True,
        'name': 'samolet',
        'time': str(now)
    }
    return jsonify(snt)


app.run()
