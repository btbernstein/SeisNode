import numpy as np
import gpsd
import csv
import datetime
import time
import board
import busio
import smbus 
import led
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode
import matplotlib.pyplot as plt

class SeisNode:
    """
    Sesmic node class (for Raspberry Pi)
    
    ADC Parameters (kwargs):
        gain = 1
        mode = Mode.CONTINUOUS
        data_rate = 860
    """
    
    def __init__(self,**kwargs):
        self.gain = 1
        self.mode = Mode.CONTINUOUS
        self.data_rate = 860
        
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
        self.vz = []
        self.vx = []
        self.vy = []
        
        ## Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)
        ## Create the ADC object
        self.ads = ADS.ADS1115(i2c)
        self.ads.gain = self.gain
        self.ads.mode = Mode.CONTINUOUS
        self.ads.data_rate = self.data_rate
        #self.ads.comparator_config = 0
        
    def set_gain(self,gain):
        self.ads.gain = gain
        self.gain = gain
            
    def collect_adc(self):
        self.vz = []
        self.vx = []
        self.vy = []
        # Create single-ended input on channel 0
        chan0 = AnalogIn(self.ads, ADS.P0)
        chan1 = AnalogIn(self.ads, ADS.P1)
        chan2 = AnalogIn(self.ads, ADS.P2)
        try:
            t = time.time()
            while time.time()-t < 60:
                # Recieve voltage values          
                self.vz.append(chan0.value)
                self.vx.append(chan1.value)
                self.vy.append(chan2.value)
        except KeyboardInterrupt:
            pass
        
        return  vz,vx,vy

    def collect_gps(self):
        gpsd.connect()
        packet = gpsd.get_current()
        #print(packet.mode)
        if packet.mode >= 3:
            time = packet.get_time(local_time=True)
            lat = packet.lat
            ey = packet.error['y']
            lon = packet.lon
            ex = packet.error['x']
            alt = packet.alt
            ez = packet.error['v']

            const = 1/111319.9 #  degrees per meter
            data = [time,lat,ey*const,lon,ex*const,alt,ez]
            return data

        
    def trigger(self):
        bus = smbus.SMBus(1)
        shot = 0
        status = True
        while True:
            #Parameters for write_byte_data
            #1. Address of the device
            #2. Communication data - active mode control register
            #3. Our data - 0 (standby mode) or 1 (active)
            bus.write_byte_data(0x1D, 0x2A, 1) 

            #Read from the status register, real-time status register 0x00
            #Data returned will be an array
            #Contents of 7 bytes read and stored in data array represent:
            #status (ignore), MSBx, LSBx, MSBy, LSBy, MSBz, LSBz
            data = bus.read_i2c_block_data(0x1D, 0x00, 7)

            number_of_bits = 16
            MSB_z = data[5]
            LSB_z = data[6]

            zAccl = (MSB_z * 256 + LSB_z) / number_of_bits
            if zAccl > 2047:
                zAccl -= 4096

            # if z acceleration changes by some great amount
            prev_z = 1000
            if abs((prev_z-zAccl)/zAccl) >= 1.0: ### Change this
                bus.write_byte_data(0x1D, 0x2A, 0)
                # record GPS for 1 second.
                with open("/home/pi/SeisNode/data/shots.csv" %shot, "a+") as writefile:
                    print("Trigger")
                    led.turn_on()
                    writer = csv.writer(writefile)
                    if shot == 0:
                        writer.writerow(["Shot","Time", "Lat", "Lat Err", "Lon", "Lon Err", "Alt", "Alt Err"])
                    start = time.time()
                    while time.time()-start < 1:
                        data = self.collect_gps()
                        data = np.concatenate([[shot],data])
                        writer.writerow(data)
                        time.sleep(0.2)
                    writefile.flush()
                    writefile.close()

                    shot += 1
                    time.sleep(30)
                    led.turn_off()
                    prev_z = 1000
                    status = True
                    continue
            status = False
            prev_z = zAccl
            
        def collect_data(self):
            pass
