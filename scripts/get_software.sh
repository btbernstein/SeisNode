#!/bin/bash

sudo pip install --upgrade pip
sudo pip3 install --upgrade pip

sudo chmod +x /home/pi/SeisNode/scripts/get_gps.sh
. /home/pi/SeisNode/scripts/get_gps.sh

sudo chmod +x /home/pi/SeisNode/scripts/get_adc.sh
. /home/pi/SeisNode/scripts/get_adc.sh

sudo chmod +x /home/pi/SeisNode/scripts/start_sensors.sh
. /home/pi/SeisNode/scripts/start_sensors.sh

sudo chmod +x /home/pi/SeisNode/SeisNode/startup.py

sudo chmod +x /home/pi/SeisNode/scripts/change_rc.sh
. /home/pi/SeisNode/scripts/change_rc.sh

sudo chmod +x /home/pi/SeisNode/scripts/lcd.sh
. /home/pi/SeisNode/scripts/lcd.sh
