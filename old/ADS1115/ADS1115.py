import numpy as np
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode
import matplotlib.pyplot as plt

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
ads.gain = 1
ads.mode = Mode.CONTINUOUS
ads.data_rate = 64
ads.comparator_config = 0
# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)

def collect_adc():
    v0 = []
    v1 = []
    v2 = []
    try:
        t = time.time()
        while time.time()-t < 60:
                # Recieve voltage values          
            v0.append(chan0.value)
            v1.append(chan1.value)
            v2.append(chan2.value)
    except KeyboardInterrupt:
        return v0,v1,v2
    return  v0,v1,v2

def main():
    rates = [128,250,475,860]
    samples = []
    for rate in rates:
        ads.data_rate = rate
        print(rate)
        sample = []
        for i in range(5):
            v0,v1,v2 = collect_adc()
            dt = 60
            s = [len(v0)/dt,len(v1)/dt,len(v2)/dt]
            sample.append(s)
            if i == 0:
                plt.figure(figsize=(12,15))
                plt.subplot(311)
                plt.plot(v0)
                plt.xlabel("Samples")
                plt.ylabel("Amplitude")
                plt.title(f"Z Signal at {rate} SPS")
                plt.subplot(312)
                plt.plot(v1)
                plt.xlabel("Samples")
                plt.ylabel("Amplitude")
                plt.title(f"X? Signal at {rate} SPS")
                plt.subplot(313)
                plt.plot(v2)
                plt.xlabel("Samples")
                plt.ylabel("Amplitude")
                plt.title(f"Y? Signal at {rate} SPS")
                plt.tight_layout()
                plt.savefig(f"Figures/{rate}_full_signal_cont.jpg")

        samples.append(sample)
    for sample,rate in zip(samples,rates):
        print(sample)
        with open("sps_trials_cont.txt", "a") as myfile:
            myfile.write(str(sample))
            myfile.write("\n")
        x = np.arange(10)
        #s0,s1,s2 = sample
        #plt.figure(figsize=(12,15))
        #plt.subplot(311)
        #plt.plot(s0)
        #plt.xlabel("Trials")
        #plt.ylabel("SPS")
        #plt.title(f"Z Rates at {rate} SPS")
        #plt.subplot(312)
        #plt.plot(s1)
        #plt.xlabel("Trials")
        #plt.ylabel("SPS")
        #plt.title(f"X? Rates at {rate} SPS")
        #plt.subplot(313)
        #plt.plot(s2)
        #plt.xlabel("Trials")
        #plt.ylabel("SPS")
        #plt.title(f"Y? Rates at {rate} SPS")
        #plt.tight_layout()
        #plt.savefig(f"Figures/{rate}_SPS_trials.jpg")

        #plt.figure(figsize=(12,5))
        #plt.plot(sample,"k.")
        #plt.axhline(y=rate,c="r")
        #plt.axhline(y=rate*1.10,c="g")
        #plt.axhline(y=rate*0.9,c="g")
        #plt.xlabel("Trials",fontsize=16,fontweight="bold")
        #plt.ylabel("Samples per Second",fontsize=16,fontweight="bold")
        #plt.title(f"True SPS for {rate} SPS",fontsize=16,fontweight="bold")
        #plt.savefig(f"{rate}_full_trial.jpg")
        #plt.show()
        #plt.close()
#print(len(voltages)/dt,dt)
    #print(len(voltages))

if __name__ == "__main__":
    main()
