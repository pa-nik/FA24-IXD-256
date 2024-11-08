import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import network

M5.begin()

ssid = 'INSERT_WIFI_NAME'
password = 'INSERT_WIFI_PASSWORD'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while wifi.isconnected() == False:
  print('.', end='')
  time.sleep_ms(100)

ip_list = wifi.ifconfig()
ip_address = ip_list[0]
print('IP address:', ip_address)

while True:
  M5.update()  
  # wait for 100 milliseconds (1/10 second):
  time.sleep_ms(100)