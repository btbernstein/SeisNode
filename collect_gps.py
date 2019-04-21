from g import collect_datum as gps

times_g = []
lats = []
lat_err = []
lons = []
lon_err = []
alts = []
alt_err = []

while True:
    # Recive gps data
    t_g,lat,lon,alt = gps()
    t_g = str(t_g).split(' ')[1]
    t_g = str(t_g).split('-')[0]
    #print(t_g)
    times_g.append(t_g)
