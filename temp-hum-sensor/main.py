from machine import Pin, Timer

class IOPin:
    def __init__(self, pin: str):
        self.pin = pin
    
    def read(self):
        tmp = Pin(self.pin, mode = Pin.IN, pull = Pin.PULL_UP)
        return tmp()
    
    def write(self, value):
        tmp = Pin(self.pin, mode = Pin.OUT)
        tmp(value)

pin = IOPin('P10')
