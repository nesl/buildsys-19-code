"""
    Remedial Action Engine.
"""

from UserInterface import *
from AbstractGraph import *
from Abstraction import *
from IFTTTParsing import ConditionStruct, IFTTTParser

def main(actuationGraph, conflictNode, conflict_condition = None, dependencyGraph = None, test=True):

    if not conflictNode:
        return None, None

    intention = []

    for parent in conflictNode.parentAbstractions:
        intention.append(parent)

    if not intention:
        return None

    print(conflict_condition)
    intention = list(intention)
    intention = sorted(intention)

    # Detect the given intention might not have any remedial actions.
    intention_candidate = []
    for intent in intention:
        moduleCandidate = actuationGraph.getModule(intent)
        absCandidate = moduleCandidate.getAbstractionList()
        addToCandidate = False
        for abst in absCandidate:
            if abst != conflictNode and not checkConflict(moduleCandidate.getAbstraction(abst), dependencyGraph, conflict_condition):
                addToCandidate = True
        if addToCandidate:
            intention_candidate.append(intent)

    if not test:
        selected = selectIntention(intention_candidate)
    else:
        selected = None if len(intention_candidate) == 0 else intention_candidate[0]

    if not selected:
        return None, None

    selectedModule = actuationGraph.getModule(selected)
    allAbstractions = selectedModule.getAbstractionList()

    remedialActions = []

    for abstraction in allAbstractions:
        if abstraction != conflictNode and not checkConflict(selectedModule.getAbstraction(abstraction), dependencyGraph, conflict_condition):
            remedialActions.append(abstraction)

    if not remedialActions:
        return None, None

    rankedActions = rankActions(selectedModule, remedialActions)
    # If remove actions, modify the text of the actions.
    if not test:
        action = displayRemedialActions(rankedActions)
    else:
        action = rankedActions[0]
    return action, selectedModule.getAbstraction(action).performFunc()

def checkConflict(node, dependencyGraph, conflict_condition):
    rule = conflict_condition + 'then ' + node.performFunc()
    # print(rule)
    rule_tuple = IFTTTParser(rule, {})
    if dependencyGraph.add(rule_tuple, remove=False):
        return True
    return False

def rankActions(module, actions):
    ranked = []
    for action in actions:
        ranked.append(action)
    ranked = sorted(ranked, reverse=True, key=lambda name:module.getAbstraction(name).cost)
    return ranked

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
