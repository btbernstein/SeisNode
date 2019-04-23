#!/bin/bash

cd ~/Rpi
sudo chmod +x get_gps.sh
./get_gps.sh
sudo chmod +x get_adc.sh
./get_adc.sh
sudo chmod +X start_sensors.sh

exit 0
