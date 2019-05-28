'''
    The evaluation of remediot!
'''

from UserInterface import *
from AbstractGraph import *
from Abstraction import *


class EvalActuationGraph:
    graph = None
    def __init__(self):
        class WindowInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'windows', deviceInfo)

        class AirConditionerInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'ac', deviceInfo)

        class FanInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'fan', deviceInfo)

        class HeaterInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'heater', deviceInfo)

        class FirePlaceInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'fireplace', deviceInfo)

        class DoorControlInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'door', deviceInfo)

        class LightBulbsInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'light_bulbs', deviceInfo)

        class CurtainControlInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'curtain', deviceInfo)

        class CameraInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'camera', deviceInfo)

        class MotionSensorInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'motion_sensor', deviceInfo)

        class AllElectricDevicesInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'electric_devices', deviceInfo)

        class SmartphoneInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'smartphone', deviceInfo)

        class SpeakerInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'speaker', deviceInfo)


        class WarningUsingSpeaker(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'play warning sound',  moduleName, 0, ACTUATION)
                speakerInstance = SpeakerInstance()
                super(WarningUsingSpeaker, self).appendChildDeviceInstance(speakerInstance)

            def performFunc(self, *argc):
                print('playing warning sound')

        class WarningUsingLightBulbs(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'flash warning lights',  moduleName, 0, ACTUATION)
                lightBulbsInstance = LightBulbsInstance()
                super(WarningUsingLightBulbs, self).appendChildDeviceInstance(lightBulbsInstance)

            def performFunc(self, *argc):
                print('flash warning lights')

        class TextUsingSmartphone(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'text message to the user',  moduleName, 0, ACTUATION)
                smartphoneInstance = SmartphoneInstance()
                super(TextUsingSmartphone, self).appendChildDeviceInstance(smartphoneInstance)

            def performFunc(self, *argc):
                print('text the user something')

        class AllElectricDevicesOff(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'turn off all electric devices', moduleName, 0, ACTUATION)
                allElectricDevicesInstance = AllElectricDevicesInstance()
                super(AllElectricDevicesOff, self).appendChildDeviceInstance(allElectricDevicesInstance)

            def performFunc(self, *argc):
                print('turning off all of the electric devices')

        class LowPowerModeDevices(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'set low-power model for all electric devices', moduleName, 0, ACTUATION)
                allElectricDevicesInstance = AllElectricDevicesInstance()
                super(LowPowerModeDevices, self).appendChildDeviceInstance(allElectricDevicesInstance)

            def performFunc(self, *argc):
                print('setting low-power mode for all of the electric devices')

        class MotionSensorDetection(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'detect motion by motion sensor', moduleName, 0, ACTUATION)
                motionSensorInstance = MotionSensorInstance()
                super(MotionSensorDetection, self).appendChildDeviceInstance(motionSensorInstance)

            def performFunc(self, *argc):
                print('detecting the motion through motion sensor')

        class CameraMotionDetection(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'detect motion by camera', moduleName, 0, SENSING)
                cameraInstance = CameraInstance()
                super(CameraMotionDetection, self).appendChildDeviceInstance(cameraInstance)

            def performFunc(self, *argc):
                print('detecting the motion through camera')

        class CurtainOpen(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'open the curtain', moduleName, 0, ACTUATION)
                curtainControlInstance = CurtainControlInstance()
                super(CurtainOpen, self).appendChildDeviceInstance(curtainControlInstance)

            def performFunc(self, *argc):
                print('opening the curtain now')

        class LightBulbTurningOn(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'turn on light bulb', moduleName, 0, ACTUATION)
                lightBulbsInstance = LightBulbsInstance()
                super(LightBulbTurningOn, self).appendChildDeviceInstance(lightBulbsInstance)

            def performFunc(self, *argc):
                print('turning on the light bulbs now')

        class DoorOpening(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'open the door', moduleName, 0, ACTUATION)
                doorControlInstance = DoorControlInstance()
                super(DoorOpening, self).appendChildDeviceInstance(doorControlInstance)

            def performFunc(self, *argc):
                print('opening the doors now')

        class FirePlaceLightUp(Abstraction):
            def __init__(self):
                Abstraction.__init__(self, 'light up fireplace', 'heating up', 0, ACTUATION)
                firePlaceInstance = FirePlaceInstance()
                super(FirePlaceLightUp, self).appendChildDeviceInstance(firePlaceInstance)

            def performFunc(self, *argc):
                print('lighting up the fireplace now')

        class HeaterTurnOn(Abstraction):
            def __init__(self):
                Abstraction.__init__(self, 'turn on heater', 'heating up', 0, ACTUATION)
                heaterInstance = HeaterInstance()
                super(HeaterTurnOn, self).appendChildDeviceInstance(heaterInstance)

            def performFunc(self, *argc):
                print('Turning on heater now')

        class AirConditionerTurnOn(Abstraction):
            def __init__(self):
                Abstraction.__init__(self, 'turn on air conditioner', 'cooling down', 0, ACTUATION)
                acInstance = AirConditionerInstance()
                super(AirConditionerTurnOn, self).appendChildDeviceInstance(acInstance)

            def performFunc(self, *args):
                print('Turning on the HVAC now')

        class WindowOpening(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'open the window', moduleName, 0, ACTUATION)
                windowInstance = WindowInstance()
                super(WindowOpening, self).appendChildDeviceInstance(windowInstance)

            def performFunc(self, *args):
                print('Opening the window now.')

        class FanTurnOn(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'turn on fan', moduleName, 0, ACTUATION)
                fanInstance = FanInstance()
                super(FanTurnOn, self).appendChildDeviceInstance(fanInstance)

            def performFunc(self, *args):
                print('Turning on the fan now')


        class CoolDownModule(Module):
            def __init__(self):
                Module.__init__(self, 'cooling down')
                acTurnOn = AirConditionerTurnOn()
                fanTurOn = FanTurnOn('cooling down')
                windowOpening = WindowOpening('cooling down')
                super(CoolDownModule, self).addAbstraction(acTurnOn)
                super(CoolDownModule, self).addAbstraction(fanTurOn)
                super(CoolDownModule, self).addAbstraction(windowOpening)

        class HeatingUpModule(Module):
            def __init__(self):
                Module.__init__(self, 'heating up')
                heaterTurnOn = HeaterTurnOn()
                fireplaceLightUp = FirePlaceLightUp()
                windowOpening = WindowOpening('heating up')
                super(HeatingUpModule, self).addAbstraction(heaterTurnOn)
                super(HeatingUpModule, self).addAbstraction(fireplaceLightUp)
                super(HeatingUpModule, self).addAbstraction(windowOpening)

        class VentilizationModule(Module):
            def __init__(self):
                Module.__init__(self, 'ventilization')
                fanTurOn = FanTurnOn('ventilization')
                doorOpening = DoorOpening('ventilization')
                windowOpening = WindowOpening('ventilization')
                super(VentilizationModule, self).addAbstraction(fanTurOn)
                super(VentilizationModule, self).addAbstraction(doorOpening)
                super(VentilizationModule, self).addAbstraction(windowOpening)

        class IlluminationModule(Module):
            def __init__(self):
                Module.__init__(self, 'illumination')
                lightbulbTurningOn = LightBulbTurningOn('illumination')
                curtainOpen = CurtainOpen('illumination')
                super(IlluminationModule, self).addAbstraction(lightbulbTurningOn)
                super(IlluminationModule, self).addAbstraction(curtainOpen)

        class MotionDetectionModule(Module):
            def __init__(self):
                Module.__init__(self, 'motion detection')
                cameraMotionDetection = CameraMotionDetection('motion detection')
                motionSensorDetection = MotionSensorDetection('motion detection')
                super(MotionDetectionModule, self).addAbstraction(cameraMotionDetection)
                super(MotionDetectionModule, self).addAbstraction(motionSensorDetection)

        class GreenEnergyModule(Module):
            def __init__(self):
                Module.__init__(self, 'enable green energy mode')
                allElectricDevicesOff = AllElectricDevicesOff('enable green energy mode')
                lowPowerModeDevices = LowPowerModeDevices('enable green energy mode')
                super(GreenEnergyModule, self).addAbstraction(allElectricDevicesOff)
                super(GreenEnergyModule, self).addAbstraction(lowPowerModeDevices)

        class WarningNotification(Module):
            def __init__(self):
                Module.__init__(self, 'warning notification')
                textUsingSmartphone = TextUsingSmartphone('warning notification')
                warningUsingSpeaker = WarningUsingSpeaker('warning notification')
                warningUsingLightBulbs = WarningUsingLightBulbs('warning notification')
                super(WarningNotification, self).addAbstraction(textUsingSmartphone)
                super(WarningNotification, self).addAbstraction(warningUsingSpeaker)
                super(WarningNotification, self).addAbstraction(warningUsingLightBulbs)

        graphInit = ActuationGraph()

        cooldDownModule = CoolDownModule()
        heatingUpModule = HeatingUpModule()
        ventilizationModule = VentilizationModule()
        illuminationModule = IlluminationModule()
        motionDetectionModule = MotionDetectionModule()
        greenEnergyModule = GreenEnergyModule()
        warningNotification = WarningNotification()

        graphInit.addModule(cooldDownModule)
        graphInit.addModule(heatingUpModule)
        graphInit.addModule(ventilizationModule)
        graphInit.addModule(illuminationModule)
        graphInit.addModule(motionDetectionModule)
        graphInit.addModule(greenEnergyModule)
        graphInit.addModule(warningNotification)

        self.graph = graphInit

if __name__ == '__main__':
    eval = EvalActuationGraph()
