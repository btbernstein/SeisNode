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
        return data

def main():
    name = datetime.datetime.strftime(datetime.datetime.today(), "%d/%m/%Y-%H:%M")
    print("Collecting GPS...")
    while True:
        try:
            with open("/home/pi/Rpi/data/%s_gps.csv" % name, "w+") as writefile:
                writer = csv.writer(writefile)
                writer.writerow(["Time", "Lat", "Lat Err", "Lon", "Lon Err", "Alt", "Alt Err"])
                while True:
                    data = collect_gps()
                    writer.writerow(data)
                    time.sleep(1)
                    writefile.flush()
        except:
            name_err = str(datetime.datetime.now())
            with open("/home/pi/Rpi/data/errors.txt", "a+") as writefile:
                writer = csv.writer(writefile)
                writer.writerow([name_err])

if __name__ == "__main__":
    main()

