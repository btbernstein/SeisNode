#!/usr/bin/python
import gpsd
import csv
import time
import datetime

def collect_gps():
    gpsd.connect()
    packet = gpsd.get_current()
    #print(packet.mode)
    if packet.mode >= 3:
        time = packet.get_time(local_time=True)
        lat = packet.lat
        ey = packet.error['y']
        lon = packet.lon
        ex = packet.error['x']
        alt = packet.alt
        ez = packet.error['v']

        const = 1/111319.9 #  degrees per meter
        data = [time,lat,ey*const,lon,ex*const,alt,ez]
        data_label = ["Time","Latitude","Latitude Error","Longitude","Longitude Error","Altitude","Altitude Error"]
        for d,l in zip(data,data_label):
            print(l+":",d) 
        print()

def main():
    name = datetime.datetime.strftime(datetime.datetime.today(), "%d-%m-%Y_%H-%M")
    print("Collecting GPS...")
    while True:
        try:
            data = collect_gps()
            time.sleep(5)

        except KeyboardInterrupt:
            return

if __name__ == "__main__":
    main()
