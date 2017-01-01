from eth import *
from arp import *

def PrintFrame(frameAsHexArray):
    print('[*] Frame:')
    print('[+]                                 ' + str(frameAsHexArray[0:6]))
    print('[+]                                 ' + str(frameAsHexArray[6:12]))
    print('[+]                                 ' + str(frameAsHexArray[12:18]))
    print('[+]                                 ' + str(frameAsHexArray[12:18]))
    print('[+]                                 ' + str(frameAsHexArray[18:24]))
    print('[+]                                 ' + str(frameAsHexArray[24:30]))
    print('[+]                                 ' + str(frameAsHexArray[30:36]))
    print('[+]                                 ' + str(frameAsHexArray[36:42]))
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
