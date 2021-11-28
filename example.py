import RPi.GPIO as gpio
import time as t
import requests

IP = "172.18.186.6"
PORT = "5000"
HOST = "http://"+IP+":"+PORT+"/bookkeeping.html"

"""
General Purpose Input/Output, aka "BCM" or "Broadcom". These are the big
numbers, e.g. "GPIO 22". You'll use these with RPi.GPIO and GPIO Zero.
"""
gpio.setmode(gpio.BCM)

LEDPINPIN = 4
gpio.setup(LEDPIN, gpio.OUT)
gpio.output(LEDPIN, gpio.HIGH)


SWITCHPIN = 23
gpio.setup(SWITCHPIN, gpio.IN)

while True:
    press = gpio.input(SWITCHPIN)
    if press == gpio.HIGH:
        gpio.output(LEDPIN, gpio.LOW)
        res = requests.post(HOST, data={'order': '1'})
        t.sleep(0.2)
    else:
        gpio.output(LEDPIN, gpio.HIGH)
