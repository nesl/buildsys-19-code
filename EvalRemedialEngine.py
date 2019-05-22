'''
    The evaluation of remediot!
'''

from UserInterface import *
from AbstractGraph import *
from Abstraction import *


class EvalActuationGraph:

    class WindowInstance(DeviceInstance):
        def __init__(self):
            deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
            DeviceInstance.__init__(self, True, 'windows', deviceInfo)

    class AirConditionerInstance(DeviceInstance):
        def __init__(self):
            deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
            DeviceInstance.__init__(self, True, 'ac', deviceInfo)

    class FanInstance(DeviceInstance):
        def __init__(self):
            deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
            DeviceInstance.__init__(self, True, 'fan', deviceInfo)


    class AirConditionerTurnOn(Abstraction):
        def __init__(self):
            Abstraction.__init__(self, 'turn on air conditioner', 'cooling down', 0, ACTUATION)
            acInstance = AirConditionerInstance()
            super(AirConditionerTurnOn, self).appendChildDeviceInstance(acInstance)

        def performFunc(self, *args):
            print('Turning on the HVAC now')

    class WindowOpening(Abstraction):
        def __init__(self):
            Abstraction.__init__(self, 'open the window', 'cooling down', 0, ACTUATION)
            windowInstance = WindowInstance()
            super(WindowOpening, self).appendChildDeviceInstance(windowInstance)

        def performFunc(self, *args):
            print('Opening the window now.')

    class FanTurnOn(Abstraction):
        def __init__(self):
            Abstraction.__init__(self, 'turn on fan', 'cooling down', 0, ACTUATION)
            fanInstance = FanInstance()
            super(FanTurnOn, self).appendChildDeviceInstance(fanInstance)

        def performFunc(self, *args):
            print('Turning on the fan now')


    class CoolDownModule(Module):
        def __init__(self):
            Module.__init__(self, 'cooling down')
            acTurnOn = AirConditionerTurnOn()
            fanTurOn = FanTurnOn()
            windowOpening = WindowOpening()
            super(CoolDownModule, self).addAbstraction(acTurnOn)
            super(CoolDownModule, self).addAbstraction(fanTurOn)
            super(CoolDownModule, self).addAbstraction(windowOpening)

    def __init__(self):
        pass
