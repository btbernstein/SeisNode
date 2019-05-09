import RPi.GPIO as GPIO
import time

pin = 18 

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)  
GPIO.output(pin, GPIO.HIGH)

def turn_on():
    GPIO.output(pin, GPIO.HIGH)
 
def turn_off():
    GPIO.output(pin, GPIO.LOW)

def blink():
  while True:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
