from abc import ABC, abstractmethod

class LightBulbInterface(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(LightBulbInterface):
    def turn_on(self):
        print("Light bulb turned on.")

    def turn_off(self):
        print("Light bulb turned off.")

class LightSwitch:
    def __init__(self, bulb: LightBulbInterface):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()  # Turn the light on
        self.bulb.turn_off() # Then off

# Create an instance of LightBulb
my_bulb = LightBulb()

# Create an instance of LightSwitch with the light bulb
my_switch = LightSwitch(my_bulb)

# Operate the switch to turn the bulb on and off
my_switch.operate()