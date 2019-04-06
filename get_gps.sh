#!/bin/bash -e

### Install GPS packages and dependencies
sudo apt-get install gpsd gpsd-clients cmake subversion build-essential espeak freeglut3-dev imagemagick libdbus-1-dev libdbus-glib-1-dev $

sudo pip3 install gpsd-py3

exit 0
