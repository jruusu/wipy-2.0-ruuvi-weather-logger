# main.py -- put your code here!
import binascii
from network import Bluetooth

bluetooth = Bluetooth()

bluetooth.start_scan(5)

while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv \
    and adv.adv_type == Bluetooth.CONN_ADV \
    and adv.addr_type == Bluetooth.RANDOM_ADDR \
    and adv.data[13:22] == b'\x03ruu.vi/#':
        # URL-safe Base64 encoded measurements
        # See: https://github.com/ruuvi/ruuvi-sensor-protocols
        encoded_measurements = adv.data[22:] \
            .decode() \
            .rstrip('\0')

        beacon_mac = binascii.hexlify(adv.mac).decode()

        print(beacon_mac + ": " + encoded_measurements)
