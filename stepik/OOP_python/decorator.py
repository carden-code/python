# decorator
def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


@table
@header  # say = table(header(say))
def say(name, surname, age):
    print('hello', name, surname, age)


say('Vasya', 'ivanov', 30)
