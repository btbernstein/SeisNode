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
ads.gain = 16
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Arrays to store volages
voltages = []

def collect_adc():
    # Recieve voltage values    
    return chan.voltage


    
if __name__ == "__main__":
    collect_adc()
    
