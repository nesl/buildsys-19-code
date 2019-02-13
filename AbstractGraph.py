import abc

"""
The abstraction graph of the data structure.
"""
abstractions = dict()
#deviceAbstractionList = []
#abstractionName = []
#modalityAbstractionList = []
#serviceAbstractionList = []

class Abstraction:
	name = ''
	explicitDependency = []
	implicitDependency = []
    
	@abc.abstractmethod
	def __init__(self,info, name, explicitDependency):
		pass

class DeviceAbstraction(Abstraction):
    deviceInfo = None
    
    def __init__(self, deviceInfo, name, explicitDependency):
        self.deviceInfo = deviceInfo
        self.name = name
        self.explicitDependency = explicitDependency
        self.implicitDependency = []


class ModalityAbstraction(Abstraction):
    modalityInfo = None

    def __init__(self, modalityInfo, name, explicitDependency):
		self.modalityInfo = modalityInfo
		self.name = name
		self.explicitDependency = explicitDependency
		self.implicitDependency = []


class ServiceAbstraction(Abstraction):
    serviceInfo = None
    
    def __init__(self, serviceInfo, name, explicitDependency):
        self.serviceInfo = serviceInfo
        self.name = name
        self.explicitDependency = explicitDependency
        self.implicitDependency = []

'''
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
'''

def addAbstraction(type):
	if type.name in abstractions.keys():
		print('abstraction name is duplicated. Change one')
		return 1
	abstractions[type.name] = type
	updateImplicitDependency(type)
    #abstractionName.append(type.name)
	return 0
	'''
    if abstractionTypeDeterminer(type) is not None:
        abstractions[type.name] = type
    else:
        print('error from AddAbstraction')
        return -1
	'''


def updateAbstraction(name):

    if name in abstractions.keys():
        updateExplicitDependency(abstraction)
        updateImplicitDependency(abstraction)
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
	'''
    type = abstractionTypeDeterminer(abstraction)

    if type is not None:
        type.remove(abstraction)
        abstractionName.remove(abstraction.name)
    else:
        print('error from DeleteAbstraction')
        return -1
    '''
	del abstractions[abstraction.name]
	return 0
    
'''
Dependencies are only cleared when there is a service retrieval.
'''
def clearDependency(name):
	
    for abstraction in abstractions.keys():
        if abstraction.name == name:
            for dependency in abstraction.explicitDependency:
                if dependency not in abstractions.keys():
                    abstraction.explicitDependency.remove(dependency)
            for dependency in abstraction.implicitDependency:
                if dependency not in abstractions.keys():
                    abstraction.implicitDependency.remove(dependency)
            return abstraction
            
    print('The name is in the abstractions but not in any of the abstraction')
    print('\nError from getServices')
    return None

'''
This function will clear any null dependencies when returning a service.
'''
def getServices(name):
 
    if name not in abstractions.keys():
        print('Name is not found. \nSent from getServices')
        return None        
	return clearDependency(name)    
    
def updateImplicitDependency(abstraction):
    # TODO: update the implicit list of the abstraction
    return 0

def updateExplicitDependency(abstraction):
	# TODO: change what updating an explicit dependency means.
	return 0


##############################
# Starting testing functions #
##############################
def clear():
    abstractions.clear()

def testAddRegistration():
    clear()
    deviceAbstration1 = DeviceAbstraction('something', 'device1', [])
    addAbstraction(deviceAbstration1)
    if len(abstractions) != 1:
        print('fail add abstraction len1')
        return 1
    '''
    tmp = deviceAbstractionList[0]
    if tmp.name != 'device1':
        print('fail add abstraction name1')
        return 2
    deviceAbstration1 = DeviceAbstraction('something', 'device2', [])
    addAbstraction(deviceAbstration1)
    if len(abstractions.keys()) != 2:
        print('fail add abstraction len2')
        return 3
    tmp = abstractions.keys()[1]
    if tmp.name != 'device2':
        print('fail add abstraction name2')
        return 4

    modalityAbstraction = ModalityAbstraction('mod1', ['device1'])
    addAbstraction(modalityAbstraction)
    if len(modalityAbstractionList) != 1:
        print('fail add abstraction mod1 len')
        return 5
    tmp = modalityAbstractionList[0]
    if tmp.name != 'mod1' or tmp.explicitDependency[0] != 'device1':
        print('fail add abstraction mod1 name')
        return 6

    serviceAbstraction = ServiceAbstraction('ser', ['device1', 'device2'])
    addAbstraction(serviceAbstraction)
    if len(serviceAbstractionList) != 1:
        print('fail add abstraction ser len')
        return 7
    tmp = serviceAbstractionList[0]
    if tmp.name != 'ser' or tmp.explicitDependency[1] != 'device2':
        print('fail add abstraction ser name')
        return 8

    if abstractionName[0] != 'device1':
        print('fail add abstraction abstraction name 0')
        return 9
    if abstractionName[1] != 'device2':
        print('fail add abstraction abstraction name 1')
        return 10
    if abstractionName[2] != 'mod1':
        print('fail add abstraction abstraction name 2')
        return 11
    if abstractionName[3] != 'ser':
        print('fail add abstraction abstraction name 3')
        return 12
	'''
    print('pass add abstraction')
    return 0

if __name__ == '__main__':
    print(testAddRegistration())
