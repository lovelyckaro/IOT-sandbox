from machine import RMT
import _thread

reciever = RMT(channel = 3, gpio='P23', rx_idle_threshold=1000)

transmitter = RMT(channel = 4, gpio='P22', tx_idle_level=RMT.LOW)