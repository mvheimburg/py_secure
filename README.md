# Home lock control

This project is intended to lock and unlock my outer doors by electric strike actuation via relays to provide 24

Requirements:
 - RaspberryPi (I am using a "Rpi Zero 3b")
 - 3 Relays

Dependencies:
```
sudo apt-get install python-pip
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install paho-mqtt

WiringPi might be preinstalled with raspbian
git clone git://git.drogon.net/wiringPi
cd wiringPi && cat INSTALL
```

## Reading Outputs

 - Ground pin (e.g. Board GPIO 34) of the Raspberry Pi should be connected to the UAP1 connectors S0{1,2,3}.5
 - The Board GPIO number 36 is connected to the DOOR1 connector S01.8 (door closed)
 - The Board GPIO number 38 is connected to the DOOR2 connector S02.8 (door closed)
 - The Board GPIO number 40 is connected to the DOOR3 connector S03.8 (door closedn)

Launch alone UAP1States.py to monitor the states of your door during 60 secondes.

## Actions

 - Raspberry Pi GPIO 29 to a solid state relay actuating the strike of DOOR1
 - Raspberry Pi GPIO 31 to a solid state relay actuating the strike of DOOR2
 - Raspberry Pi GPIO 33 to a solid state relay actuating the strike of DOOR3


## MQTT Controller

MQTT.py takes care of communicate the state of the door and of the
light of the motor via resp. MQTT topics:

 - `state/${MQTT_CLIENTID}/door1`
 - `state/${MQTT_CLIENTID}/door2`
 - `state/${MQTT_CLIENTID}/door2`

Plus, it executes commands received on:

 - `command/${MQTT_CLIENTID}/door1` allows messages: LOCK, UNLOCK
 - `command/${MQTT_CLIENTID}/door2` allows messages: LOCK, UNLOCK
 - `command/${MQTT_CLIENTID}/door3` allows messages: LOCK, UNLOCK

Following parameters can be set via global environment variables :

 - `${MQTT_SERVER}` for the server URI (e.g. "mqtt://10.8.0.42:1883")
 - `${MQTT_USERNAME}` for authenticate on the MQTT\_SEVER, can be null
 - `${MQTT_PASSWORD}` for authenticate on the MQTT\_SEVER, can be null
 - `${MQTT_CLIENT_ID}` identifies the MQTT client and the door (part of the
topic)

MQTT.py is the main file to launch.
 
