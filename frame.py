import binascii

def GetFrameAsHexArray(frameAsShellCode):
    frameAsHexString = binascii.hexlify(frameAsShellCode).decode()
    frameAsHexArray = [frameAsHexString[i:i+2] for i in range(0, len(frameAsHexString), 2)]
    return frameAsHexArray
