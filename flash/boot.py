# boot.py -- run on boot-up
from machine import UART
from network import WLAN
import os
import ujson
uart = UART(0, 115200)
os.dupterm(uart)

config = ujson.loads(open('config.json', 'r').readall())

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid=config['wlan']['ssid'], auth=(WLAN.WPA2, config['wlan']['password']))
while not wlan.isconnected():
    pass
