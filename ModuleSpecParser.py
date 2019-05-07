"""
    The parser for the module spect sheets.
"""

from Abstraction import Abstraction

class Module:
    name = ''
    abstractions = dict() # All name in string for the abstractions

    def __init__(self, name):
        self.name = name

    def cost(self):
        #TODO: Add the cost function for this specific abstraction
        return 1

    def addAbstraction(self, abstraction):
        self.abstractions[abstraction.name] = abstraction

    def callFunc(self, name, *args):
        self.abstractions[name].performFunc(*args)

def testModuleSpectSheet():
    #TODO: Add the test function here.
    return

class TurnOnAC(Abstraction):
    def __init__ ():
        pass

if __name__ == "__main__":
    testModuleSpectSheet()
