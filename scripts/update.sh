#!/bin/bash

cd ~/Rpi
rm adc.py collect_adc.py collect_data.py gps.py led.py plot_data.py rc.local test_gps.py trigger.py
curl -o adc.py https://raw.githubusercontent.com/btbernstein/Rpi/master/adc.py
curl -o collect_adc.py https://raw.githubusercontent.com/btbernstein/Rpi/master/collect_adc.py
curl -o collect_data.py https://raw.githubusercontent.com/btbernstein/Rpi/master/collect_data.py
curl -o gps.py https://raw.githubusercontent.com/btbernstein/Rpi/master/gps.py
curl -o led.py https://raw.githubusercontent.com/btbernstein/Rpi/master/led.py
curl -o plot_data.py https://raw.githubusercontent.com/btbernstein/Rpi/master/plot_data.py
curl -o rc.local https://raw.githubusercontent.com/btbernstein/Rpi/master/rc.local
curl -o test_gps.py https://raw.githubusercontent.com/btbernstein/Rpi/master/test_gps.py
curl -o trigger.py https://raw.githubusercontent.com/btbernstein/Rpi/master/trigger.py

sudo chmod +x /home/pi/Rpi/scripts/change_rc.sh
. /home/pi/Rpi/scripts/change_rc.sh

cd /scripts/
rm get_software.sh lcd.sh
curl -o home/pi/Rpi/scripts/get_software.sh https://raw.githubusercontent.com/btbernstein/Rpi/master/scripts/get_software.sh
sudo chmod +x /home/pi/Rpi/scripts/get_software.sh
curl -o /home/pi/Rpi/scripts/lcd.sh https://raw.githubusercontent.com/btbernstein/Rpi/master/scripts/lcd.sh
sudo chmod +x /home/pi/Rpi/scripts/lcd.sh
. /home/pi/Rpi/scripts/lcd.sh

