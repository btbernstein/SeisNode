from gps import collect_gps as GPS
from adc import collect_adc as ADC

voltages = []
g_data = []

times_g = []
lats = []
lat_err = []
lons = []
lon_err = []
alts = []
alt_err = []


try:
    while True:
        voltages.append(ADC())
        g_data.append(GPS())


except KeyboardInterrupt:
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
    
    arr = [voltages, times_g, lats, lat_err, lons, lon_err, alts, alt_err]

    with open(str(times_g[0]), 'w+') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(np.array(arr).T)

    writeFile.close()
