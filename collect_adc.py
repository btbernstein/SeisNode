import numpy as np
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import datetime

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

def main():
    name = datetime.datetime.strftime(datetime.datetime.today(), "%d-%m-%Y_%H-%M")
    print("Collecting Voltages...")
    while True:
        try:
            with open("/home/pi/Rpi/data/%s_adc.txt" % name, "a+") as f:
                with chan0 as chan:
                    while True:
                        # Recieve voltage values
                        f.write(str(chan.voltage) + ", " + str(time.time()) + "\n")
                        f.flush()
                        time.sleep(0.00001)
        except:
            continue

if __name__ == "__main__":
    main()
