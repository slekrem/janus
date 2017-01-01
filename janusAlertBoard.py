#!/usr/bin/env python

from rgbLed import RgbLed
from active_buzzer import ActiveBuzzer
from photoresistor import Photoresistor
import time

"""
used pins

red = 15
green = 13
blue = 11

buzzer = 37
"""

class JanusAlert():
    _red = 15
    _green = 12
    _blue = 11
    _buzzer = 37
    _photoResistor = 35
    _alarmBuzzerActive = True

    def __init__(self):
        self._rgbLed = RgbLed(self._red, self._green, self._blue)
        self._buzzer = ActiveBuzzer(self._buzzer)
        self._photoResistor = Photoresistor(self._photoResistor)

    def resetAlert(self):
        self._alarmBuzzerActive = True

    def test(self):
        for x in xrange(0,100):
            self.alert(0.1)
            
    def alert(self, speedInSeconds):
        if(self._photoResistor.getStatus()):
            self._alarmBuzzerActive = False
        self.alertSignal(speedInSeconds)

    def arpPacketIncoming(self, speedInSeconds):
        self._rgbLed.turnMagentaOn()
        time.sleep(speedInSeconds)
        self._rgbLed.turnMagentaOff()
        time.sleep(speedInSeconds)

    def standby(self, speedInSeconds):
        self._rgbLed.ledBreathe(self._green, speedInSeconds)
        

        
    def alertSignal(self, speedInSeconds):
        if(self._alarmBuzzerActive):
            self._rgbLed.turnRedOn()
            self._buzzer.turnBuzzerOn()
        else:
            self._rgbLed.turnRedOn()
        time.sleep(speedInSeconds)

        if(self._alarmBuzzerActive):
            self._rgbLed.turnRedOff()
            self._buzzer.turnBuzzerOff()
        else:
            self._rgbLed.turnRedOff()
        time.sleep(speedInSeconds)

