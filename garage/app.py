import RPi.GPIO as gpio
from flask import Flask, render_template

REED_PIN = 12

gpio.setmode(gpio.BCM)
gpio.setup(REED_PIN, gpio.IN)

app = Flask(__name__)

SWITCH_TYPE = 'NO'


@app.route('/')
def index():
    status = 'Open' if get_pin_status() else 'Closed'
    return render_template('index.html', status=status)


def get_pin_status():
    return gpio.input(REED_PIN) ^ (SWITCH_TYPE == 'NO')


if __name__ == "__main__":
    try:
        app.run('0.0.0.0', debug=False)
    finally:
        gpio.cleanup()
