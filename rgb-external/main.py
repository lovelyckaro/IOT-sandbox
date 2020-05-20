from machine import Pin, PWM, Timer
from time import sleep

brightness = 0.0
velocity = 0.1
def update(alarm):
    global brightness
    global velocity
    global red, green, blue
    if brightness + velocity > 1.0 or brightness + velocity < 0.0:
        velocity = -velocity
    brightness += velocity
    red.duty_cycle(brightness)
    blue.duty_cycle(1.0 - brightness)
    green.duty_cycle(0.5 - brightness)


pwm = PWM(0, frequency=78000) # pwm on timer 0, with frequency 5000 Hz

red = pwm.channel(0, pin="P10", duty_cycle = 0)
green = pwm.channel(1, pin="P11", duty_cycle = 0)
blue = pwm.channel(2, pin="P12", duty_cycle = 0)
alarm = Timer.Alarm(update, 0.1, periodic = True, arg = None)
