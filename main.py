from sub import listener
from distance import distance
from dotenv import load_dotenv
import os

load_dotenv()

mqtt_server = os.getenv("MQTT_SERVER")
mqtt_port = os.getenv("MQTT_PORT") 
name = os.getenv("NAME")
passwd = os.getenv("PASSWD")

if __name__ == "__main__":
    mqtt_port = int(mqtt_port) # convert string to int

    listener(name, passwd, mqtt_server, mqtt_port)
    #distance(name, passwd, mqtt_server, mqtt_port)
