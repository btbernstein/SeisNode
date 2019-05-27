#!/usr/bin/python
import gpsd
import time
import led

def test_gps():
    while True:
        try:
            gpsd.connect()
            packet = gpsd.get_current()
            if packet.mode >= 3:
                print("GPS Online.")
                for i in range(2):
                    led.pulse()
                return
        except:
            time.sleep(0.5)
            continue

def main():
    test_gps()

if __name__ == "__main__":
    main()
