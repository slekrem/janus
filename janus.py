import socket

from janusAlertBoard import JanusAlert
from frame import *
from eth import *
from arp import * 

def PrintFrame(frameAsHexArray):
    print('[*] Frame:')
    print('[+] ' + str(frameAsHexArray))
    print('')

def PrintEth(ethAsHexArray):
    print('[*] Ethernet:')
    print('[+]     Destination MAC address:    ' + str(GetEthDestinationMacAddressAsHexArray(ethAsHexArray)))
    print('[+]     Source MAC address:         ' + str(GetEthSourceMacAddressAsHexArray(ethAsHexArray)))
    print('[+]     Type:                       ' + str(GetEthTypeAsHexArray(ethAsHexArray)))
    print('')

def PrintArp(arpAsHexArray):
    print('[*] Address Resolution Protocol:')
    print('[+]     Hardware type:              ' + str(GetArpHardwareTypeAsHexArray(arpAsHexArray)))
    print('[+]     Protocol type:              ' + str(GetArpProtocolTypeAsHexArray(arpAsHexArray)))
    print('[+]     Hardware size:              ' + str(GetArpHardwareSizeAsHexArray(arpAsHexArray)))
    print('[+]     Protocol size:              ' + str(GetArpProtocolSizeAsHexArray(arpAsHexArray)))
    print('[+]     Opcode:                     ' + str(GetArpOpcodeAsHexArray(arpAsHexArray)))
    print('[+]     Sender Mac Address:         ' + str(GetArpSenderMacAddressAsHexArray(arpAsHexArray)))
    print('[+]     Sender Ip Address:          ' + str(GetArpSenderIpAddressAsHexArray(arpAsHexArray)))
    print('[+]     Target Mac Address:         ' + str(GetArpTargetMacAddressAsHexArray(arpAsHexArray)))
    print('[+]     Target Ip Address:          ' + str(GetArpTargetIpAddressAsHexArray(arpAsHexArray)))
    print('')
    

def Main():
    packetSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    packetSocket.bind(("wlan0", 0x0806))
    janusAlert = JanusAlert()
    while True:
        frameAsShellCode = packetSocket.recvfrom(2048)[0]
        if not frameAsShellCode:
            break
        frameAsHexArray = GetFrameAsHexArray(frameAsShellCode)
        
        PrintFrame(frameAsHexArray)
        PrintEth(frameAsHexArray[0:])
        PrintArp(frameAsHexArray[14:])
        janusAlert.alert(0.1)

    arpSocket.close()

if __name__ == "__main__":
    Main()
