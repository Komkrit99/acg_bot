import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect('enkey.bu.ac.th')
client.publish('TEST/MQTT','GOTO 1.2358 2.98 90')