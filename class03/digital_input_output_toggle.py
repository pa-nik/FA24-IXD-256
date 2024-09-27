# digital input / output example:
# using button on pin 7 to control an LED connected to pin 8

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

print('digital input + output example')

# initialize M5 board:
M5.begin()

# configure pin 8 as output:
output_pin = Pin(8, mode=Pin.OUT)
  
# configure pin 7 as input that is high by default:
input_pin = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)

while True:           # infinite loop
  M5.update()         # update M5 board
  #input_pin_val = input_pin.value()  # read input pin value
  input_pin_val = BtnA.wasPressed() 
  if input_pin_val == True:    # read input value
    output_pin_val = output_pin.value()  # read output value
    if output_pin_val == True:
      #output_pin.off()        # turn off output pin if input is True
      output_pin.value(0)
    else:
     #output_pin.on()         # turn on output pin if input is False
     output_pin.value(1)
  time.sleep_ms(100)  # wait for 100 milliseconds
    
