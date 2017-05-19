# main.py -- put your code here!
from network import Bluetooth

bluetooth = Bluetooth()

bluetooth.start_scan(5)

while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv \
    and adv.adv_type == Bluetooth.CONN_ADV \
    and adv.addr_type == Bluetooth.RANDOM_ADDR \
    and adv.data[13:22] == b'\x03ruu.vi/#':
        print(repr(adv))
