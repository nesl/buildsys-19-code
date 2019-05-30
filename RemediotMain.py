import sys
from IFTTTParsing import ConditionStruct, IFTTTParser
from DependencyGraph import GraphNode,is_compatible_or_identical,DependencyGraphClass
from AbstractGraph import *
from EvalRemedialEngine import *
from RemedialEngine import main as obtain_remedial_action

PRIORITY_SAFETY = 0
PRIORITY_SECURITY = 1
PRIORITY_USABILITY = 2
PRIORITY_DEFAULT = PRIORITY_USABILITY

class EventNode:
    def __init__(self, event, remedial_action_index=-1, block=False):
        self.event = event
        self.remedial_action_index = remedial_action_index
        self.block = block

if __name__ == '__main__':
    print("Please enter the rule(s)")
    dependenceGraph = DependencyGraphClass()
    evalGraph = EvalActuationGraph()
    rules = ['if user.home = 1 then door.state = 0', 'if user.home = 1 then door.state = 1']
    # for rule in sys.stdin:
    for rule in rules:
        rule_raw = rule.strip()
        rule = rule_raw.split(',')[0]
        priority = PRIORITY_DEFAULT

        if len(rule_raw.split(',')) == 2:
            priority = rule_raw.split(',')[1]

        rule_tuple = IFTTTParser(rule, {})
        conflict = dependenceGraph.add(rule_tuple)
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
                print(conflict_devices)
                print(obtain_remedial_action(evalGraph.graph, conflict_devices))
            # print(conflict_devices_names)
