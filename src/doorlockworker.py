import paho.mqtt.client as mqtt
import urllib.parse

from dooractuator import DoorActuator



class DoorlockWorker():
    def __init__(self, fake, client_id=None, num_doors=0, door_dict=None):
        print(client_id)
        self._mqttc = mqtt.Client(client_id)
        self._num_doors = num_doors
        self._door_dict = door_dict
        self._dooractuator = DoorActuator(fake, num_doors, door_dict)
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_publish = self.mqtt_on_publish
        self._mqttc.on_subscribe = self.mqtt_on_subscribe

    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))
        print(f"flag: {flags}")

    def mqtt_on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

        if not msg.retain:
            pass

        # fmt_date = time.strftime("%Y-%m-%d %H:%M")
        # if not msg.retain:
        #     rcv = msg.payload.lower()
        #     force_update = True
        #     if msg.topic == topic_command_light:
        #         if ustates.get_str_light().lower() != rcv:
        #             uactions.light()
        #     if msg.topic == topic_command_door:
        #         if ustates.get_str_door().lower() != rcv:
        #             print("[{}] Received {} command".format(fmt_date, rcv))
        #             if rcv == "close":
        #                 uactions.close()
        #             if rcv == "open":
        #                 uactions.open()
        #             if rcv == "slight":
        #                 uactions.slightly_open()

    def mqtt_on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def mqtt_on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def mqtt_on_log(self, mqttc, obj, level, string):
        print(string)

    def tls_set(self):
        #TODO: sett ssl and cert for encrypt
        pass

    def connect_to_broker(self, server, username=None, password=None):
        print(f"connecting to server {server}")
        print(f"Username: {username}, Password: {password}")
        server_parsed = urllib.parse.urlparse(server)
        self._mqttc.username_pw_set(username, password=password)
        self._mqttc.connect(server_parsed.hostname, port=server_parsed.port, keepalive=60)

    def subscribe(self):
        for i in range(1,self._num_doors):
            topic = self._door_dict[str(i)]["topic_cmd"]
            print(f"subscribing to topic: {topic}")
            self._mqttc.subscribe(topic, qos=0)

    def run(self):     

        rc = 0
        while rc == 0:

            rc = self._mqttc.loop()

        return rc




# time.sleep(1)
# while rc == 0:
#     door_state = ustates.get_door()
#     light_state = ustates.get_light()
#     curr_time = time.time()
#     fmt_date = time.strftime("%Y-%m-%d %H:%M")
#     if last_door_state != door_state or curr_time - last_door_update > UPDATE_TIME or force_update:
#         last_door_update = time.time()
#         last_door_state = door_state
#         print("[{}] publishing new door state {}".format(fmt_date, ustates.get_str_door()))
#         mqttc.publish(topic_status_door, ustates.get_str_door())
#     if last_light_state != light_state or curr_time - last_light_update > UPDATE_TIME or force_update:
#         last_light_update = time.time()
#         last_light_state = light_state
#         print("[{}] publishing new light state {}".format(fmt_date, ustates.get_str_light()))
#         mqttc.publish(topic_status_light, ustates.get_str_light())
#     force_update = False
#     rc = mqttc.loop()
#     time.sleep(0.3)
# print("[{}] exited ! rc: {}".format(fmt_date, rc))