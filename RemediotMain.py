import sys
from IFTTTParsing import ConditionStruct, IFTTTParser
from DependencyGraph import GraphNode,is_compatible_or_identical,DependencyGraphClass
from AbstractGraph import *
from EvalRemedialEngine import *
from RemedialEngine import main as obtain_remedial_action
import time

PRIORITY_SAFETY = 0
PRIORITY_ENERGY = 1
PRIORITY_USABILITY = 2
PRIORITY_DEFAULT = PRIORITY_USABILITY

PRIORITY_TABLE = dict()

class EventNode:
    def __init__(self, event, priority, remedial_action_index=-1, block=False):
        self.event = event
        self.remedial_action_index = remedial_action_index
        self.block = block
        self.priority = priority

def generateResults(events_database, remedial_action_database, total_app):
    conflict = 0
    remedial_action = 0
    blocked = 0
    total = 0
    for event in events_database:
        if event.block:
            blocked += 1
        if event.remedial_action_index != -1:
            remedial_action += 1
        if event.block or event.remedial_action_index != -1:
            conflict += 1
        total += 1

    if remedial_action != len(remedial_action_database):
        print('Error! Remedial events do not equal to action databse size')

    print('###########################################')
    print('Total Apps: ' + str(total_app))
    print('Total Events: ' + str(total))
    print('Total Conflicts: ' + str(conflict))
    print('Blocked Events: ' + str(blocked))
    print('Total Remedial Actions: ' + str(remedial_action))
    print('Conflict Percentage: ' + str(round(float(conflict)/float(total)*100, 2)))
    print('Blocked Percentage out of Conflicts: ' + str(round(float(blocked)/float(conflict)*100, 2)))
    print('Remedial Action Percentage out of Conflicts: ' + str(round(float(remedial_action)/float(conflict)*100, 2)))
    print('###########################################')

def evalNumberOfModules():
    number_of_testing = [10, 100, 1000, 10000, 100000]
    for i in number_of_testing:
        with open('results/' + str(i)+'.txt', 'a+') as fh:
            for j in range(0,50):
                time_start = time.time()
                dummy_graph = EvalActuationGraph(True, i)
                time_end = time.time()
                fh.write(str(round((time_end-time_start)*1000, 2)))
                fh.write('\n')

def evalNumberOfRemedialActions():
    remedial_action_number = [10, 100, 1000, 10000]
    number_of_modules = [10, 100, 1000, 10000, 100000]
    rule = 'if user.home = 1 then door.state = 0'
    for module_num in number_of_modules:
        dummy_graph = EvalActuationGraph(True, module_num)
        dependencyGraph = DependencyGraphClass()
        dependencyGraph.add(IFTTTParser(rule, {}))
        for remedial_number in remedial_action_number:
            conflict_devices = dummy_graph.graph.getDeviceInstance('door')
            with open('results/remedial-abstraction/'
                + 'module-'
                + str(module_num)
                + '-action-'
                + str(remedial_number) + '.txt', 'a+') as fh:
                    for i in range(0,50):
                        time_start = time.time()
                        for i in range(0, remedial_number):
                            remedial_action, remedial_state = obtain_remedial_action(dummy_graph.graph, conflict_devices,
                                dependencyGraph=dependencyGraph,
                                conflict_condition='if user.home = 1 ')
                        time_end = time.time()
                        fh.write(str(round((time_end-time_start)*1000, 2)))
                        fh.write('\n')


def main(fileName='rules.txt'):
    events_database = set()
    remedial_action_database = []
    dependencyGraph = DependencyGraphClass()
    evalGraph = EvalActuationGraph()
    rules = ['if user.home = 1 then door.state = 0', 'if user.home = 1 then door.state = 1']
    priority_list = dict()
    priority_list['safety'] = PRIORITY_SAFETY
    priority_list['energy'] = PRIORITY_ENERGY
    priority_list['usability'] = PRIORITY_USABILITY
    priority_list['default'] = PRIORITY_DEFAULT

    fh = open(fileName, 'r')
    total_app = 0
    # for rule in sys.stdin:
    for rule in fh:
        if '##' in rule:
            total_app += 1
            continue
        rule_raw = rule.strip()
        rule = rule_raw.split(',')[0]
        priority = PRIORITY_DEFAULT

        # print(rule)
        if len(rule_raw.split(',')) == 2:
            priority = priority_list[rule_raw.split(',')[1]]

        rule_tuple = IFTTTParser(rule, {})
        conflict = dependencyGraph.add(rule_tuple)
        PRIORITY_TABLE[rule] = priority

        if conflict is not None:
            conflict_devices_names = []
            conflict_events = []
            # print('=====================================')
            for entry in conflict:  # entry is a link
                for connection in entry: # connection is a tuple
                    recovered_event = ''
                    for condition in connection[0]:
                        recovered_event = recovered_event + ' and ' + condition.subject + ' ' + condition.operator + ' ' + condition.value
                        # condition.printConditionStruct()
                        # print("({} {} {})".format(condition.subject, condition.operator, condition.value))
                    # print("->")
                    recovered_event = 'if ' + recovered_event[5:] + ' '
                    recovered_action = ''
                    for action in connection[1]:
                        # action.printConditionStruct()
                        # print("({} {} {})".format(action.subject, action.operator, action.value))
                        recovered_action = recovered_action + ' and ' + action.subject + ' ' + action.operator + ' ' + action.value
                        name = action.subject.split('.')[0]
                        if name not in conflict_devices_names:
                            conflict_devices_names.append(name)
                    # print('----------------------------')
                    recovered_event = recovered_event + 'then ' + recovered_action[5:]
                    conflict_events.append(recovered_event)
            # print('=====================================')

            if PRIORITY_TABLE[conflict_events[-1]] <= PRIORITY_TABLE[conflict_events[0]]:
                for e in conflict_events[:-1]:
                    if dependencyGraph.add(IFTTTParser(e, {})):
                        print('THERE ARE ERRORS IN THE ALGORITHM!!!!!')
                        sys.exit()
                    conflict_devices_names = conflict_devices_names[-1:]
            else:
                if dependencyGraph.add(IFTTTParser(conflict_events[-1], {})):
                    print('THERE ARE ERRORS IN THE ALGORITHM!!!!!')
                    sys.exit()
                conflict_devices_names = conflict_devices_names[:-1]

            for name in conflict_devices_names:
                conflict_devices = evalGraph.graph.getDeviceInstance(name)
                remedial_action, remedial_state = obtain_remedial_action(evalGraph.graph, conflict_devices, dependencyGraph=dependencyGraph, conflict_condition=rule.split('then')[0])
                event = None
                if remedial_action is None:
                    event = EventNode(rule, priority, block=True)
                else:
                    event = EventNode(rule, priority, remedial_action_index=len(remedial_action_database))
                    remedial_action = rule.split('then')[0] + 'then ' + remedial_state
                    # print(remedial_action)
                    # print('**********************************')
                    rule_tuple = IFTTTParser(remedial_action, {})
                    conflict = dependencyGraph.add(rule_tuple, remove=False)
                    if conflict:
                        print('ERRORS! The remedial action should never have a conflict')
                        sys.exit()
                    remedial_action_database.append(remedial_action)
                    PRIORITY_TABLE[remedial_action] = priority
                events_database.add(event)
        else:
            event = EventNode(rule, priority)
            events_database.add(event)

    generateResults(events_database, remedial_action_database, total_app)
    # evalNumberOfModules()

if __name__ == '__main__':
    main()
    # evalNumberOfRemedialActions()
