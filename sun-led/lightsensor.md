
Connect photoresistor to outpin
connect inpin to other end of photoresistor
connect 560 Ohm resistor between photoresistor and ground
Should look something like this:

outpin-----photoresistor---.---resistor--GND
                           |
                         inpin

The inpin must be one of the ones with support for adc
These are p13 to p20