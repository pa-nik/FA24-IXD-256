# digital output example:
# blink an LED connected to pin 8

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

# initialize M5 board:
M5.begin()

# configure pin 8 as output:
pin8 = Pin(8, mode=Pin.OUT)

while True:           # infinite loop
  M5.update()         # update M5 board
  pin8.on()           # turn on pin 8
  time.sleep_ms(500)  # wait for 500 milliseconds
  pin8.off()          # turn off pin 8 
  time.sleep_ms(500)  # wait for 100 milliseconds
    


