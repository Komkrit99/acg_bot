import paho.mqtt.client as mqtt
host = 'test.mosquitto.org'
port = 1883

def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe("BURL/MOVE")

def on_message(client, userdata,msg):
    print(msg.payload.decode("utf-8", "strict"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()