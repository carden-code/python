import time

db = [
    {
        'text': 'Привет',
        'name': 'Slava',
        'time': time.time()
    },
    {
        'text': 'Привет, Slava',
        'name': 'Kola',
        'time': time.time()
    },
    {
        'text': 'Как дела?',
        'name': 'Slava',
        'time': time.time()
    }
]


def send_massage(text, name):
    db.append({
        'text': text,
        'name': name,
        'time': time.asctime()
    })


def get_messages(after):
    filtered_db = []
    for message in db:
        if message['time'] > after:
            filtered_db.append(message)
    return filtered_db
