import abc
from typing import List,Set
import sys
from SpecParser import DeviceInfo

SENSING = 0
ACTUATION = 1

'''
    Abstraction classes:
'''
class Abstraction:
    def __init__(self, name, moduleName, initState, type):
        self.childAbstractions = set() # Abstraction Set using the name of string
        self.parentAbstractions = set() # Abstraction Set using the name of string
        self.cost = sys.maxsize
        self.childDeviceInstance = set() # DeviceInstance Set
        self.range = set()
        self.busy = False
        self.moduleName = moduleName
        self.name = name
        self.state = initState
        self.type = type

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def updateCost(self, cost):
        self.cost = cost

    def isBusy(self):
        return self.busy

    def setUsing(self):
        self.busy = True

    def releaseUsing(self):
        self.busy = False

    # This function needs to be overwritten by the child class
    def performFunc(self, *args):
        return

    def addRange(self, range):
        if range in self.range:
            return
        # range is the string
        self.range.add(range)
        for abs in childAbstraction:
            abs.addRange(range)

        for device in childDeviceInstance:
            device.tagRange(range)

    def appendChildDeviceInstance(self, childDeviceInstance):
        self.childDeviceInstance.add(childDeviceInstance)

    def appendChildAbstraction(self,childAbstraction):
        self.childAbstractions.add(childAbstraction)

    def appendParentAbstraction(self,parentAbstraction):
        self.parentAbstractions.add(parentAbstraction)

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
    def __init__(self, status, name, deviceInfo):
        self.parentAbstractions = set()
        self.name = name
        self.status = status # On or OFF. Or discrete value.
        self.deviceInfo = deviceInfo

    def addParentsInfo(self, parentModule):
        self.parentAbstractions.add(parentModule)

    def removeParentsInfo(self, parentModule):
        self.parentAbstractions.remove(parentModule)
