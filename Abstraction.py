import abc
from typing import List,Set
import sys

SENSING = 0
ACTUATION = 1

'''
    Abstraction classes:
'''
class Abstraction:
    name = ''
    childAbstractions = set() # Abstraction Set
    parentAbstractions = set() # Abstraction Set
    cost = sys.maxInt
    moduleName = ''
    childDeviceInstance = set() # DeviceInstance Set
    range = set()
    state = None
    type = -1

    def __init__(self, name, moduleName, initState, type):
        self.moduleName = moduleNname
        self.name = name
        self.state = initState
        self.type = type

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def updateCost(self, cost):
        self.cost = cost

    def addRange(self, range):
        if range in self.range:
            return
        # range is the string
        self.range.append(range)
        for abs in childAbstraction:
            abs.addRange(range)

        for device in childDeviceInstance:
            device.tagRange(range)

    def appendChildDeviceInstance(self, childDeviceInstance):
        self.childDeviceInstance.append(childDeviceInstance)

    def appendChildAbstraction(self,childAbstraction):
        self.childAbstractions.append(childAbstraction)

    def appendParentAbstraction(self,parentAbstraction):
        self.parentAbstractions.append(parentAbstraction)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.name == other.name)

    def __str__(self):
        abstractionStr = "Abstraction Name: "+self.name
        if self.childAbstractions is not None:
            abstractionStr = abstractionStr + "\n"+"Children:\n"
            for child in self.childAbstractions:
                abstractionStr = abstractionStr + "\t -"+child.name+"\n"
        if self.parentAbstractions is not None:
            abstractionStr = "Parents:\n"
            for parent in self.parentAbstractions:
                abstractionStr= abstractionStr + "\t -"+parent.name+"\n"
        return abstractionStr


class DeviceInstance:

    def __init__(self, status, name, range = None, parentAbstractions = None):
        self.name = name
        self.status = status # On or OFF. Or discrete value.
        self.parentAbstractions: Set[Abstraction] = parentAbstractions
        self.range = ''

    # Range is the string
    def tagRange(self, range):
        self.range.append(range)

    # Range is the string
    def removeRange(self, range):
        self.range.remove(range)
