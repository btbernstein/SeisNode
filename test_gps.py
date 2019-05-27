#!/usr/bin/python
import gpsd
import time

def test_gps():
    while True:
        try:
            gpsd.connect()
            packet = gpsd.get_current()
            if packet.mode >= 3:
                print("GPS Online.")
                return
        except:
            time.sleep(0.5)
            continue

def main():
    test_gps()

if __name__ == "__main__":
    main()
