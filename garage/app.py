import RPi.GPIO as gpio
from flask import Flask, render_template

gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.IN)

app = Flask(__name__)


@app.route('/')
def index():
    status = 'Open' if get_pin_status() else 'Closed'
    return render_template('index.html', status=status)


def get_pin_status():
    return gpio.input(12)


if __name__ == "__main__":
    app.run()