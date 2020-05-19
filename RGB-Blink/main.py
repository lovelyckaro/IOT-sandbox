from machine import Timer
import pycom
import time

class ColorSwitcher:
    def __init__(self, colors):
        self.colors = colors
        self.current_color = 0
        self._alarm = Timer.Alarm(self.switch_color, s = 1.0, periodic = True)
    
    def switch_color(self, alarm):
        self.current_color = (self.current_color + 1) % len(self.colors)
        #print("Color = ", hex(self.colors[self.current_color]))
        pycom.rgbled(self.colors[self.current_color])



# Disable heartbeat
pycom.heartbeat(False)

#colorSwitcher = ColorSwitcher([0xff0000, 0x00ff00, 0x0000ff])