import time

print('Hello World!')

# list
l = [1, 2, 3, 'abc', [1, 2, 3]]

# dict
d = {
    'text': 'Привет',
    'name': 'Nick',
    'time': '20:00'
}

db = [
    {
        'text': 'Привет',
        'name': 'Nick',
        'time': time.time(),
        'count': 0
    }, {
        'text': 'Привет, Nick',
        'name': 'Jane',
        'time': time.time(),
        'count': 0
    }, {
        'text': 'Как дела?',
        'name': 'Nick',
        'time': time.time(),
        'count': 0
    }
]


def send_message(text, name):
    db.append({
        'text': text,
        'name': name,
        'time': time.time()
    })


def get_messages(after):
    filtered_db = []
    for message in db:
        if message['time'] > after:
            filtered_db.append(message)
    return filtered_db
