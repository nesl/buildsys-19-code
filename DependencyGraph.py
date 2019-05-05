from IFTTTParsing import ConditionStruct, IFTTTParser


class GraphNode:
    def __init__(self, x: list): # x should be a list contains "ConditionStruct"
        self.val = x
        self.outward_link = []
        self.inward_link = []


def is_compatible_or_identical(a: GraphNode, b: GraphNode, is_source_node=True):
    # determine if two nodes a and b are compatible or not, identical or not
    # for a source_node, "compatible" means conditions of a and b can satisfy at the same time
    # for a dest_node, "compatible" means actions of a and b can perform at the same time
    is_compatible = True
    is_identical = True
    if is_source_node:
        # we do not compare source node with nodes without outward links for compatibility
        # directly, do not compare 'if' with 'then'
        if len(b.outward_link) == 0:
            is_compatible = False
    for each_a in a.val:
        for each_b in b.val:
            if each_a.subject == each_b.subject:
                if each_a.operator == '>=' and each_b.operator == '=':
                    # a is numerical and b is a command
                    # for conditions, they can be satisfied at the same time -> compatible
                    # for actions, they can be performed at the same time -> compatible
                    is_identical = False
                if each_a.operator == '=' and each_b.operator == '=':
                    # a,b are both commands
                    # if a.val != b.val, then they are certainly non-compatible
                    if each_a.value != each_b.value:
                        is_compatible = False
                        is_identical = False
                        return is_compatible, is_identical
                if each_a.operator == '<=' and each_b.operator == '=':
                    # a is numerical and b is a command
                    # for conditions, they can be satisfied at the same time -> compatible
                    # for actions, they can be performed at the same time -> compatible
                    is_identical = False
                if each_a.operator == '>=' and each_b.operator == '>=':
                    # a,b are both numerical
                    # as conditions, they can be satisfied together -> compatible
                    # as actions, they are not different values thresholds of a same subject ->non-compatible
                    # actually very few actions are numerical
                    if each_a.value != each_b.value:
                        is_identical = False
                        if not is_source_node:
                            is_compatible = False
                            return is_compatible, is_identical
                if each_a.operator == '=' and each_b.operator == '>=':
                    # a is a command and b is numerical
                    # for conditions, they can be satisfied at the same time -> compatible
                    # for actions, they can be performed at the same time -> compatible
                    is_identical = False
                if each_a.operator == '<=' and each_b.operator == '>=':
                    # a,b are both numerical
                    # if a.val > b.val, they can be satisfied together -> compatible, otherwise non-compatible
                    is_identical = False
                    if each_a.value <= each_b.value:
                        is_compatible = False
                if each_a.operator == '>=' and each_b.operator == '<=':
                    # a,b are both numerical
                    # if a.val < b.val, they can be satisfied together -> compatible, otherwise non-compatible
                    is_identical = False
                    if each_a.value >= each_b.value:
                        is_compatible = False
                if each_a.operator == '=' and each_b.operator == '<=':
                    # a is a command and b is numerical
                    # for conditions, they can be satisfied at the same time -> compatible
                    # for actions, they can be performed at the same time -> compatible
                    is_identical = False
                if each_a.operator == '<=' and each_b.operator == '<=':
                    # a,b are both numerical
                    # as conditions, they can be satisfied together -> compatible
                    # as actions, they are not different values thresholds of a same subject ->non-compatible
                    # actually very few actions are numerical
                    if each_a.value != each_b.value:
                        is_identical = False
                        if not is_source_node:
                            is_compatible = False
                            return is_compatible, is_identical
            else:
                # a and b are not working on the same subject
                # as conditions, a and b can be satisfied together
                # as actions, a and b can be done together
                is_identical = False
    if not is_source_node:
        # similarly, we do not compare 'then' with pure 'if'
        if len(b.inward_link) == 0:
            is_compatible = True
    return is_compatible, is_identical


class DependencyGraph:
    def __init__(self):
        self.nodes = []

    def add(self, new_link: tuple):
        source_node = GraphNode(new_link[0])
        dest_node = GraphNode(new_link[1])

        # Compare source node with existing nodes
        # if any of the existing nodes is compatible with source node, then there's a potential of conflict
        source_is_compatible = False
        source_is_identical = False
        for node in self.nodes:
            is_compatible, is_identical = is_compatible_or_identical(source_node, node)
            if is_compatible:
                source_is_compatible = True
            if is_identical:
                source_is_identical = True
                source_node = node

        # Compare dest node with existing nodes
        # if any of the existing nodes does not agree with destination node, then there's a potential of conflict
        dest_is_compatible = True
        dest_is_identical = False
        for node in self.nodes:
            is_compatible, is_identical = is_compatible_or_identical(dest_node, node, is_source_node=False)
            if not is_compatible:
                dest_is_compatible = False
            if is_identical:
                dest_is_identical = True
                dest_node = node

        # If source_node is compatible, which means the new condition will happen along with existing conditions
        # and meanwhile, dest_node is not compatible, which suggest the new action may counteract with others
        # In this case, this IFTTT rule need to be revised
        if source_is_compatible and not dest_is_compatible:
            return new_link  # send the tuple for processing
        else:
            if not source_is_identical:
                self.nodes.append(source_node)
            if not dest_is_identical:
                self.nodes.append(dest_node)
            source_node.outward_link.append(dest_node)
            dest_node.inward_link.append(source_node)
            return None

    def remove(self, a: GraphNode, b: GraphNode):
        # remove an edge a->b, a and b are known pointers of two nodes that are ALREADY in the graph
        a.outward_link.remove(b)
        b.inward_link.remove(a)
        if len(a.outward_link) == 0 and len(a.inward_link) == 0:
            self.nodes.remove(a)
        if len(b.outward_link) == 0 and len(b.inward_link) == 0:
            self.nodes.remove(b)
        removed_link = (a.val, b.val)
        return removed_link

    def find_loop(self):
        # find all circles in the current directional graph and remove the looped links
        # return a list, each element of which is a list containing tuples of loop_links
        # e.g result[i] = [(ConditionStruct1, Condition_Struct2), (ConditionStruct3, Condition_Struct4)]
        loop_link_list = []
        searched_for_loop = []  # Save the nodes that has already been search for loops
        has_loop = True
        while has_loop:
            for start_node in self.nodes:  # Traverse all nodes in the graph, search for loops containing this node
                restart = False  # if restart == True, then a loop is found and removed, we break all loops and restart

                # start a DFS
                visited, stack = [],[start_node]
                while len(stack):
                    current_node = stack[-1]
                    if current_node not in visited:
                        visited.append(current_node)  # mark this vertex as visited
                    has_unvisited_child = False
                    for each in current_node.outward_link:
                        if each in stack:
                            # the current vertex u has a link towards some vertex v in the stack
                            # a loop is found as v->...->u->v
                            has_loop = True
                            loop_start_index = stack.index(each)  # find v's location
                            loop_link_list.append([])
                            for i in range(loop_start_index , len(stack)-1):
                                loop_link_list[-1].append(self.remove(stack[i],stack[i+1]))
                                # pop all links in the loop
                            restart = True
                            break  # break from for each in current_node.outward_link
                        else:
                            has_loop = False
                            if each not in visited:
                                stack.append(each)
                                has_unvisited_child = True  # push one of the outward nodes in stack
                                break
                    if not has_unvisited_child:  # all outwards nodes has been visited
                        stack.pop()  # pop current node from the stack
                    # otherwise continue the while loop
                    if restart:
                        break  # break from while len(stack)
                if restart:
                    break  # break from for start_node in self.nodes
        return loop_link_list


if __name__ == '__main__':
    strings = [ # "if temperature.val >= 70 then air_conditioner.state = 1 ",
               "if temperature.val <= 69 then air_conditioner.state = 0 ",
               "if air_conditioner.state = 0 then humidifier.state = 1 ",
               "if humidifier.state = 1 and temperature.val >= 70 and air_conditioner.state = 1 then air_conditioner.state = 0"]

    valid_abstract = {"temperature": ["val"], "air_conditioner": ["state"],
                      "humidity": ["val"], "humidifier": ["state"]}
    test_graph = DependencyGraph()
    rule_collector = []
    for each in strings:
        rule_tuple = IFTTTParser(each, valid_abstract)
        if rule_tuple is not None:
            rule_collector.append(rule_tuple)
    for each in rule_collector:
        popped_out = test_graph.add(each)
    test_graph.nodes[2].outward_link.append(test_graph.nodes[3])  # Force a link to form a loop
    test_graph.nodes[3].inward_link.append(test_graph.nodes[2])
    result = test_graph.find_loop()
    print("Done")


# if __name__ == '__main__': # Used to test the compatibility function
#     a = GraphNode([ConditionStruct("humidity", '>=', "25"), ConditionStruct("humidity", '<=', "30")])
#     b = GraphNode([ConditionStruct("humidity", '>=', "35")])
#     print(is_compatible_or_identical(a,b))