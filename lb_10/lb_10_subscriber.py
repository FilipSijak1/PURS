import paho.mqtt.client as mqtt_client

broker= "192.168.86.211"
port= 1883
topic= "python"

def on_message(client, userdata, msg):
    print(str(msg.payload))

def connect_mqtt():
    client = mqtt_client.Client("moze_i_2")
    client.connect(broker, port)
    client.on_message= on_message

    return client

def run():
    client = connect_mqtt()
    client.subscribe(topic)
    client.loop_forever()

if __name__ == '__main__': 
    run()

