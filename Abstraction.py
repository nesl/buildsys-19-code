import abc
from typing import List,Set

'''
    This time abstraction represents the a start and stop time for
    a device's operation. A device can have multiple instances of time
    operation.
    '''
class OperationTimeInterval:
    start_time = None
    end_time = None
    def __init__(self, st, et):
        self.start_time = st
        self.end_time = et

'''
    This class will represent the location of a device. For now, we will
    work in 2 dimensions.
'''
class Location:
    locationX = None
    locationY = None
    def __init__(self, locationX, locationY):
        self.locationX = locationX
        self.locationY = locationY

'''
    The sampling rate is currently a simple int that will represent a resolution for a specific
    abstraction. This API can later be augmented to have abstraction-specific sampling rates
    '''
class AbstractionSamplingRate:
    value: int = None
    
    def __init__(self, value):
        self.value = value

'''
    The resolution is currently a simple int that will represent a resolution for a specific
    abstraction. This API can later be augmented to have abstraction-specific resolutions
'''
class AbstractionResolution:
    value: int = None

    def __init__(self, value):
        self.value = value

'''
    This class will represent the specifications of a device
        > The effective radius represents the "range of a device w.r.t. its location
        > The resolution is currently a simple float that will represent a resolution for a specific
          abstraction. This API can later be augmented to have abstraction-specific
        > Same goes for the sampling rate of a modality
'''
class AbstractionSpecification:
    effectiveRadius: float = None
    resolution: AbstractionResolution = None
    samplingRate: AbstractionSamplingRate = None
    
    def __init__(self,effectiveRadius, resolution = None, samplingRate = None):
        self.effectiveRadius = effectiveRadius
        self.resolution = resolution
        self.samplingRate = samplingRate

'''
    Abstraction classes:
'''
class Abstraction:
    name = ''
    childAbstractions = None
    parentAbstractions = None
    specs : AbstractionSpecification = None
    location : Location = None
    toop: OperationTimeInterval = None
    
    @abc.abstractmethod
    def __init__(self, specs, name, childAbstractions = None, parentAbstractions = None):
        self.name = name
        self.specs = specs
        self.childAbstractions : Set[Abstraction] = childAbstractions
        self.parentAbstractions: Set[Abstraction] = parentAbstractions

    def appendChildAbstraction(self,childAbstraction):
        self.childAbstractions.append(childAbstraction)

    def appendParentAbstraction(self,parentAbstraction):
        self.parentAbstractions.append(parentAbstraction)

    def setLocation(self, location: Location):
        self.location = location

    def setTimeOfOperation(self, toop: OperationTimeInterval):
        self.toop = toop

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.name == other.name)

    def __str__(self):
        abstractionStr = "Abstraction Name: "+self.name
        if self.childAbstractions is not None:
            abstractionStr = abstractionStr + "\n"+"Children:\n"
            for child in self.childAbstractions:
                abstractionStr = abstractionStr + "\t -"+child.name+"\n"
        if self.parentAbstractions is not None:
            abstractionStr = "Parents:\n"
            for parent in self.parentAbstractions:
                abstractionStr= abstractionStr + "\t -"+parent.name+"\n"
        return abstractionStr

class DeviceAbstraction(Abstraction):
    
    def __init__(self, specs, name, childAbstractions = None, parentAbstractions = None):
        self.name = name
        self.specs = specs
        self.childAbstractions : Set[Abstraction] = childAbstractions
        self.parentAbstractions: Set[Abstraction] = parentAbstractions


class ModalityAbstraction(Abstraction):
    
    def __init__(self, specs, name, childAbstractions = None, parentAbstractions = None):
        self.name = name
        self.specs = specs
        self.childAbstractions : Set[Abstraction] = childAbstractions
        self.parentAbstractions: Set[Abstraction] = parentAbstractions


class ServiceAbstraction(Abstraction):
    
    def __init__(self, specs, name, childAbstractions = None, parentAbstractions = None):
        self.name = name
        self.specs = specs
        self.childAbstractions : Set[Abstraction] = childAbstractions
        self.parentAbstractions: Set[Abstraction] = parentAbstractions

