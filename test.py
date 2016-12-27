#!/usr/bin/env python

from janus_alert import JanusAlert
from photoresistor import Photoresistor
import RPi.GPIO as GPIO
import time

"""
red = 13
green = 11
blue = 15
"""

if __name__ == '__main__':
    try:     
       janus = JanusAlert()
       janus.test()

        
 
    except KeyboardInterrupt:
        GPIO.cleanup()
