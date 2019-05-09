import numpy as np
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

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

with open("/home/pi/Rpi/data/adc.txt", "w+") as f:
    with chan0 as chan:
        print("Collecting Voltages...")
        while True:
            # Recieve voltage values
            f.write(str(chan.voltage) + "\n")
            f.flush()
