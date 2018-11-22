import RPi.GPIO as gpio
from flask import Flask, render_template

gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.IN)

app = Flask(__name__)

SWITCH_TYPE = 'NO'


@app.route('/')
def index():
    status = 'Closed' if get_pin_status() else 'Open'
    return render_template('index.html', status=status)


def get_pin_status():
    return gpio.input(12) ^ SWITCH_TYPE == 'NO'


if __name__ == "__main__":
    app.run('0.0.0.0')
