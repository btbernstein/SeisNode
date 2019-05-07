#!/bin/bash

sudo killall gpsd
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo gpsd /dev/serial0 -n -F /var/run/gpsd.sock

exit 0
