from machine import Pin
import pycom
from time import sleep

def pressedHandler(pin):
    sleep(0.1)
    led.toggle()

button = Pin('P11', mode=Pin.IN, pull = Pin.PULL_UP)
led = Pin('P10', mode=Pin.OUT)

button.callback(Pin.IRQ_FALLING, handler = pressedHandler)