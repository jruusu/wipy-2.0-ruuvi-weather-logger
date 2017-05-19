# main.py -- put your code here!
import binascii
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
    print(beacon_mac + ": " + encoded_measurements)

scan_for_measurements(Bluetooth(), 5)
