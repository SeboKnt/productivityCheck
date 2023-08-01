from sub import listener

def distance(name, passwd, mqtt_server, mqtt_port):

    listener(name, passwd, mqtt_server, mqtt_port)
    try:
        if distance <= 1.0:
            print("Watch ist nicht nahe des Schreibtisches")
    except KeyboardInterrupt:
        print("Verbindung zum MQTT-Broker beendet.")
