#!/usr/bin/python
import gpsd

def test_gps():
    #print(packet.mode)
    while True:
        gpsd.connect()
        packet = gpsd.get_current()
        try:
        #print(packet.mode)
            if packet.mode >= 3:
                print("GPS Online.")
                return
        except:
            pass

def main():
    test_gps()

if __name__ == "__main__":
    main()
