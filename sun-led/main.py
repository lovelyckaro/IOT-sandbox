from machine import Pin, ADC, Timer
import time

# Light sensor class
class LightSensor:
    adc = ADC()
    def __init__(self, outpin: str, inpin: str):
        self.outpin = Pin(outpin, mode = Pin.OUT)
        self.inpin = LightSensor.adc.channel(pin = inpin)
    # Temporarily turn on voltage over photoresistor and measure
    # voltage on inpin. Range of voltage should be between 0 - 700 mV
    def voltage(self):
        self.outpin(1)
        #time.sleep(0.1)
        voltage = self.inpin.voltage()
        self.outpin(0)
        return voltage
    # Measure voltage on inpin and determine whether it is bright or dark
    # any voltage over 300 mV is bright
    def bright(self):
        voltage = self.voltage()
        return voltage > 300

# Light controlled LED, uses LightSensor to turn LED on or off
class LightControlledLED:
    def __init__(self, pin: str, lightSensor):
        self.pin = Pin(pin, mode = Pin.OUT)
        self.sensor = lightSensor
        self._alarm = Timer.Alarm(self.update, 0.5, periodic = True)

    def update(self, alarm):
        if self.sensor.bright():
            self.pin(0)
        else:
            self.pin(1)
    
sensor = LightSensor('P12', 'P13')
led = LightControlledLED('P10', sensor)