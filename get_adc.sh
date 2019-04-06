#!/bin/bash

sudo apt-get install build-essential python3-dev python3-smbus python-dev python-smbus python3-pip git libreadline-gplv2-dev libncursesw5-$
git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
cd Adafruit_Python_ADS1x15
sudo python3 setup.py install
cd ~
sudo pip3 install  adafruit-blinka RPI.GPIO  adafruit-circuitpython-ads1x15

exit 0