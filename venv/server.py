from flask import Flask
import random

app = Flask(__name__)
digit_guess = random.randint(0, 9)
print(digit_guess)

# user_choice = input("Podaj liczbe z zakresu 0 do 9: ")

@app.route('/')
def hello_display():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:user_choice>')
def too_low(user_choice):

    if digit_guess > user_choice:
        return f'<h1>{user_choice} is too low </h1>'\
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif digit_guess < user_choice:
        return f'<h1>{user_choice} is too high </h1>'\
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return f'<h1> YOU FOUND ME </h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == "__main__":
    app.run()