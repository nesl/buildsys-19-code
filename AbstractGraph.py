"""
The abstraction graph of the data structure.
"""

deviceAbstractionList = []
abstractionName = []
modalityAbstractionList = []
serviceAbstractionList = []

class DeviceAbstraction:
    DeviceInfo = None
    name = ''
    explicitDependency = []
    implicitDependency = []


class ModalityAbstraction:
    name = ''
    explicitDependency = []
    implicitDependency = []


class ServiceAbstraction:
    name = ''
    explicitDependency = []
    implicitDependency = []


def abstractionTypeDeterminer(type):
    if isinstance(type, DeviceAbstraction):
        return deviceAbstractionList
    elif isinstance(type, ModalityAbstraction):
        return modalityAbstractionList
    elif isinstance(type, ServiceAbstraction):
        return serviceAbstractionList
    else:
        print('Error! Unknown type.')
        return None

def addAbstraction(type):
    if type.name in abstractionName:
        print('abstraction name is duplicated. Change one')
        return 1

    if abstractionTypeDeterminer(type) is not None:
        abstractionTypeDeterminer(type).append(type)
    else:
        print('error from AddAbstraction')
        return -1

    updateImplicitDependency(type)
    abstractionName.append(type.name)
    return 0

def updateAbstraction(abstraction):
    typeList = abstractionTypeDeterminer(abstraction)

    if type is not None:
        updateExplicitDependency(abstraction, typeList)
        updateImplicitDependency(abstraction, typeList)
    else:
        print('error from UpdateAbstraction')
        return -1
    return 0

"""
Note: After the abstraction is deleted. It does not delete its dependency.
The dependencies rely on this should be updated at the runtime when accessing
them.
"""
def deleteAbstraction(abstraction):
    type = abstractionTypeDeterminer(abstraction)

    if type is not None:
        type.remove(abstraction)
        abstractionName.remove(abstraction.name)
    else:
        print('error from DeleteAbstraction')
        return -1
    return 0

def clearDependency(name, abstractionList):
    for abstraction in abstractionList:
        if abstraction.name == name:
            for dependency in abstraction.explicitDependency:
                if dependency is not in abstractionName:
                    abstraction.explicitDependency.remove(dependency)
            for dependency in abstraction.implicitDependency:
                if dependency is not in abstractionName:
                    abstraction.implicitDependency.remove(dependency)
            return abstraction
    return None

def getServices(name):
    if name is not in abstractionName:
        print('Name is not found. \nSent from getServices')
        return None

    deviceAbstraction = clearDependency(name, deviceAbstractionList)
    if deviceAbstraction is not None:
        return deviceAbstraction

    modalityAbstraction = clearDependency(name, modalityAbstractionList)
    if modalityAbstraction is not None:
        return modalityAbstraction

    serviceAbstraction = clearDependency(name, serviceAbstractionList)
    if serviceAbstraction is not None:
        return serviceAbstraction

    print('The name is in the abstractionName but not in any of the abstraction')
    print('\nError from getServices')
    return None

def updateImplicitDependency(abstraction):
    # TODO: update the implicit list of the abstraction
    return 0

def updateExplicitDependency(abstraction, typeList):
    for type in typeList:
        if type.name == abstraction.name:
            typeList.remove(type)
            typeList.append(abstraction)
            return 0

    print('Error from updateExplicitDependency\n' + abstraction.name + 'not found!')
    return -1




if '__name__' == '__main__':
    pass
