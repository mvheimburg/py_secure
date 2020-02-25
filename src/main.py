

import os, sys



from doorlockworker import DoorlockWorker


# Inspired from https://www.cloudmqtt.com/docs/python.html

server = os.environ.get('MQTT_SERVER', 'mqtt://localhost:1883')
uname = os.environ.get('MQTT_USERNAME', None)
password = os.environ.get('MQTT_PASSWORD', None)
client_id = os.environ.get('MQTT_CLIENT_ID', None)


NUMBER_OF_DOORS = 2
GPIO_actuator_startpin = 29

door_dict = {}


def main(fake = False):

    for i in range(1,NUMBER_OF_DOORS+1):
        door_dict.update({str(i):{"topic_cmd":f'door/{i}/cmd', "gpio_actuator":GPIO_actuator_startpin+(i-1)*2}})

    doorlockworker = DoorlockWorker(fake, client_id=client_id, num_doors=NUMBER_OF_DOORS, door_dict=door_dict)
    doorlockworker.connect_to_broker(server, uname, password)
    doorlockworker.subscribe()
    rc = doorlockworker.run()
    print(rc)




# Tests
if __name__ == '__main__':
    if 'fake' in sys.argv:
        main(fake=True)
    else:
        main()


# ustates = States(36, 38, 40)
