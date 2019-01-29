import json
from pprint import pprint

class DeviceInfo:
    ip = ""
    classSpect = ""
    descrpt = ""
    location = ""
    mac = ""
    id = -1

    def __init__(self, ip, classSpect, descrpt, location, mac):
        self.ip = ip
        self.classSpect = classSpect
        self.descrpt = descrpt
        self.location = location
        self.mac = mac

    def assignID(self, id):
        self.id = id


# add the device information to JSON specs
def addDevice(cur, addInfo):
    temp = [{"ip": addInfo.ip, "classSpect": addInfo.classSpect, "descrpt":
    addInfo.descrpt, "location": addInfo.location, "mac": addInfo.mac,
    "id": addInfo.id}]
    cur.append(temp)
    return cur

# Register the device. The device must be associated with the specific device
def register(path, deviceInfo):
    with open(path, 'r') as fh:
        data = json.load(fh)
        if data['class'] is None:
            data['uid'] = 1
            deviceInfo.assignID(1)

            return 1
