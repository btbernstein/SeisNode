#!/bin/bash

sudo rm -rf /home/pi/Rpi
cd /usr/local/lib/python3.5/dist-packages
sudo rm -rf adafruit_ads1x15

cd ~/
git clone https://github.com/btbernstein/Rpi.git

sudo chmod +x /home/pi/Rpi/scripts/get_software.sh
. /home/pi/Rpi/scripts/get_software.sh

exit 0
