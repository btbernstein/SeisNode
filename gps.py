#!/usr/bin/python
import gpsd

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
    import csv
    import time
    with open("/home/pi/Rpi/data/gps.csv", "w+") as writefile:
        print("Collecting GPS...")
        writer = csv.writer(writefile)
        writer.writerow(["Time", "Lat", "Lat Err", "Lon", "Lon Err", "Alt", "Alt Err"])
        while True:
            data = collect_gps()
            writer.writerow(data)
            time.sleep(1)
            writefile.flush()

if __name__ == "__main__":
    main()

