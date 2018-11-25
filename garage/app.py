import RPi.GPIO as gpio
from flask import Flask, render_template

REED_PIN = 12
LED = 16

gpio.setmode(gpio.BCM)
gpio.setup(REED_PIN, gpio.IN)
gpio.setup(LED, gpio.OUT)

app = Flask(__name__)

SWITCH_TYPE = 'NO'  # normally open, change to NC for normally closed


@app.route('/')
def index():
    status = 'Open' if get_pin_status() else 'Closed'
    return render_template('index.html', status=status)


def get_pin_status():
    """Read status of the reed switch pin"""
    return gpio.input(REED_PIN) ^ (SWITCH_TYPE == 'NO')


def set_led(high=True):
    """Turn on/off led pin"""
    if high:
        gpio.output(LED, gpio.HIGH)
    else:
        gpio.output(LED, gpio.LOW)


if __name__ == "__main__":
    try:
        app.run('0.0.0.0', debug=False)
    finally:
        gpio.cleanup()
