from IFTTTParsing import ConditionStruct, IFTTTParser
import numpy as np
from DependencyGraph import GraphNode,is_compatible_or_identical,DependencyGraphClass


if __name__ == '__main__':
    fp = open("rules.txt","r")
    strings = fp.readlines()
    fp.close()
    for i in range(0,len(strings)):
        strings[i] = strings[i].strip()
    test_graph = DependencyGraphClass()
    rule_collector = []
    for each in strings:
        rule_tuple = IFTTTParser(each, {})
        if rule_tuple is not None:
            rule_collector.append(rule_tuple)

    conflict_collector = []
    for each in rule_collector:
        popped_out = test_graph.add(each, force=False)
        if popped_out:
            conflict_collector.append(popped_out)
    loops = test_graph.find_loop()
    for each in loops:
        conflict_collector.append([each])
    collisions = test_graph.graph_check_forward()
    conflict_collector.extend(collisions)

    for each in conflict_collector:
        print("-"*20)  # each is a conflict
        for entry in each:  # entry is a link
            for connection in entry: # connection is a tuple
                for condition in connection[0]:
                    print("({} {} {})".format(condition.subject, condition.operator, condition.value),end=' ')
                print("->", end=' ')
                for action in connection[1]:
                    print("({} {} {})".format(action.subject, action.operator, action.value),end=' ')
            print()

    print("Done")