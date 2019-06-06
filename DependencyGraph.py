from IFTTTParsing import ConditionStruct, IFTTTParser
import numpy as np

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
                command_value = [0,1]
                if each_a.operator == '>=' and each_b.operator == '=':
                    # a is numerical and b is a command
                    # for conditions, they can be satisfied at the same time -> compatible
                    # for actions, they can be performed at the same time -> compatible
                    is_identical = False
                    if each_a.value > each_b.value and each_b.value not in command_value:
                        is_compatible = False
                        return is_compatible, is_identical
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
                    if each_a.value < each_b.value and each_b.value not in command_value:
                        is_compatible = False
                        return is_compatible, is_identical
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
                    if each_a.value < each_b.value and each_a.value not in command_value:
                        is_compatible = False
                        return is_compatible, is_identical
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
                    if each_a.value > each_b.value and each_a.value not in command_value:
                        is_compatible = False
                        return is_compatible, is_identical
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


class DependencyGraphClass:
    def __init__(self):
        self.nodes = []

    def add(self, new_link: tuple, force=False, remove=True):
        source_node = GraphNode(new_link[0])
        dest_node = GraphNode(new_link[1])

        compatible_condtions_list = []
        uncompatible_actions_list = []


        # Compare source node with existing nodes
        # if any of the existing nodes is compatible with source node, then there's a potential of conflict
        source_is_compatible = False
        source_is_identical = False
        for node in self.nodes:
            is_compatible, is_identical = is_compatible_or_identical(source_node, node)
            if is_compatible:
                source_is_compatible = True
                compatible_condtions_list.append(node)
            if is_identical:
                source_is_identical = True
                source_node = node
                compatible_condtions_list.append(node)

        # Compare dest node with existing nodes
        # if any of the existing nodes does not agree with destination node, then there's a potential of conflict
        dest_is_compatible = True
        dest_is_identical = False
        for node in self.nodes:
            is_compatible, is_identical = is_compatible_or_identical(dest_node, node, is_source_node=False)
            if not is_compatible:
                dest_is_compatible = False
                uncompatible_actions_list.append(node)
            if is_identical:
                dest_is_identical = True
                dest_node = node

        # If source_node is compatible, which means the new condition will happen along with existing conditions
        # and meanwhile, dest_node is not compatible, which suggest the new action may counteract with others
        # In this case, we list all the existing compatible condtions C and uncompatible actions A
        # Run a search, if there exist a route in graph from c in C to a in A, the new rule need to be revised

        if source_is_identical and dest_is_identical:
            route_already_exist, _ = self.find_shortest_path(source_node, dest_node)
            if route_already_exist:
                return None

        if force:  # forciably add a new link without checking conflicts. This is used to test other functions
            if not source_is_identical:
                self.nodes.append(source_node)
            if not dest_is_identical:
                self.nodes.append(dest_node)
            source_node.outward_link.append(dest_node)
            dest_node.inward_link.append(source_node)
            return None

        pop_out_from_graph = []
        # pop_out_from_graph is a list, each element of which is a list containing tuples of conflict_links
        # e.g result[i] = [(ConditionStruct1, Condition_Struct2), (ConditionStruct3, Condition_Struct4)] is one link


        new_rule_is_valid = True
        for compatible_condtion in compatible_condtions_list:
            for uncompatible_action in uncompatible_actions_list:
                found_route, shortest_path = self.find_shortest_path(compatible_condtion, uncompatible_action)
                if found_route:
                    new_rule_is_valid = False
                    pop_out_from_graph.append([])
                    for i in range(0, len(shortest_path)-1):
                        pop_out_from_graph[-1].append(self.remove(shortest_path[i], shortest_path[i + 1], remove=remove))
                    # pop all links in current conflict chain

        if not new_rule_is_valid:
            pop_out_from_graph.append([])
            pop_out_from_graph[-1].append(new_link)
            return pop_out_from_graph  # send the tuple for processing
        else:
            if remove:
                if not source_is_identical:
                    self.nodes.append(source_node)
                if not dest_is_identical:
                    self.nodes.append(dest_node)
                source_node.outward_link.append(dest_node)
                dest_node.inward_link.append(source_node)
            return None

    def remove(self, a: GraphNode, b: GraphNode, remove=True):
        # remove an edge a->b, a and b are known pointers of two nodes that are ALREADY in the graph
        if remove:
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
        while has_loop and len(self.nodes):
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
                            loop_link_list[-1].append(self.remove(stack[i+1], stack[loop_start_index]))
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

    def find_shortest_path(self, a: GraphNode, b: GraphNode):
        trace_back = list(np.zeros(len(self.nodes)))
        topology_depth = list(np.zeros(len(self.nodes)))
        shortest_path = []

        if a not in self.nodes:
            return False, []
        else:  # start a BFS
            trace_back[self.nodes.index(a)] = 0
            current_depth = 1
            visited, queue = [], [a]
            found_dest = False
            while len(queue):
                current_node = queue[0]
                if current_node not in visited:
                    visited.append(current_node)  # mark this vertex as visited
                for each in current_node.outward_link:

                    if each == b:
                        # We have found a trail leading to the destination in the graph
                        found_dest = True
                        queue.append(b)
                        trace_back[self.nodes.index(b)] = current_node
                        topology_depth[self.nodes.index(b)] = current_depth
                        break  # break from for each in current_node.outward_link

                    else:
                        if each not in visited:
                            queue.append(each)
                            trace_back[self.nodes.index(each)] = current_node
                            topology_depth[self.nodes.index(each)] = current_depth

                queue.pop(0)  # dequeue the current_node
                if found_dest:
                    break  # break from while
            if len(queue) == 0:
                found_dest = False

            # Next step: Trace back from b to a and same the links along the way in a list
            # In the future, if you want to pop out the conflicted rule from the list, then change here(add remove)
            if found_dest:
                dest_node = b
                source_node =  None
                shortest_path = [b]
                while source_node != a:
                    source_node = trace_back[self.nodes.index(dest_node)]
                    shortest_path.append(source_node)
                    dest_node = source_node
            shortest_path.reverse()
            return found_dest, shortest_path


    def DFS(self, a: GraphNode):
        visited, stack = [], [a]
        while len(stack):
            curr_node = stack[-1]
            if curr_node not in visited:
                visited.append(curr_node)
            has_unvisited_child = False
            for each in curr_node.outward_link:
                has_unvisited_child = False
                if each not in visited:
                    stack.append(each)
                    has_unvisited_child = True  # push one of the outward nodes in stack
                    break
            if not has_unvisited_child:
                stack.pop()
        return visited

    def reverse_BFS(self, a: GraphNode): # BFS based on inward link
        trace_back = list(np.zeros(len(self.nodes)))
        topology_depth = list(np.zeros(len(self.nodes)))
        current_depth = 1

        visited, queue = [], [a]
        while len(queue):
            current_node = queue[0]
            if current_node not in visited:
                visited.append(current_node)  # mark this vertex as visited
            for each in current_node.inward_link:
                if each not in visited:
                    queue.append(each)
                    trace_back[self.nodes.index(each)] = current_node
                    topology_depth[self.nodes.index(each)] = current_depth
            queue.pop(0)  # dequeue the current_node
            current_depth += 1
        return topology_depth


    def graph_check_forward(self):
        conflicts_found = []

        index = 0
        while index < len(self.nodes):
            curr_node = self.nodes[index]
            pop_out_from_graph = []
            compatible_conditions_list = []
            for node in self.nodes:
                is_compatible, is_identical = is_compatible_or_identical(curr_node, node, is_source_node=True)
                if is_compatible or is_identical:
                    compatible_conditions_list.append(node)
            # find all compatible condition nodes

            remove_happens = False
            for compat_node in compatible_conditions_list:
                curr_node_desendents = self.DFS(curr_node)
                curr_node_desendents.remove(curr_node)
                compat_node_desendents = self.DFS(compat_node)
                compat_node_desendents.remove(compat_node)

                is_compatible = True

                for i in range(0, len(curr_node_desendents)):
                    for j in range(0, len(compat_node_desendents)):
                        is_compatible, _ = is_compatible_or_identical(curr_node_desendents[i],
                                                                      compat_node_desendents[j], is_source_node=False)
                        if not is_compatible:
                            break
                    if not is_compatible:
                        break

                if not is_compatible:
                    pop_out_from_graph.append([])
                    remove_happens = True
                    _, path_to_remove_curr = self.find_shortest_path(curr_node, curr_node_desendents[i])
                    _, path_to_remove_compat = self.find_shortest_path(compat_node, compat_node_desendents[j])
                    for k in range(0, len(path_to_remove_curr)-1):
                        if path_to_remove_curr[k] in path_to_remove_compat and path_to_remove_curr[k+1] in path_to_remove_compat:
                            temp_tuple = (path_to_remove_curr[k].val, path_to_remove_curr[k+1].val)
                            pop_out_from_graph[-1].append(temp_tuple)
                        else:
                            pop_out_from_graph[-1].append(self.remove(path_to_remove_curr[k], path_to_remove_curr[k+1]))
                    pop_out_from_graph.append([])
                    for k in range(0, len(path_to_remove_compat)-1):
                        pop_out_from_graph[-1].append(self.remove(path_to_remove_compat[k], path_to_remove_compat[k+1]))
            if not remove_happens:
                index = index + 1
            else:
                conflicts_found.append(pop_out_from_graph)
        return conflicts_found


    def graph_check_backward(self):
        pass

    def print_contigency_table(self):
        contigency_table = []
        for node_a in self.nodes:
            contigency_table.append([])
            for node_b in self.nodes:
                if node_b in node_a.outward_link:
                    contigency_table[-1].append(1)
                else:
                    contigency_table[-1].append(0)
        for i in range (0, len(contigency_table)):
            for j in range(0, len(contigency_table)):
                print(contigency_table[i][j], end=' ')
            print()

if __name__ == '__main__':
    strings = ["if A.val = 1 then B.val = 1", "if B.val = 1 then C.val = 1", "if C.val = 1 then F.val = 1",
               "if A.val = 1 then D.val = 1", "if D.val = 1 then E.val = 1", "if E.val = 1 then F.val = 0",
               "if K.val = 1 then L.val = 0", "if L.val = 0 then K.val = 1", "if H.val = 0 then I.val = 0",
               "if H.val = 0 then I.val = 1"]
    valid_abstract = {"temperature": ["val"], "air_conditioner": ["state"],
                      "humidity": ["val"], "humidifier": ["state"],
                      "A": ["val"], "B": ["val"], "C": ["val"], "D": ["val"], "E": ["val"], "F": ["val"],
                      "G": ["val"], "H": ["val"], "I": ["val"], "J": ["val"], "K": ["val"], "L": ["val"]}
    test_graph = DependencyGraphClass()
    rule_collector = []
    for each in strings:
        rule_tuple = IFTTTParser(each, valid_abstract)
        if rule_tuple is not None:
            rule_collector.append(rule_tuple)
    for each in rule_collector:
        popped_out = test_graph.add(each, force=True)
    ans = test_graph.reverse_BFS(test_graph.nodes[3])
    result1 = test_graph.find_loop()
    result2 = test_graph.graph_check_forward()
    test_graph.print_contigency_table()
    print("Done")


# if __name__ == '__main__': # Used to test the compatibility function
#     a = GraphNode([ConditionStruct("humidity", '>=', "25"), ConditionStruct("humidity", '<=', "30")])
#     b = GraphNode([ConditionStruct("humidity", '>=', "35")])
#     print(is_compatible_or_identical(a,b))


    # This string for testing add()
    # strings = ["if temperature.val >= 70 then air_conditioner.state = 1 ",
    #            "if air_conditioner.state = 1 then humidifier.state = 1",
    #            "if humidity.val <= 70 and temperature.val <= 69 then air_conditioner.state = 0",
    #            "if temperature.val <= 69 then air_conditioner.state = 0 ",
    #            "if air_conditioner.state = 1 and temperature.val <= 69 then humidifier.state = 0 ",  # this conflicts to line 2
    #            "if humidifier.state = 1 and temperature.val >= 70 and air_conditioner.state = 1 then air_conditioner.state = 0"] # this conflicts to line 1

    # valid_abstract = {"temperature": ["val"], "air_conditioner": ["state"],
    #                   "humidity": ["val"], "humidifier": ["state"],
    #                   "A": ["val"], "B": ["val"], "C": ["val"], "D": ["val"], "E": ["val"], "F": ["val"],
    #                   "G": ["val"], "H": ["val"], "I": ["val"], "J": ["val"], "K": ["val"], "L": ["val"]}

    # test_graph = DependencyGraphClass()
    # rule_collector = []
    # for each in strings:
    #     rule_tuple = IFTTTParser(each, valid_abstract)
    #     if rule_tuple is not None:
    #         rule_collector.append(rule_tuple)
    # for each in rule_collector:
    #     popped_out = test_graph.add(each)

    # # test_graph.nodes[2].outward_link.append(test_graph.nodes[3])  # Force a link to form a loop
    # # test_graph.nodes[3].inward_link.append(test_graph.nodes[2])

    # result1 = test_graph.find_loop()
    # result2 = test_graph.graph_check_forward()
    # test_graph.print_contigency_table()
    # print("Done")

    # test add()
    # strings = ["if A.val = 1 then C.val = 1", "if C.val = 1 then D.val = 1", "if D.val = 1 then B.val = 1",
    #            "if A.val = 1 then B.val = 0"]
