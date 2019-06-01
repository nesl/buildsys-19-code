import sys
from IFTTTParsing import ConditionStruct, IFTTTParser
from DependencyGraph import GraphNode,is_compatible_or_identical,DependencyGraphClass
from AbstractGraph import *
from EvalRemedialEngine import *
from RemedialEngine import main as obtain_remedial_action

PRIORITY_SAFETY = 0
PRIORITY_ENERGY = 1
PRIORITY_USABILITY = 2
PRIORITY_DEFAULT = PRIORITY_USABILITY

class EventNode:
    def __init__(self, event, priority, remedial_action_index=-1, block=False):
        self.event = event
        self.remedial_action_index = remedial_action_index
        self.block = block
        self.priority = priority

if __name__ == '__main__':
    events_database = set()
    remedial_action_database = []
    print("Please enter the rule(s)")
    dependencyGraph = DependencyGraphClass()
    evalGraph = EvalActuationGraph()
    rules = ['if user.home = 1 then door.state = 0', 'if user.home = 1 then door.state = 1']
    priority_list = dict()
    priority_list['safety'] = PRIORITY_SAFETY
    priority_list['energy'] = PRIORITY_ENERGY
    priority_list['usability'] = PRIORITY_USABILITY
    priority_list['default'] = PRIORITY_DEFAULT
    # for rule in sys.stdin:
    for rule in rules:
        rule_raw = rule.strip()
        rule = rule_raw.split(',')[0]
        priority = PRIORITY_DEFAULT

        if len(rule_raw.split(',')) == 2:
            priority = priority_list(rule_raw.split(',')[1])

        rule_tuple = IFTTTParser(rule, {})
        conflict = dependencyGraph.add(rule_tuple, remove=False)

        if conflict is not None:
            conflict_devices_names = set()
            for entry in conflict:  # entry is a link
                for connection in entry: # connection is a tuple
                    # for condition in connection[0]:
                        # condition.printConditionStruct()
                        # print("({} {} {})".format(condition.subject, condition.operator, condition.value))
                    # print("->")
                    for action in connection[1]:
                        # action.printConditionStruct()
                        # print("({} {} {})".format(action.subject, action.operator, action.value))
                        name = action.subject.split('.')[0]
                        conflict_devices_names.add(name)
            for name in conflict_devices_names:
                conflict_devices = evalGraph.graph.getDeviceInstance(name)
                remedial_action = obtain_remedial_action(evalGraph.graph, conflict_devices, dependencyGraph=dependencyGraph, conflict_condition=rule.split('then')[0])
                event = None
                if remedial_action is None:
                    event = EventNode(rule, priority, block=True)
                else:
                    event = EventNode(rule, priority, remedial_action_index=len(remedial_action_database))
                    remedial_action_database.append(remedial_action)
                events_database.add(event)
                print(remedial_action)
        else:
            event = EventNode(rule, priority)
            events_database.add(event)
