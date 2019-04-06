import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import matplotlib.pyplot as plt
from g import collect_datum as gps
import matplotlib
matplotlib.use("TkAgg")
import _thread


#GPIO.setmode(GPIO.BOARD)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.gain = 1
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)
#print("hi")
#print("{:>5}\t{:>5}".format('raw', 'v'))

voltages = []
times_v = [] # About 80 per second
times_g = []
lats = []
lat_err = []
lons = []
lon_err = []
alts = []
alt_err = []

def collect_voltages():
    try:
        while True:
            t_v = time.time()
            volt = chan.voltage
            times_v.append(t_v)
            voltages.append(volt)
            print("hi")
    except KeyboardInterrupt:
        return
try:
   # _thread.start_new_thread(collect_voltages,())
    while True:
        
        # Recieve time and voltage values
        t_v = time.time()
        volt = chan.voltage
        # Append the values to their respective lists
        times_v.append(t_v)
        voltages.append(volt)
#        print(volt)
        # Recive gps data
        t_g,lat,lon,alt = gps()
        t_g = str(t_g).split(' ')[1]
        t_g = str(t_g).split('-')[0]
        #print(t_g)
        times_g.append(t_g)
        lats.append(lat[0])
        lat_err.append(lat[1])
        lons.append(lon[0])
        lon_err.append(lon[1])
        alts.append(alt[0])
        alt_err.append(alt[1])
 
        # Print values for testing purposes
        #print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    
        # Clear the previous plot and plot the current points
        #plt.clf()
        #plt.plot(times, voltages)
        # Update the plot
        #plt.pause(0.001)
#        time.sleep(1)

except KeyboardInterrupt:
#    plt.plot(times_v,voltages)
#    plt.show(block=True)
    times_v[:] = [x - times_v[0] for x in times_v]
    fig,ax = plt.subplots(4,1,figsize=(16,10))
    ax[0].plot(times_v,voltages)
    ax[0].set_title("Geophone Readings: n=%i Data Points" % len(voltages), fontsize=16, fontweight="bold")
    ax[0].set_xlabel("Time (seconds)", fontsize=14, fontweight="bold")
    ax[0].set_ylabel("Voltage", fontsize=14, fontweight="bold")
    ax[1].errorbar(times_g,lats,yerr=lat_err)
    ax[1].set_title("Latitude: n=%i Data Points" % len(lats), fontsize=16, fontweight="bold")
    ax[1].set_xlabel("Time", fontsize=14, fontweight="bold")
    ax[1].set_ylabel("Latitude (Decimal$^\circ$)", fontsize=14, fontweight="bold")
    #ax[0,1].xaxis.set_ticks(times_g[::4], rotation=45)
    ax[2].errorbar(times_g,lons,yerr=lon_err)
    ax[2].set_title("Longitude: n=%i Data Points" % len(lons), fontsize=16, fontweight="bold")
    ax[2].set_xlabel("Time", fontsize=14, fontweight="bold")
    ax[2].set_ylabel("Longitude (Decimal$^\circ$)", fontsize=14, fontweight="bold")
    ax[3].errorbar(times_g,alts,yerr=alt_err)
    ax[3].set_title("Altitude: n=%i Data Points" % len(alts), fontsize=16, fontweight="bold")
    ax[3].set_xlabel("Time", fontsize=14, fontweight="bold")
    ax[3].set_ylabel("Altitude (meters)", fontsize=14, fontweight="bold")

    for axi in ax.flat:
        if axi != ax[0]:
          plt.setp(axi.xaxis.get_majorticklabels(),rotation=20)
        axi.xaxis.set_major_locator(plt.MaxNLocator(5))

    plt.tight_layout()
    plt.savefig("all")
    
    #plt.subplots_adjust(hspace=0.5)    
    plt.show(block=True)
    #print(len(times_v),len(voltages))
    #print(times_v)
    #print(len(alts))
    #print(alts)
#    for i in range(len(times_v)-2):
#        print(times_v[i+1] - times_v[i])
