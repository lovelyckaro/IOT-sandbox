

class Thermostat:
    def __init__(self, low, high):
        self.on = False
        self.low = low
        self.high = high

    def update(self, temperature):
        print("Updating with temperature {}".format(temperature)) 
        if temperature > self.low and not self.on:
            print("Send turn on signal")
            self.on = True
        elif temperature < self.high and self.on:
            print("Send turn off signal")
            self.on = False
        else:
            print("Do nothing")
        self.status()

    def status(self):
        print("Heater is turned {}".format("on" if self.on else "off"))

therm = Thermostat(20, 40)

therm.update(20)
therm.update(30)
therm.update(60)

