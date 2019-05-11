"""
    Remedial Action Engine.
"""

from UserInterface import *

def main(actuationGraph, conflictNode):
    intention = set()

    for parent in conflictNode.parentAbstractions:
        intention.add(parent.moduleName)

    if not intention:
        return None

    selected = selectIntention(intention)
    if selected is None:
        return None

    selectedModule = actuationGraph.getModuleList()
    allAbstractions = selectedModule.getAbstractionList()

    remedialActions = set()

    for abstraction in allAbstractions:
        if abstraction != conflictNode and not checkConflict(abstraction):
            remedialActions.add(abstraction.name)

    if not remedialActions:
        return None

    action = displayRemedialActions(remedialActions)
    return action

#TODO: Connect this with conflict detector.
def checkConflict(node):
    return False

def testRemdedialEngine():
    pass

if __name__ == '__main__':
    testRemdedialEngine()
