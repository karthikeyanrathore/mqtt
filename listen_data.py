#!/usr/bin/env python3

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print("connection is OK")
  else:
    print("bad connection")

def on_subscribe(client, obj , mid, granted_qos):
  print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, userdata, level, buf):
  print("log: ", buf)

def on_message(client, obj, msg):
  print("MQTT topic: %s and data: %s" % (msg.topic , msg.payload.decode('utf-8', 'ignore')))


client = mqtt.Client(client_id="bfb")

# call back functions
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_log = on_log


# connect client to broker
# MQTT_broker="mqtt.eclipseprojects.io"
MQTT_broker="192.168.29.224"

client.connect(MQTT_broker, 1883, 40)
# client.loop_start()

# subscribe (client here subscribed to client on publish_data.py through broker)
# multi-level(#)
# wild-card(+)
client.subscribe("industry/sensor/#", 0)

# loop on
client.loop_forever()
# client.loop_stop()

