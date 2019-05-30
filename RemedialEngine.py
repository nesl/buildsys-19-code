"""
    Remedial Action Engine.
"""

from UserInterface import *
from AbstractGraph import *
from Abstraction import *

def main(actuationGraph, conflictNode):
    intention = set()

    for parent in conflictNode.parentAbstractions:
        print(parent)
        intention.add(parent)

    if not intention:
        return None

    selected = selectIntention(intention)
    if selected is None:
        return None

    selectedModule = actuationGraph.getModule(selected)
    allAbstractions = selectedModule.getAbstractionList()

    remedialActions = set()

    for abstraction in allAbstractions:
        if abstraction != conflictNode and not checkConflict(abstraction):
            remedialActions.add(abstraction)

    if not remedialActions:
        return None

    remedialActions = rankActions(selectedModule, remedialActions)
    # If remove actions, modify the text of the actions.
    action = displayRemedialActions(remedialActions)
    return action

#TODO: Connect this with conflict detector.
def checkConflict(node):
    return False

#TODO: Rank the remedial actions based on their costs
def rankActions(module, actions):
    return actions

def removeActions(events, conflictList):
    return events

def groupEvents(events):
    grouped = dict()
    for event in events:
        if not grouped[event.label]:
            grouped[event.label] = list()
        grouped[event.label].append(event)
    return grouped

def testRemdedialEngine():
    class HvacDevice(DeviceInstance):
        def __init__(self):
            deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
            DeviceInstance.__init__(self, True, 'HVAC-instance', deviceInfo)

    class HvacAbstraction(Abstraction):
        def __init__(self):
            Abstraction.__init__(self, 'turn-on-hvac', 'cooling-down', 0, ACTUATION)
            hvacDevice = HvacDevice()
            super(HvacAbstraction, self).appendChildDeviceInstance(hvacDevice)

        def performFunc(self, *args):
            print('I am turning on HVAC')

    class FanAbstraction(Abstraction):
        def __init__(self):
            Abstraction.__init__(self, 'turn-on-fan', 'cooling-down', 0, ACTUATION)
            hvacDevice = HvacDevice()
            super(FanAbstraction, self).appendChildDeviceInstance(hvacDevice)

        def performFunc(self, *args):
            print('I am turning on HVAC')

    class CoolDownModule(Module):
        def __init__(self):
            Module.__init__(self, 'cooling-down')
            hvacAbs = HvacAbstraction()
            fanAbs = FanAbstraction()
            super(CoolDownModule, self).addAbstraction(hvacAbs)
            super(CoolDownModule, self).addAbstraction(fanAbs)

    graph = ActuationGraph()
    cooldownMod = CoolDownModule()

    graph.addModule(cooldownMod)
    conflictNode = graph.getDeviceInstance('HVAC-instance')
    print(main(graph, conflictNode))

if __name__ == '__main__':
    testRemdedialEngine()
