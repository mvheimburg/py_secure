import os, sys
import yaml

from doorlockworker import DoorlockWorker

server = os.environ.get('MQTT_SERVER', 'mqtt://localhost:1883')
uname = os.environ.get('MQTT_USERNAME', None)
password = os.environ.get('MQTT_PASSWORD', None)
client_id = os.environ.get('MQTT_CLIENT_ID', None)


def main():

    cfg = None
    current_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_dir, "config.yaml")
    with open(path, 'r') as stream:
        cfg = yaml.load(stream, Loader=yaml.FullLoader)
    print(cfg)

    doorlockworker = DoorlockWorker(client_id=client_id, config=cfg['doors'])
    doorlockworker.connect_to_broker(server, uname, password)
    doorlockworker.subscribe()
    rc = doorlockworker.run()
    print(rc)




# Tests
if __name__ == '__main__':
    main()


# ustates = States(36, 38, 40)
