#!/bin/bash

sudo apt-get install build-essential python3-dev python3-smbus python-dev python-smbus python3-pip git libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y

#cd ~/SeisNode
#git clone https://github.com/caternuson/Adafruit_CircuitPython_ADS1x15.git
#cd ~/SeisNode/Adafruit_CircuitPython_ADS1x15
#sudo python3 setup.py install

cd ~/

sudo pip3 install adafruit-blinka RPI.GPIO
