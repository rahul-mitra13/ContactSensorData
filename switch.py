# servo control
import os
import time #library for sleep function
import RPi.GPIO as GPIO #library for Raspberry Pi output pins

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
    
