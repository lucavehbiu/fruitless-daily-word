import random
import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message

mail_password = os.getenv("MAIL_PASSWORD")

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lvehbiu@fruitless.nl'  # Your Gmail address
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_DEFAULT_SENDER'] = 'lvehbiu@fruitless.nl'

mail = Mail(app)

def send_email(receiver_email, word, explanation):
    msg = Message("Albanian Word of the Day", recipients=[receiver_email])
    msg.html = render_template('email_template.html', word=word, explanation=explanation)
    mail.send(msg)

words = [
    {"word": "Fjalë1", "explanation": "Explanation for word 1"},
    {"word": "Fjalë2", "explanation": "Explanation for word 2"},
    # Add more words as needed
]

def save_email(email):
    with open('subscribers.txt', 'a') as file:
        file.write(email + '\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    user_email = request.form['email']
    save_email(user_email)
    # Send an email, with the user's email as the sender
    send_email(user_email, "Test Word", "Test Explanation")
    return "Subscription successful! Check your email."


@app.route('/random')
def random_word():
    word = random.choice(words)
    return render_template('random_word.html', word=word)


if __name__ == '__main__':
    app.run(debug=True)
