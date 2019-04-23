from gps import collect_gps as GPS
from adc import collect_adc as ADC
import csv
import time
import numpy as np

cont = True
i = 1
while cont:
    for j in range(1,4):

        voltages = []
        g_data = []

        times_g = []
        lats = []
        lat_err = []
        lons = []
        lon_err = []
        alts = []
        alt_err = []

        print("Station %i Trial %i \nPress enter to collect data:" % (i,j))
        pause = input('')
        print("Collecting data...")

        g_data.append(GPS())
        t0 = time.time()
        voltages = ADC()
        t1 = time.time()
        g_data.append(GPS())


        for g in g_data:
            t_g = g[0]
            t_g = str(t_g).split(' ')[1]
            t_g = str(t_g).split('-')[0]
            times_g.append(t_g)

            lats.append(g[1][0])
            lat_err.append(g[1][1])

            lons.append(g[2][0])
            lon_err.append(g[2][1])

            alts.append(g[3][0])
            alt_err.append(g[3][1])

        arr = np.asarray([voltages, times_g, lats, lat_err, lons, lon_err, alts, alt_err])

        with open("data/S%iT%i" % (i,j), 'w+') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(arr.T)

        writeFile.close()
    prompt = 0
    while str.lower(prompt) != 'y' or str.lower(prompt) != 'n':
        prompt = input("Record another station? (Y/n): ")
    if str.lower(prompt) == 'y':
        cont = True
        i += 1
    else:
        cont = False
