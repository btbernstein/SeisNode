import smbus 
import time
from gps import collect_gps as GPS
import led
import numpy as np

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
        with open("/home/pi/Rpi/data/shots.csv" %shot, "a+") as writefile:
            print("Trigger")
            led.turn_on()
            writer = csv.writer(writefile)
            if shot == 0:
                writer.writerow(["Shot","Time", "Lat", "Lat Err", "Lon", "Lon Err", "Alt", "Alt Err"])
            start = time.time()
            while time.time()-start < 1:
                data = GPS()
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
