from sub import listener
from prepDB import prep_db
from dotenv import load_dotenv
import os

load_dotenv()

mqtt_server = os.getenv("MQTT_SERVER")
mqtt_port = int(os.getenv("MQTT_PORT")) # convert string to int
name = os.getenv("NAME")
passwd = os.getenv("PASSWD")

if __name__ == "__main__":
    #prep_db()
    listener(name, passwd, mqtt_server, mqtt_port)
