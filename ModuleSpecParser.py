"""
    The parser for the module spect sheets.
"""

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
