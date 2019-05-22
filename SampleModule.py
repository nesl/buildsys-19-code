# Import the existing modules
from AbstractGraph import *

# Implementation for cooling down by turning on the AC
class AirConditionerTurnOn(Abstraction):
    def __init__(self):
        Abstraction.__init__(...)
        acInstance = AirConditionerInstance()
        super(AirConditionerTurnOn, self).appendChildDeviceInstance(acInstance)

    def performFunc(self, *args):
        # Perform the specific action to turn on AC
        ...

# Actuation Module
class CoolDownModule(Module):
    def __init__(self):
        Module.__init__(...)
        acTurnOn = AirConditionerTurnOn()
        fanTurOn = FanTurnOn()
        super(CoolDownModule, self).addAbstraction(acTurnOn)
