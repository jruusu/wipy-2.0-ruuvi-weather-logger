# boot.py -- run on boot-up
from machine import RTC, UART
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

rtc = RTC()
rtc.ntp_sync(config['ntp']['server'])
while rtc.now()[0] == 1970:
    pass
