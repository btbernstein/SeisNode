#!/bin/bash
cd ~/
sudo mv /etc/rc.local /etc/rc_copy.local
sudo mv Rpi/rc.local /etc/rc.local
sudo chmod 777 /etc/rc.local

exit 0
