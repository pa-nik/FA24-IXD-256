# MQTT button publish to Adafruit IO feed

import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import network
from umqtt import *

ssid = 'INSERT_WIFI_NAME'
password = 'INSERT_WIFI_PASSWORD'

mqtt_client = None
aio_user_name = 'INSERT_ADAFRUIT_IO_USERNAME'
aio_password = 'INSERT_ADAFRUIT_IO_PASSWORD'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print('connect to WiFi...')
while wifi.isconnected() == False:
print('.', end='')
time.sleep_ms(100)

print('WiFi connection successful')
ip_list = wifi.ifconfig()
ip_address = ip_list[0]
print('IP address:', ip_address)

mqtt_client = MQTTClient(
  'testclient',
  'io.adafruit.com',
  port = 1883,
  user = aio_user_name,
  password = aio_password,
  keepalive = 3000
)
mqtt_client.connect(clean_session=True)  
mqtt_client.subscribe(aio_user_name+'/feeds/button-feed', feed_callback)

M5.begin()

while True:
  M5.update()
  
  if BtnA.wasPressed():
    print('button pressed..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', 'ON', qos=0)
  elif BtnA.wasReleased():
    print('button released..')
    mqtt_client.publish(aio_user_name+'/feeds/button-feed', 'OFF', qos=0)

  time.sleep_ms(100)  
  
