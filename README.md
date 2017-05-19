# wipy-2.0-ruuvi-weather-logger

## Mission
1) read data from [RuuviTags](https://ruuvitag.com/) running the stock [Weather Station](https://ruu.vi/setup/#weather-station) firmware
2) dump it in the cloud for further processing

## TODO / ideas for future development
* Connect logger to local wifi
* NTP sync; https://docs.pycom.io/pycom_esp32/library/machine.RTC.html?highlight=ntp#machine.rtc.ntp_sync
* Set up AWS infrastructure to receive the data
* Implement data upload from logger to AWS
* Continuous operation; sleep, repeat

## Resources
* [pycom esp32 Bluetooth tutorial](https://docs.pycom.io/pycom_esp32/pycom_esp32/tutorial/includes/bluetooth.html)
* [pycom esp32 API Reference: Bluetooth](https://docs.pycom.io/pycom_esp32/library/network.Bluetooth.html)
* [RuuviTag sensor protocol for Eddystone-URL](https://github.com/ruuvi/ruuvi-sensor-protocols)
