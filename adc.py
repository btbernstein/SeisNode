import numpy as np
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import csv


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.gain = 1
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

voltages = []
times = [time.time()] # About 80 per second

try:
    while True:
        
        # Recieve time and voltage values
   
        volt = 
        # Append the values to their respective lists
    
        voltages.append(chan.voltage)

except KeyboardInterrupt:
    times.append(time.time())
    times[:] = [x - times[0] for x in times]
    #arr = [times_v, voltages, times_g, lats, lat_err, lons, lon_err, alts, alt_err]

    with open(str("data.txt"), 'w+') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(np.array(arr).T)

    writeFile.close()
    
