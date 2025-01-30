from flask import Flask
from app.routes.sendmessage import send_to_bot
import os


app = Flask(__name__, static_folder='public')

send_to_bot(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)