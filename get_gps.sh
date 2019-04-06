{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 Arial-BoldMT;}
{\colortbl;\red255\green255\blue255;\red67\green67\blue67;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c33333\c33333\c33333;\cssrgb\c0\c0\c0\c2353;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #!bin/bash -e\
\
### Install GPS packages and dependencies\
\pard\pardeftab720\sl320\partightenfactor0

\f1\b\fs27\fsmilli13585 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 sudo apt-get install gpsd gpsd-clients cmake subversion build-essential espeak freeglut3-dev imagemagick libdbus-1-dev libdbus-glib-1-dev libdevil-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev libgarmin-dev libglc-dev libgps-dev libgtk2.0-dev libimlib2-dev libpq-dev libqt4-dev libqtwebkit-dev librsvg2-bin libsdl-image1.2-dev libspeechd-dev libxml2-dev ttf-liberation -y\cb1 \
\
sudo reboot now}