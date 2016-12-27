#!/usr/bin/env python

from GPIOService import GPIOService

class ActiveBuzzer(GPIOService):
    _buzzerPin = -1

    def __init__(self, buzzerPin):
        self._buzzerPin = buzzerPin

        pinList = [self._buzzerPin]
        GPIOService.__init__(self, pinList)

    def turnBuzzerOn(self):
        self.turnDigitalOn(self._buzzerPin)

    def turnBuzzerOff(self):
        self.turnDigitalOff(self._buzzerPin)

    def destroy(self):
        self.destroyGPIO()
    
