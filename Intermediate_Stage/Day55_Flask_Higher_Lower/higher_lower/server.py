from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 100)


@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 100</h1>'
            '<img src="https://media0.giphy.com/media/wIo1jZH4iHf6xRwJu4/giphy.webp?'
            'cid=790b761136fpqpiudo79qyez7q7gug7xbq5vn5xso4ws'
            'bo1a&ep=v1_gifs_search&rid=giphy.webp&ct=g" alt="home page gif">')


@app.route('/<int:numb>')
def check_number(numb):
    if numb < number:
        return ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="too low gif"')
    elif numb > number:
        return ('<h1 style="color: blue">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g" alt="too high gif"')
    else:
        return ('<h1 style="color: green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="correct guess gif"')


if __name__ == '__main__':
    app.run(debug=True)
