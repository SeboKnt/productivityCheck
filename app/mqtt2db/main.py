from sub import listener
from prepDB import prep_db
from dotenv import load_dotenv
import os

load_dotenv()

mqtt_server = os.getenv("MQTT_SERVER")
mqtt_port = int(os.getenv("MQTT_PORT")) # convert string to int
mqtt_name = os.getenv("MQTT_NAME")
mqtt_passwd = os.getenv("MQTT_PASSWD")
db_user = os.getenv("DB_USER")
db_passwd = os.getenv("DB_PASSWD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")


if __name__ == "__main__":
    prep_db(db_user, db_passwd, db_host, db_name)
    listener(mqtt_name, mqtt_passwd, mqtt_server, mqtt_port, db_user, db_passwd, db_host, db_name)
