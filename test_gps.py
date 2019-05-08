#!/usr/bin/python
import gpsd

def test_gps():
    gpsd.connect()
    packet = gpsd.get_current()
    #print(packet.mode)
    while True:
        #print(packet.mode)
        if packet.mode >= 3:
            return

def main():
    test_gps()

if __name__ == "__main__":
    main()
