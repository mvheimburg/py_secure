

import threading
import time

 #WirePI

# GPIO.BCM

class DoorActuator():
    def __init__(self, fake, num_doors, door_dict):
        """ Trigger actions by relays connected between the Hormann door and GPIOs of the Raspberry Pi.

        The GPIO_door1 is the GPIO number of the board connected to a relay connected door1 strike
        The GPIO_door2 is the GPIO number of the board connected to a relay connected door2 strike
        The GPIO_door3 is the GPIO number of the board connected to a relay connected door3 strike

        """
        if fake:
            import sys
            import fake_rpi
            sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)
            sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)
        
        else:
            import RPi.GPIO as GPIO

        self._num_doors = num_doors
        self._door_dict = door_dict

        GPIO.setwarnings(False)
        # See https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
        GPIO_MODE = GPIO.BOARD 

        #GPIO Pin Setup
        GPIO.setmode(GPIO_MODE)

        for i in range(1,self._num_doors):
            GPIO.setup(self._door_dict[str(i)]["gpio_actuator"], GPIO.OUT, initial=GPIO.HIGH)

    def open_door(self):
        GPIO.output(pin, GPIO.HIGH)

    def close_door(self):
        GPIO.output(pin, GPIO.LOW)

    def open_door(self, index):
        if index > self._num_doors:
            #TODO: Raise error
            pass
        else:
            self.open_door(self._door_dict[str(index)]["gpio_actuator"])

    def close_door1(self, index):
        if index > self._num_doors:
            #TODO: Raise error
            pass
        else:
            self.close_door(self._door_dict[str(index)]["gpio_actuator"])
