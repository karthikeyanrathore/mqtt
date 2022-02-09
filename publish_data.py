#!/usr/bin/env python3

print("hello world")
import paho.mqtt.client as mqtt
import socket
import time

def on_log(client, userdata, level, buf):
  print("log: ", buf)

def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print("connection is OK")
  else:
    print("bad connection")

def on_disconnect(client, userdata, flags, rc=0):
  print("diconnected ", str(rc))

#MQTT_broker="mqtt.eclipseprojects.io"
MQTT_broker="192.168.29.224"

# client
client = mqtt.Client(client_id="cfc")

# call back function
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log


# connect client to broker
client.connect(MQTT_broker ,1883,40)
client.loop_start()

# publish
TOPIC1="industry/sensor/heat"
TOPIC2="industry/sensor/cool"
client.publish(TOPIC1, "24f")
client.publish(TOPIC2, "-1f")



# loop end 
client.loop_stop()
client.disconnect()
#client.loop_forever()


