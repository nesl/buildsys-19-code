"""
    The parser for the module spect sheets.
"""

from Abstraction import Abstraction

class Module:
    def __init__(self, name):
        self.abstractions = dict() # All name in string for the abstractions
        self.name = name

    def cost(self):
        #TODO: Add the cost function for this specific abstraction
        return 1

    def addAbstraction(self, abstraction):
        for instance in abstraction.childDeviceInstance:
            instance.addParentsInfo(self.name)
        self.abstractions[abstraction.name] = abstraction

    def callFunc(self, name):
        self.abstractions[name].performFunc()

    def getAbstraction(self, name):
        return self.abstractions[name]

    def getAbstractionList(self):
        return self.abstractions
