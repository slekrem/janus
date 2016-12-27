#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

class Photoresistor(object):
    _resistorPin = -1

    def __init__(self, pin):
        self._resistorPin = pin
        
        if(self._resistorPin >= 0):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self._resistorPin, GPIO.IN)

    def getStatus(self):
        if(GPIO.input(self._resistorPin) == GPIO.HIGH):
            return True #HIGH
        else:
            return False #LOW

    def test(self):
        for count in xrange(0, 100):
            if(GPIO.input(self._resistorPin) == GPIO.LOW):
                print "LOW"
                time.sleep(1)
            else:
                print "HIGH"
                time.sleep(1)
        GPIO.cleanup()
            
                
