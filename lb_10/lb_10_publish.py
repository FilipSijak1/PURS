from paho.mqtt import client as mqtt_client

broker= "192.168.86.211"
port= 1883
topic= "python"

def connect_mqtt():
    client= mqtt_client.Client("4_boda")
    client.connect(broker, port)

    return client

def run():
    client= connect_mqtt()
    client.loop_start()
    client.publish(topic, 100)
    client.loop_stop()

run()


