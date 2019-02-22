import abc
from Abstraction import *
from typing import List

"""
    The abstraction graph of the data structure.
"""
class AbstractGraph:
    
    abstractions: List[Abstraction] = dict()

    '''
    Adds a new abstraction to the graph. This assumes that the control system developer
    will provide lists of the names of both the children and the parents of an abstraction.
    We can imagine an interface where the control system developer can select which
    abstractions are parents/children and pass the names (IDs)  to this function accordingly.
    '''
    def addAbstraction(self, abstraction, children : List[str] = None, parents: List[str] = None):
        if abstraction.name in self.abstractions.keys():
            print('abstraction name is duplicated. Change one')
            return 1
        self.abstractions[abstraction.name] = abstraction
        self.updateAbstractionFamily(abstraction,children, parents)
        return 0

    '''
        Updates the children and parents for a new abstraction.
    '''
    def updateAbstractionFamily(self,abstraction,children: List[str], parents: List[str]):

        if abstraction.name not in self.abstractions.keys():
            print("Error updating abstraction family; abstraction does not exist: ",abstraction.name)
            return 1
        
        if children is not None:
            # Add the children
            for child in children:
                if child not in self.abstractions.keys():
                    print("Error updating abstraction family; child abstraction does not exist: ", child)
                    return 1
                if self.abstractions[abstraction.name].childAbstractions is None:
                    self.abstractions[abstraction.name].childAbstractions = set()
                self.abstractions[abstraction.name].childAbstractions.add(self.abstractions[child])
                if self.abstractions[child].parentAbstractions is None:
                    self.abstractions[child].parentAbstractions = set()
                self.abstractions[child].parentAbstractions.add(self.abstractions[abstraction.name])

        if parents is not None:
            # Add the parents
            for parent in parents:
                if parent not in self.abstractions.keys():
                    print("Error updating abstraction family; parent abstraction does not exist: ", parent)
                    return 1
                if self.abstractions[abstraction.name].parentAbstractions is None:
                    self.abstractions[abstraction.name].parentAbstractions = set()
                self.abstractions[abstraction.name].parentAbstractions.add(self.abstractions[parent])
                if self.abstractions[parent].childAbstractions is None:
                    self.abstractions[parent].childAbstractions = set()
                self.abstractions[parent].childAbstractions.add(self.abstractions[abstraction.name])


        return 0

    """
    Note: After the abstraction is deleted. It does not delete its dependency.
    The dependencies rely on this should be updated at the runtime when accessing
    them.
    """
    def deleteAbstraction(self,abstraction):
        del self.abstractions[abstraction.name]
        return 0
    
#    '''
#    Dependencies are only cleared when there is a service retrieval.
#    '''
#    def clearDependency(name):
#
#        for abstraction in self.abstractions.keys():
#            if abstraction.name == name:
#                for dependency in abstraction.explicitDependency:
#                    if dependency not in self.abstractions.keys():
#                        abstraction.explicitDependency.remove(dependency)
#                for dependency in abstraction.implicitDependency:
#                    if dependency not in self.abstractions.keys():
#                        abstraction.implicitDependency.remove(dependency)
#                return abstraction
#
#        print('The name is in the abstractions but not in any of the abstraction')
#        print('\nError from getServices')
#        return None

#    '''
#    This function will clear any null dependencies when returning a service.
#    '''
#    def getServices(self,name):
#
#        if name not in self.abstractions.keys():
#            print('Name is not found. \nSent from getServices')
#            return None
#        return self.clearDependency(name)

#    def updateImplicitDependency(abstraction):
#        # TODO: update the implicit list of the abstraction
#        return 0
#
#    def updateExplicitDependency(abstraction):
#        # TODO: change what updating an explicit dependency means.
#        return 0


    ##############################
    # Starting testing functions #
    ##############################
    def clear(self):
        self.abstractions.clear()



#    def testAddRegistration():
#        clear()
#        deviceAbstration1 = DeviceAbstraction('something', 'device1', [])
#        addAbstraction(deviceAbstration1)
#        if len(abstractions) != 1:
#            print('fail add abstraction len1')
#            return 1
#        '''
#        tmp = deviceAbstractionList[0]
#        if tmp.name != 'device1':
#            print('fail add abstraction name1')
#            return 2
#        deviceAbstration1 = DeviceAbstraction('something', 'device2', [])
#        addAbstraction(deviceAbstration1)
#        if len(abstractions.keys()) != 2:
#            print('fail add abstraction len2')
#            return 3
#        tmp = abstractions.keys()[1]
#        if tmp.name != 'device2':
#            print('fail add abstraction name2')
#            return 4
#
#        modalityAbstraction = ModalityAbstraction('mod1', ['device1'])
#        addAbstraction(modalityAbstraction)
#        if len(modalityAbstractionList) != 1:
#            print('fail add abstraction mod1 len')
#            return 5
#        tmp = modalityAbstractionList[0]
#        if tmp.name != 'mod1' or tmp.explicitDependency[0] != 'device1':
#            print('fail add abstraction mod1 name')
#            return 6
#
#        serviceAbstraction = ServiceAbstraction('ser', ['device1', 'device2'])
#        addAbstraction(serviceAbstraction)
#        if len(serviceAbstractionList) != 1:
#            print('fail add abstraction ser len')
#            return 7
#        tmp = serviceAbstractionList[0]
#        if tmp.name != 'ser' or tmp.explicitDependency[1] != 'device2':
#            print('fail add abstraction ser name')
#            return 8
#
#        if abstractionName[0] != 'device1':
#            print('fail add abstraction abstraction name 0')
#            return 9
#        if abstractionName[1] != 'device2':
#            print('fail add abstraction abstraction name 1')
#            return 10
#        if abstractionName[2] != 'mod1':
#            print('fail add abstraction abstraction name 2')
#            return 11
#        if abstractionName[3] != 'ser':
#            print('fail add abstraction abstraction name 3')
#            return 12
#        '''
#        print('pass add abstraction')
#        return 0
#


def testAddChildrenAndParents():
    graph = AbstractGraph()
    device1 = DeviceAbstraction(AbstractionSpecification(10.0, 100, 100,), "Device1")
    graph.addAbstraction(device1)
    device2 = DeviceAbstraction(AbstractionSpecification(11.0, 100, 100,), "Device2")
    graph.addAbstraction(device2, ["Device1"])
    device3 = DeviceAbstraction(AbstractionSpecification(12.0, 100, 100,), "Device3")
    graph.addAbstraction(device3, None, ["Device2"])
    print("Device1: \n***********\n", device1)
    print("\nDevice2: \n***********\n", device2)
    print("\nDevice3: \n***********\n", device3)


if __name__ == "__main__":
    # print("What the fuck I am doing here!")
    # testRegister()
    testAddChildren()
'''
    TODOs:
        > Test deletion of abstraction to ensure that any children/parent sets don't retain deleted abstraction
    
'''
