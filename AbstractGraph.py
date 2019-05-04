import abc
from Abstraction import *
from typing import List

"""
    The abstraction graph of the data structure.
"""
class AbstractGraph:

    abstractions: List[Abstraction] = dict()
    devices: List[DeviceInstance] = dict()

    def __init__ (self):
        return

    '''
        Adds a new abstraction to the graph. This assumes that the control system developer
        will provide lists of the names of both the children and the parents of an abstraction.
        We can imagine an interface where the control system developer can select which
        abstractions are parents/children and pass the names (IDs)  to this function accordingly.
    '''
    def addAbstraction(self, name, abstraction):
        if abstraction.name in self.abstractions.keys():
            print('abstraction name is duplicated. Change one')
            return 1
        self.abstractions[abstraction.name] = abstraction
        return 0

    """
        Note: After the abstraction is deleted. It does not delete its dependency.
        The dependencies rely on this should be updated at the runtime when accessing
        them.
    """
    def deleteAbstraction(self,abstraction):
        del self.abstractions[abstraction.name]
        return 0

    def addDeviceInstance(self, deviceInstance):
        if deviceInstance.name in self.devices.keys():
            print('device name is duplicated. Change one')
            return 1

        self.devices[deviceInstance.name] = deviceInstance

    def getAbstractionList(self):
        return self.abstractions
    ##############################
    # Starting testing functions #
    ##############################
    def clear(self):
        self.abstractions.clear()


def testAddChildrenAndParents():
    graph = AbstractGraph()
    device1 = DeviceAbstraction(AbstractionSpecification(10.0, 100, 100,), "Device1")
    graph.addAbstraction(device1)
    device2 = DeviceAbstraction(AbstractionSpecification(11.0, 100, 100,), "Device2")
    graph.addAbstraction(device2, ["Device1"])
    device3 = DeviceAbstraction(AbstractionSpecification(12.0, 100, 100,), "Device3")
    graph.addAbstraction(device3, None, ["Device2"])
    print("Device1: \n***********\n", device1)
    print("\nDevice2: \n***********\n", device2)
    print("\nDevice3: \n***********\n", device3)


if __name__ == "__main__":
    # print("What the fuck I am doing here!")
    # testRegister()
    testAddChildren()
