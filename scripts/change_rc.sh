#!/bin/bash

sudo mv /etc/rc.local /etc/rc_copy.local
sudo mv /home/pi/Rpi/scripts/assets/rc.local /etc/rc.local
sudo chmod 777 /etc/rc.local
echo "rc" >> /home/pi/Rpi/scripts/assets/_status.txt
