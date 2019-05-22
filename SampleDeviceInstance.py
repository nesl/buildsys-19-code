# Import the existing modules
from AbstractGraph import *

class HeaterInstance(DeviceInstance):
    def __init__(self):
        deviceInfo = DeviceInfo(...) #The device information
        DeviceInstance.__init__(self, True, 'heater', deviceInfo)
