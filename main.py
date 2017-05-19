# main.py -- put your code here!
from network import Bluetooth

bluetooth = Bluetooth()

bluetooth.start_scan(5)

while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv:
        print(repr(adv))
