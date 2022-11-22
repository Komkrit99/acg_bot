import paho.mqtt.client as mqtt
import time
import base64
import numpy as np
import threading

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("MQTT Conneted.")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    print ("Message received: "  + message.payload)
    with open('/home/prem/test_robot_pose.txt','a+') as f:
         f.write("Message received: "  + message.payload + "\n")

Connected = False   #global variable for the state of the connection

broker_address= "192.168.0.6"  #Broker address
port = 1883                         #Broker port
user = "me"                    #Connection username
password = "abcdef"            #Connection password

client = mqtt.Client()               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.connect(broker_address,port,60) #connect
client.subscribe("some/topic") #subscribe
client.loop_forever() #then keep listening forever