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
        data = [time,(lat,ey*const),(lon,ex*const),(alt,ez)]
        return data
        
if __name__ == "__main__":
    collect_gps()
