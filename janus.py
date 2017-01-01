import socket
import os

from frame import *
from arpDetector import *
from janusAlertBoard import JanusAlert

clear = lambda: os.system('clear')

def Main():
    packetSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    packetSocket.bind(("wlan0", 0x0806))
    janusAlert = JanusAlert()
    while True:
        frameAsShellCode = packetSocket.recvfrom(2048)[0]
        if not frameAsShellCode:
            break
        frameAsHexArray = GetFrameAsHexArray(frameAsShellCode)

        clear()
        PrintFrame(frameAsHexArray)
        PrintEth(frameAsHexArray[0:])
        PrintArp(frameAsHexArray[14:])
        janusAlert.alert(0.1)

    arpSocket.close()

if __name__ == "__main__":
    Main()
