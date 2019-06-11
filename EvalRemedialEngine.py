'''
    The evaluation of remediot!
'''

from UserInterface import *
from AbstractGraph import *
from Abstraction import *


class EvalActuationGraph:
    def __init__(self, performance_eval=False, number=0):
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
                DeviceInstance.__init__(self, True, 'light', deviceInfo)

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

        class HumidifierDeviceInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'humudifier', deviceInfo)

        class SmartphoneInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'text', deviceInfo)

        class SpeakerInstance(DeviceInstance):
            def __init__(self):
                deviceInfo = DeviceInfo("null", "null", "null", "null", "null")
                DeviceInstance.__init__(self, True, 'speaker', deviceInfo)


        class WarningUsingSpeaker(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'play warning sound',  moduleName, 0, ACTUATION)
                speakerInstance = SpeakerInstance()
                super(WarningUsingSpeaker, self).appendChildDeviceInstance(speakerInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('playing warning sound')
                return 'speaker.state = 1'

        class WarningUsingLightBulbs(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'flash warning lights',  moduleName, 0, ACTUATION)
                lightBulbsInstance = LightBulbsInstance()
                super(WarningUsingLightBulbs, self).appendChildDeviceInstance(lightBulbsInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('flash warning lights')
                return 'lightbulb.state = 1'

        class TextUsingSmartphone(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'text message to the user',  moduleName, 0, ACTUATION)
                smartphoneInstance = SmartphoneInstance()
                super(TextUsingSmartphone, self).appendChildDeviceInstance(smartphoneInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('text the user something')
                return 'text.state = 1'

        class AllElectricDevicesOff(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'turn off all electric devices', moduleName, 0, ACTUATION)
                allElectricDevicesInstance = AllElectricDevicesInstance()
                super(AllElectricDevicesOff, self).appendChildDeviceInstance(allElectricDevicesInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('turning off all of the electric devices')
                return 'all_devices.state = 0'

        class LowPowerModeDevices(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'set low-power model for all electric devices', moduleName, 0, ACTUATION)
                allElectricDevicesInstance = AllElectricDevicesInstance()
                super(LowPowerModeDevices, self).appendChildDeviceInstance(allElectricDevicesInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('setting low-power mode for all of the electric devices')
                return 'all_devices.lowerpower = 1'

        class MotionSensorDetection(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'detect motion by motion sensor', moduleName, 0, ACTUATION)
                motionSensorInstance = MotionSensorInstance()
                super(MotionSensorDetection, self).appendChildDeviceInstance(motionSensorInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('detecting the motion through motion sensor')
                return 'motion_sensor.state = 1'

        class CameraMotionDetection(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'detect motion by camera', moduleName, 0, SENSING)
                cameraInstance = CameraInstance()
                super(CameraMotionDetection, self).appendChildDeviceInstance(cameraInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('detecting the motion through camera')
                return 'camera.state = 1'

        class CurtainOpen(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'open the curtain', moduleName, 0, ACTUATION)
                curtainControlInstance = CurtainControlInstance()
                super(CurtainOpen, self).appendChildDeviceInstance(curtainControlInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('opening the curtain now')
                return 'curtain.state = 1'

        class LightBulbTurningOn(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'turn on light bulb', moduleName, 0, ACTUATION)
                lightBulbsInstance = LightBulbsInstance()
                super(LightBulbTurningOn, self).appendChildDeviceInstance(lightBulbsInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('turning on the light bulbs now')
                return 'lightbulb.state = 1'

        class DoorOpening(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'open the door', moduleName, 0, ACTUATION)
                doorControlInstance = DoorControlInstance()
                super(DoorOpening, self).appendChildDeviceInstance(doorControlInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('opening the doors now')
                return 'door.state = 1'

        class FirePlaceLightUp(Abstraction):
            def __init__(self):
                Abstraction.__init__(self, 'light up fireplace', 'heating up', 0, ACTUATION)
                firePlaceInstance = FirePlaceInstance()
                super(FirePlaceLightUp, self).appendChildDeviceInstance(firePlaceInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('lighting up the fireplace now')
                return 'fireplace.state = 1'

        class HeaterTurnOn(Abstraction):
            def __init__(self):
                Abstraction.__init__(self, 'turn on heater', 'heating up', 0, ACTUATION)
                heaterInstance = HeaterInstance()
                super(HeaterTurnOn, self).appendChildDeviceInstance(heaterInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('Turning on heater now')
                return 'heater.state = 1'

        class AirConditionerTurnOn(Abstraction):
            def __init__(self):
                Abstraction.__init__(self, 'turn on air conditioner', 'cooling down', 0, ACTUATION)
                acInstance = AirConditionerInstance()
                super(AirConditionerTurnOn, self).appendChildDeviceInstance(acInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('Turning on the HVAC now')
                return 'ac.state = 1'

        class HumidifierTurnOn(Abstraction):
            def __init__(self, name):
                Abstraction.__init__(self, 'turn on humidifier', name, 0, ACTUATION)
                humidifierInstance = HumidifierDeviceInstance()
                super(HumidifierTurnOn, self).appendChildDeviceInstance(humidifierInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('Turning on the humidifier now')
                return 'humidifier.state = 1'


        class WindowOpening(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'open the window', moduleName, 0, ACTUATION)
                windowInstance = WindowInstance()
                super(WindowOpening, self).appendChildDeviceInstance(windowInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('Opening the window now.')
                return 'window.state = 1'

        class FanTurnOn(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'turn on fan', moduleName, 0, ACTUATION)
                fanInstance = FanInstance()
                super(FanTurnOn, self).appendChildDeviceInstance(fanInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('Turning on the fan now')
                return 'fan.state = 1'

        class FanTurnOff(Abstraction):
            def __init__(self, moduleName):
                Abstraction.__init__(self, 'turn off fan', moduleName, 0, ACTUATION)
                fanInstance = FanInstance()
                super(FanTurnOff, self).appendChildDeviceInstance(fanInstance)

            def performFunc(self, printState=False):
                if printState:
                    print('Turning off the fan now')
                return 'fan.state = 0'

        class CoolDownModule(Module):
            def __init__(self):
                Module.__init__(self, 'cooling down')
                acTurnOn = AirConditionerTurnOn()
                acTurnOn.updateCost(100)
                fanTurnOn = FanTurnOn('cooling down')
                fanTurnOn.updateCost(10)
                windowOpening = WindowOpening('cooling down')
                windowOpening.updateCost(1)
                super(CoolDownModule, self).addAbstraction(acTurnOn)
                super(CoolDownModule, self).addAbstraction(fanTurnOn)
                super(CoolDownModule, self).addAbstraction(windowOpening)

        class IncreaseHumidityModule(Module):
            def __init__(self):
                Module.__init__(self, 'increase humidity')
                humidifierOn = HumidifierTurnOn('increase humidity')
                humidifierOn.updateCost(20)
                fanTurnOff = FanTurnOff('increase humidity')
                fanTurnOff.updateCost(1)
                super(IncreaseHumidityModule, self).addAbstraction(humidifierOn)
                super(IncreaseHumidityModule, self).addAbstraction(fanTurnOff)

        class HeatingUpModule(Module):
            def __init__(self):
                Module.__init__(self, 'heating up')
                heaterTurnOn = HeaterTurnOn()
                heaterTurnOn.updateCost(100)
                fireplaceLightUp = FirePlaceLightUp()
                fireplaceLightUp.updateCost(100)
                windowOpening = WindowOpening('heating up')
                windowOpening.updateCost(1)
                # print('#############################')
                # for instance in heaterTurnOn.childDeviceInstance:
                #     print(instance.name + "=>" + self.name)
                # print('#############################')
                super(HeatingUpModule, self).addAbstraction(heaterTurnOn)
                super(HeatingUpModule, self).addAbstraction(fireplaceLightUp)
                super(HeatingUpModule, self).addAbstraction(windowOpening)

        class VentilizationModule(Module):
            def __init__(self):
                Module.__init__(self, 'ventilization')
                fanTurnOn = FanTurnOn('ventilization')
                fanTurnOn.updateCost(10)
                doorOpening = DoorOpening('ventilization')
                doorOpening.updateCost(1)
                windowOpening = WindowOpening('ventilization')
                windowOpening.updateCost(1)
                super(VentilizationModule, self).addAbstraction(fanTurnOn)
                super(VentilizationModule, self).addAbstraction(doorOpening)
                super(VentilizationModule, self).addAbstraction(windowOpening)

        class IlluminationModule(Module):
            def __init__(self):
                Module.__init__(self, 'illumination')
                lightbulbTurningOn = LightBulbTurningOn('illumination')
                lightbulbTurningOn.updateCost(40)
                curtainOpen = CurtainOpen('illumination')
                curtainOpen.updateCost(1)
                super(IlluminationModule, self).addAbstraction(lightbulbTurningOn)
                super(IlluminationModule, self).addAbstraction(curtainOpen)

        class MotionDetectionModule(Module):
            def __init__(self):
                Module.__init__(self, 'motion detection')
                cameraMotionDetection = CameraMotionDetection('motion detection')
                cameraMotionDetection.updateCost(40)
                motionSensorDetection = MotionSensorDetection('motion detection')
                motionSensorDetection.updateCost(20)
                super(MotionDetectionModule, self).addAbstraction(cameraMotionDetection)
                super(MotionDetectionModule, self).addAbstraction(motionSensorDetection)

        class GreenEnergyModule(Module):
            def __init__(self):
                Module.__init__(self, 'enable green energy mode')
                allElectricDevicesOff = AllElectricDevicesOff('enable green energy mode')
                allElectricDevicesOff.updateCost(1)
                lowPowerModeDevices = LowPowerModeDevices('enable green energy mode')
                lowPowerModeDevices.updateCost(30)
                super(GreenEnergyModule, self).addAbstraction(allElectricDevicesOff)
                super(GreenEnergyModule, self).addAbstraction(lowPowerModeDevices)

        class WarningNotification(Module):
            def __init__(self):
                Module.__init__(self, 'warning notification')
                textUsingSmartphone = TextUsingSmartphone('warning notification')
                textUsingSmartphone.updateCost(5)
                warningUsingSpeaker = WarningUsingSpeaker('warning notification')
                warningUsingSpeaker.updateCost(20)
                warningUsingLightBulbs = WarningUsingLightBulbs('warning notification')
                warningUsingLightBulbs.updateCost(40)
                super(WarningNotification, self).addAbstraction(textUsingSmartphone)
                super(WarningNotification, self).addAbstraction(warningUsingSpeaker)
                super(WarningNotification, self).addAbstraction(warningUsingLightBulbs)

        class DummyModule(Module):
            def __init__(self, name):
                Module.__init__(self, name)
                fanTurOn = FanTurnOn('dummy')
                doorOpening = DoorOpening('dummy')
                windowOpening = WindowOpening('dummy')
                super(DummyModule, self).addAbstraction(fanTurOn)
                super(DummyModule, self).addAbstraction(doorOpening)
                super(DummyModule, self).addAbstraction(windowOpening)

        graphInit = ActuationGraph()

        if not performance_eval:
            cooldDownModule = CoolDownModule()
            heatingUpModule = HeatingUpModule()
            ventilizationModule = VentilizationModule()
            illuminationModule = IlluminationModule()
            motionDetectionModule = MotionDetectionModule()
            greenEnergyModule = GreenEnergyModule()
            warningNotification = WarningNotification()
            increaseHumidityModule = IncreaseHumidityModule()

            graphInit.addModule(cooldDownModule)
            graphInit.addModule(heatingUpModule)
            graphInit.addModule(ventilizationModule)
            graphInit.addModule(illuminationModule)
            graphInit.addModule(motionDetectionModule)
            graphInit.addModule(greenEnergyModule)
            graphInit.addModule(warningNotification)
            graphInit.addModule(increaseHumidityModule)
        else:
            for i in range(0, number):
                dummyModule = DummyModule(str(i))
                graphInit.addModule(dummyModule)

        self.graph = graphInit

if __name__ == '__main__':
    eval = EvalActuationGraph()
