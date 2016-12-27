#!/usr/bin/env python

from GPIOService import GPIOService
import time

class RgbLed(GPIOService):
    _redPin = -1
    _greenPin = -1
    _bluePin = -1
    
    def __init__(self, redPin, greenPin, bluePin):
        self._redPin = redPin
        self._greenPin = greenPin
        self._bluePin = bluePin

        pinList = [self._redPin, self._greenPin, self._bluePin]
        GPIOService.__init__(self, pinList)
    
    def turnRedOn(self):
        self.turnDigitalOn(self._redPin)

    def turnRedOff(self):
        self.turnDigitalOff(self._redPin)

    def turnGreenOn(self):
        self.turnDigitalOn(self._greenPin)

    def turnGreenOff(self):
        self.turnDigitalOff(self._greenPin)

    def turnBlueOn(self):
        self.turnDigitalOn(self._bluePin)

    def turnBlueOff(self):
        self.turnDigitalOff(self._bluePin)

    def turnMagentaOn(self):
        self.turnDigitalOn(self._bluePin)
        self.turnDigitalOn(self._redPin)

    def turnMagentaOff(self):
        self.turnDigitalOff(self._bluePin)
        self.turnDigitalOff(self._redPin)

    def turnCyanOn(self):
        self.turnDigitalOn(self._bluePin)
        self.turnDigitalOn(self._greenPin)

    def turnCyanOff(self):
        self.turnDigitalOff(self._bluePin)
        self.turnDigitalOff(self._greenPin)

    def turnYellowOn(self):
        self.turnDigitalOn(self._redPin)
        self.turnDigitalOn(self._greenPin)

    def turnYellowOff(self):
        self.turnDigitalOff(self._redPin)
        self.turnDigitalOff(self._greenPin)

    def turnWhiteOn(self):
        self.turnDigitalOn(self._redPin)
        self.turnDigitalOn(self._greenPin)
        self.turnDigitalOn(self._bluePin)

    def turnWhiteOff(self):
        self.turnDigitalOff(self._redPin)
        self.turnDigitalOff(self._greenPin)
        self.turnDigitalOff(self._bluePin)

    def ledBreathe(self, pin, speedInSeconds):
        pwmPin = self.setupPwmPin(pin)
        self.ledBreatheIn(pwmPin, speedInSeconds)
        self.ledBreatheOut(pwmPin, speedInSeconds)

    def ledBreatheIn(self, pwmPin, speedInSeconds):
        for dutyCycle in xrange(0,25):
            pwmPin.start(dutyCycle)
            time.sleep(speedInSeconds)
            
    def ledBreatheOut(self, pwmPin, speedInSeconds):
        for dutyCycle in xrange(25, 0, -1):
            pwmPin.start(dutyCycle)
            time.sleep(speedInSeconds)
        
        pwmPin.stop()
        time.sleep(15)

    def test(self):
        self.turnRedOn()
        time.sleep(1)
        self.turnRedOff()
        self.turnGreenOn()
        time.sleep(1)
        self.turnGreenOff()
        self.turnBlueOn()
        time.sleep(1)
        self.turnBlueOff()
        self.turnYellowOn()
        time.sleep(1)
        self.turnYellowOff()
        self.turnCyanOn()
        time.sleep(1)
        self.turnCyanOff()
        self.turnMagentaOn()
        time.sleep(1)
        
        self.turnMagentaOff()
        self.turnWhiteOn()
        time.sleep(1)
        self.turnWhiteOff()
        time.sleep(1)
        self.turnWhiteOn()
        time.sleep(1)
        self.turnWhiteOff()
        time.sleep(1)
        self.turnWhiteOn()
        time.sleep(1)
        self.turnWhiteOff()
        time.sleep(1)
        
    def destroy(self):
        self.destroyGPIO()
