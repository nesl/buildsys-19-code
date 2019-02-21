
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
    
    def __init__(self,effectiveRadius, resolution, samplingRate):
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
    def __init__(self, specs, name, childAbstractions, parentAbstractions):
        self.name = name
        self.specs = specs
        self.childAbstractions : List[Abstraction] = childAbstractions
        self.parentAbstractions: List[Abstraction] = parentAbstractions

    def appendChildAbstraction(self,childAbstraction : Abstraction):
        self.childAbstractions.append(childAbstraction)

    def appendParentAbstraction(self,parentAbstraction : Abstraction):
        self.parentAbstractions.append(parentAbstraction)

    def setLocation(self, location: Location):
        self.location = location

    def setTimeOfOperation(self, toop: OperationTimeInterval):
        self.toop = toop

class DeviceAbstraction(Abstraction):
    
    def __init__(self, specs, name, childAbstractions, parentAbstractions):
        self.name = name
        self.specs = specs
        self.childAbstractions : List[Abstraction] = childAbstractions
        self.parentAbstractions: List[Abstraction] = parentAbstractions


class ModalityAbstraction(Abstraction):
    
    def __init__(self, specs, name, childAbstractions, parentAbstractions):
        self.name = name
        self.specs = specs
        self.childAbstractions : List[Abstraction] = childAbstractions
        self.parentAbstractions: List[Abstraction] = parentAbstractions


class ServiceAbstraction(Abstraction):
    
    def __init__(self, specs, name, childAbstractions, parentAbstractions):
        self.name = name
        self.specs = specs
        self.childAbstractions : List[Abstraction] = childAbstractions
        self.parentAbstractions: List[Abstraction] = parentAbstractions
