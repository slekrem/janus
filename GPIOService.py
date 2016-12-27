#!/usr/bin/env python

import RPi.GPIO as GPIO

class GPIOService(object):
    _digitalPinList = []

    def __init__(self, digitalPinList):
        self.addDigitalPins(digitalPinList)
        self.setupDigital()

    def addDigitalPin(self, pin):
        self._digitalPinList.append(pin)

    def addDigitalPins(self, pinList):
        for pin in pinList:
            self.addDigitalPin(pin)
        
    def setupDigital(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in self._digitalPinList:
            GPIO.setup(pin, GPIO.OUT)
            self.turnDigitalOff(pin)

    def turnDigitalOn(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def turnDigitalOff(self, pin):
        GPIO.output(pin, GPIO.LOW)

    def setupPwmPin(self, pin):
        pwmPin = GPIO.PWM(pin, 100) # set 100 Hertz
        return pwmPin

    def destroyGPIO(self):
        for pin in self._digitalPinList:
            self.turnDigitalOff(pin)
        GPIO.cleanup()
