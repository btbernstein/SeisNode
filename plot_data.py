
import numpy as np
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.gain = 2
ads.mode = 0x0000
ads.data_rate = 860
ads.comparator_config = 0
# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)

def plot():
    plt.ion()
    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(111)
#     plt.title("Geophone Readings", fontsize=16, fontweight="bold")
#     plt.xlabel("Time (seconds)", fontsize=14, fontweight="bold")
#     plt.ylabel("Voltage", fontsize=14, fontweight="bold")
    #ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    i = 0
    time_0 = time.time()
    times = []
    voltages = []
    plt.show()
    while True:
        times.append(time.time()-time_0)
        voltages.append(i*i)
        plt.clf()
        
        ax.plot(times,voltages)
        #plt.show(block=True)
        plt.pause(5)
        i += 1
    plt.ioff()
    plt.show(block=True)
