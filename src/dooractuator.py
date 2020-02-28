import gpiozero


class DoorActuator():
    def __init__(self, config):
        """ Trigger door-strike actions by relays

        """

        self._config = config

        for door in self._config:
            relay = gpiozero.OutputDevice(self._config[door]["bcd_pin_number"], active_high=False, initial_value=False)
            self._config[door].update({"relay":relay})
            

    def unlock_door(self, index):
        print(f"Unlocking door {index}")
        self._config[index]["relay"].off()


    def lock_door(self, index):
        print(f"Locking door {index}")
        self._config[index]["relay"].on()

