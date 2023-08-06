import json
from db import insert_db
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Verbunden mit MQTT-Broker mit dem Code: " + str(rc))
    client.subscribe("espresense/rooms/schreibtisch")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    data = json.loads(payload)
    if data.get("id") == "apple:watch6-4":
        name = data.get("name")
        distance = data.get("distance")
        #insert_db(name, distance)
        print(" Name: " + name + " Distance: " + str(distance))

def listener(name, passwd, mqtt_server, mqtt_port):

    client = mqtt.Client()
    client.username_pw_set(name, passwd)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(mqtt_server, mqtt_port, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print("Verbindung zum MQTT-Broker beendet.")