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
ads.gain = 4
ads.mode = 0x0000
ads.data_rate = 860
ads.comparator_config = 0
# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)

def collect_adc():
    voltages = []
    try:
        with chan0 as chan:
            while True:
                # Recieve voltage values          
                voltages.append(chan.voltage)
    except:
        return voltages

def main():
    t0 = time.time()
    voltages = collect_adc()
    t1 = time.time()
    dt = t1 - t0
    print(len(voltages)/dt)

if __name__ == "__main__":
    main()
    
