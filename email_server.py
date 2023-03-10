import os
from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Init flask
app = Flask(__name__)
# Load env vars
load_dotenv()
# Pulled this out cuz its used later
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')

# Config for mailing
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = bool(os.environ.get('MAIL_USE_TLS'))
app.config['MAIL_USE_SSL'] = bool(os.environ.get('MAIL_USE_SSL'))

mail = Mail(app)

@app.route('/')
def hello_world():
  return 'Hello world'

@app.route('/send_email')
def send_email(email):
    msg = Message('test', sender=MAIL_USERNAME, recipients=[email])
    msg.body = 'test'
    mail.send(msg)
    return 'Email sent'

if __name__ == '__main__':
    app.run(debug=True)

