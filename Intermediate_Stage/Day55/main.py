from flask import Flask
import time

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        text = func()
        return text.replace('Welcome', '<b>Welcome</b>')
    return wrapper


def make_underline(func):
    def wrapper():
        text = func()
        return text.replace('Welcome', '<u>Welcome</u>')
    return wrapper


def make_emphasis(func):
    def wrapper():
        text = func()
        return text.replace('Welcome', '<em>Welcome</em>')
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underline
def home():
    return ('<h1 style="text-align: center">Welcome</h1>'
            '<p>This is a paragraph</p><br>'
            '<p>I love programming</p>'
            '<img src="https://media4.giphy.com/media/UQOtfc9uIXVv9IidCD/200.webp?cid=ecf05e475megsalqlmtse7mtuuhz70cu6ychf4qu2ampib1m&ep=v1_gifs_related&rid=200.webp&ct=g" alt="goodnight gif"')


@app.route('/bye/')
def bye():
    return 'Bye!'


@app.route('/username/<name>/5')
def say_name(name):
    return f'Hello there {name.title()}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after path
    return f'Subpath: {subpath}'


if __name__ == '__main__':
    app.run(debug=True)
