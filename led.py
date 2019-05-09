import RPi.GPIO as GPIO
import time

pin = 18

def pulse():
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.5)

def initialize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)

initialize()

def turn_on():
    initialize()
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    #GPIO.cleanup()

def turn_off():
    #initialize()
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

if __name__ == "__main__":
    for i in range(2):
        pulse()
