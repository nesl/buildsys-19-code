import abc
from Abstraction import *
from typing import List
from ModuleSpecParser import Module
from pprint import pprint

SENSING = 0
ACTUATION = 1

"""
    The abstraction graph of the data structure.
"""
class ActuationGraph:

    modules: List[Module] = dict()
    devices: List[DeviceInstance] = dict()

    def __init__ (self):
        return

    '''
        Adds a new abstraction to the graph. This assumes that the control system developer
        will provide lists of the names of both the children and the parents of an abstraction.
        We can imagine an interface where the control system developer can select which
        abstractions are parents/children and pass the names (IDs)  to this function accordingly.
    '''
    def addModule(self, module):
        if module.name in self.modules.keys():
            print('abstraction name is duplicated. Change one')
            return 1
        self.modules[module.name] = module
        if module.getAbstractionList():
            for name, abs in module.getAbstractionList().items():
                if not abs.childDeviceInstance:
                    continue

                for deviceInstance in abs.childDeviceInstance:
                    self.devices[deviceInstance.name] = deviceInstance

        return 0

    """
        Note: After the abstraction is deleted. It does not delete its dependency.
        The dependencies rely on this should be updated at the runtime when accessing
        them.
    """
    def deleteAbstraction(self, module):
        del self.modules[module.name]
        return 0

    def addDeviceInstance(self, deviceInstance):
        if deviceInstance.name in self.devices.keys():
            print('device name is duplicated. Change one')
            return 1

        self.devices[deviceInstance.name] = deviceInstance

    def getModule(self, name):
        return self.modules[name]

    def getModuleList(self):
        return self.modules

    def getDeviceInstance(self, name):
        return self.devices[name]

def testAddChildren():
    class HvacDevice(DeviceInstance):
        def __init__(self):
            deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
            DeviceInstance.__init__(self, True, 'This is HVAC instance', deviceInfo)

    class HvacAbstraction(Abstraction):
        def __init__(self):
            Abstraction.__init__(self, 'turn-on-hvac', 'cooling-down', 0, ACTUATION)
            hvacDevice = HvacDevice()
            super(HvacAbstraction, self).appendChildDeviceInstance(hvacDevice)

        def performFunc(self, *args):
            print('I am turning on HVAC')

    graph = ActuationGraph()
    hvacAbs = HvacAbstraction()
    graph.addAbstraction(hvacAbs)
    pprint(graph.modules)
    # device1 = DeviceAbstraction(AbstractionSpecification(10.0, 100, 100,), "Device1")
    # graph.addAbstraction(device1)
    # device2 = DeviceAbstraction(AbstractionSpecification(11.0, 100, 100,), "Device2")
    # graph.addAbstraction(device2, ["Device1"])
    # device3 = DeviceAbstraction(AbstractionSpecification(12.0, 100, 100,), "Device3")
    # graph.addAbstraction(device3, None, ["Device2"])
    # print("Device1: \n***********\n", device1)
    # print("\nDevice2: \n***********\n", device2)
    # print("\nDevice3: \n***********\n", device3)


if __name__ == "__main__":
    # print("What the fuck I am doing here!")
    # testRegister()
    testAddChildren()
