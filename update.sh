#!/bin/bash
cd ~/
sudo rm -rf Rpi
git clone https://github.com/btbernstein/Rpi.git
cd /usr/local/lib/python3.5/dist-packages
sudo rm -rf adafruit_ads1x15
cd ~/Rpi
sudo chmod +x get_software.sh
./get_software.sh

sudo chmod +x change_rc.sh
./change_rc.sh

exit 0
