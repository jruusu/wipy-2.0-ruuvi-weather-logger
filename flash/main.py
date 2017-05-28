# main.py -- put your code here!
import binascii
import utime
from network import Bluetooth

def scan_for_measurements(bluetooth, duration_seconds):
    """Find RuuviTag Weather Station beacons, print measurements"""
    bluetooth.start_scan(duration_seconds)

    while bluetooth.isscanning():
        adv = bluetooth.get_adv()
        if adv and is_ruuvi_weather_station(adv):
            # URL-safe Base64 encoded measurements
            # See: https://github.com/ruuvi/ruuvi-sensor-protocols
            encoded_measurements = adv.data[22:] \
                .decode() \
                .rstrip('\0')

            beacon_mac = binascii.hexlify(adv.mac).decode()

            process_datapoint(beacon_mac, encoded_measurements)

def is_ruuvi_weather_station(adv):
    """Returns true if adv appears to be from a RuuviTag Weather Station"""
    return adv.adv_type == Bluetooth.CONN_ADV \
        and adv.addr_type == Bluetooth.RANDOM_ADDR \
        and adv.data[13:22] == b'\x03ruu.vi/#'

def process_datapoint(beacon_mac, encoded_measurements):
    t = utime.localtime()
    formatted_datetime = '{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z' \
        .format(t[0], t[1], t[2], t[3], t[4], t[5])
    print(str(formatted_datetime) + " " + beacon_mac + ": " + encoded_measurements)

scan_for_measurements(Bluetooth(), 5)
