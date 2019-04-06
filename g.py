#!/usr/bin/python
#from gps3 import gps3
import gpsd
import csv
import time

#def collect_data():
#    #i = 0
#    with open("/home/pi/data", mode='a') as d:
#        d_writer = csv.writer(d, delimiter=',')
#        time,lat,lon,alt = collect_datum()
#        d_writer.writerow([time, lat, lon, alt])
#        #i += 1
#        #if i == 57:
#            #break
#    #print(i)
 
def collect_datum():
    #gps_socket = gps3.GPSDSocket()
    #data_stream = gps3.DataStream()
    #gps_socket.connect()
    #gps_socket.watch()
    while True:
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
        #data = [time,lat,lon,alt]
        #for d in data:
            #if d == 0:
                #break
        #else:
            const = 1/111319.9 #  degrees per meter
            data_error = [time,(lat,ey*const),(lon,ex*const),(alt,ez)]
            return data_error
        #print(data) 

    #for new_data in gps_socket:
            #if new_data:
                #data_stream.unpack(new_data)
                #time = data_stream.time_local()
                #lat = data_stream.TPV['lat']
                #lon = data_stream.TPV['lon']
                #alt = data_stream.TPV['alt']
                #data = [time, lat, lon, alt]
                #print(data)
                #for d in data:
                    #if d == 'n/a':
                        #break
                #else:
                    #print(data)
                    #return data

#collect_data()
