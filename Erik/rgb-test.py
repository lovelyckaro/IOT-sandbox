from machine import Pin, PWM
import time
#import random

#red = Pin('P12', mode = Pin.OUT)
#green = Pin('P11', mode = Pin.OUT)
#blue = Pin('P10', mode = Pin.OUT)

pwm_timer = PWM(0, frequency = 5000)

red_pwm = pwm_timer.channel(0, pin = 'P12', duty_cycle = 0)
green_pwm = pwm_timer.channel(1, pin = 'P11', duty_cycle = 0)
blue_pwm = pwm_timer.channel(2, pin = 'P10', duty_cycle = 0)

def flash(led):
    led.toggle()
    time.sleep(1)
    led.toggle()

def color_cycle():
    for i in range(100):
        j = randint(1, 100)
        red_pwm.duty_cycle((abs(j-i))/100)
        time.sleep(.300)
        green_pwm.duty_cycle((j)/100)
        time.sleep(.300)
        blue_pwm.duty_cycle((i)/100)
        time.sleep(.300)

def turn_off():
   red_pwm.duty_cycle(0)
   green_pwm.duty_cycle(0)
   blue_pwm.duty_cycle(0)