import smbus 
import time
from gps import collect_gps as GPS
import led

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
#    MSB_x = data[1]
#    LSB_x = data[2]
#    MSB_y = data[3]
#    LSB_y = data[4]
    MSB_z = data[5]
    LSB_z = data[6]

#    xAccl = (MSB_x * 256 + LSB_x) / number_of_bits
#    if xAccl > 2047:
#        xAccl -= 4096
#    yAccl = (MSB_y * 256 + LSB_y) / number_of_bits
#    if yAccl > 2047:
#        yAccl -= 4096
    zAccl = (MSB_z * 256 + LSB_z) / number_of_bits
    if zAccl > 2047:
        zAccl -= 4096

    shot = 0
    # if z acceleration changes by some great amount
    if abs((prev_z-zAccl)/zAccl) >= 0.3: ### Change this
        # record GPS for 1 second.
        with open("/home/pi/Rpi/data/shots/shot%i.csv" %shot, "w+") as writefile:
            status = False
            for i in range(4):
                if status:
                    led.turn_off():
                else:
                    led.turn_on()

                writer = csv.writer(writefile)
                writer.writerow(["Time", "Lat", "Lat Err", "Lon", "Lon Err", "Alt", "Alt Err"])

                data = collect_gps()
                writer.writerow(data)
                writefile.flush()
            writefile.close()
    
    prev_z = zAccl
    shot += 1
