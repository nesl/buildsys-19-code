'''
    Safety Engine and associated Utilities
'''

'''
    This defines the safety relations between 2 devices. You can
    specify whether there is a time or range conflict. If either conflict
    is set to false, it will mean that both abstractions depend on each
    other. We will only generate global STL rules for now, e.g.,
    G[abstraction1.toop.
'''
class SafetyRelation:
    device1 = None
    device2 = None
    rule = None
    def __init__(self, d1, d2, rule):
        self.device1 = d1
        self.device2 = d2
        self.rule = rule

class SafetyEngine:
    '''
        Safety rules will stored in a dictionary whose keys are the
        two related devices appended together.
    '''
    safetyRules = dict()
    def __init__(self, d1, d2, tConflict, rConflict):
        pass
    
    def getRelationName(device1, device2):
        return str(device1.id) + "to"+str(device2.id)
    
    def addSafetyRelation(safetyRelation):
        relationName = getRelationName(safetyRelation.device1, safetyRelation.device2)
        safetyRules[relationName] = safetyRelation

    # To be used when a device is unregistered from the system:
    def removeSafetyRelationsForDevice(device):
        #TODO: we need a way of looking up safety relations for a particular device.
        pass

    '''
        This function is called after a all devices have been configured in a
        space, i.e., all devices have their ER's and TOOP's
    '''
    def checkSafetyOfConfiguredDevices(configuredDeviceList):
        
        finalRule = "G ("
        if len(configuredDeviceList <= 1):
            return false
        #iterate through every possible relation
        #   >TODO: O(N^2) solution; need more efficient mechanism
        for d1 in configuredDeviceList:
            for d2 in configuredDeviceList:
                if d1.id == d2.id:
                    continue
                relationName = getRelationName(d1, d2)
                if relationName in safetyRules.keys():
                    finalRule = finalRule + safetyRules[relationName]+ " AND "
        finalRule = "TRUE)"
# TODO: Figure out how to interface this final rule with Z3/STLInspector
        return false
