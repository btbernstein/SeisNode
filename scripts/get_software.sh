#!/bin/bash

sudo pip install --upgrade pip
sudo pip3 install --upgrade pip

sudo chmod +x /home/pi/Rpi/scripts/get_gps.sh
. /home/pi/Rpi/scripts/get_gps.sh
sudo chmod +x /home/pi/Rpi/scripts/get_adc.sh
. /home/pi/Rpi/scripts/get_adc.sh
sudo chmod +x /home/pi/Rpi/scripts/change_rc.sh
. /home/pi/Rpi/scripts/change_rc.sh
sudo chmod +x /home/pi/Rpi/scripts/start_sensors.sh

cd ~/

exit 0
