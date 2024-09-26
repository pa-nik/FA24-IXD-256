# digital input / output example:
# using button on pin 7 to control an LED connected to pin 8

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

# initialize M5 board:
M5.begin()

# configure pin 8 as output:
pin8 = Pin(8, mode=Pin.OUT)

# configure pin 7 as input that is high by default:
pin7 = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)

while True:           # infinite loop
  M5.update()         # update M5 board
  if pin7.value():    # read pin 7 input value
    pin8.off()        # turn off pin 8 if input is True
  else:
    pin8.on()         # turn on pin 8 if input is False
  time.sleep_ms(100)  # wait for 100 milliseconds
    

