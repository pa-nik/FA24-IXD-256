# digital input / output example:
# using button on pin 7 to control an LED connected to pin 8

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

print('digital input + output toggle example')

# initialize M5 board:
M5.begin()

# configure pin 8 as output:
output_pin = Pin(8, mode=Pin.OUT)
  
# configure pin 7 as input that is high by default:
input_pin = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)
input_pin_val = input_pin.value()  # read input pin value


while True:           # infinite loop
  M5.update()         # update M5 board
  
  if input_pin_val == True:
    if input_pin.value() == False: # if the input pin is off (low or False)
      print('input pin changed from high to low')
      #input_pin_val = BtnA.wasPressed() # was the top button on ATOM board pressed?
      #if input_pin_val == True:    # read input value
      output_pin_val = output_pin.value()  # read output value
      if output_pin_val == True: # if output pin is on (high or True)
        #output_pin.off()        # turn off output pin if input is True
        #output_pin.value(0)     # set output pin low
        output_pin.value(False)  # set output pin low
      else:                      # output pin is off (low or False)
       #output_pin.on()          # turn on output pin if input is False
       #output_pin.value(1)      # set output pin high
       output_pin.value(True)    # turn output pin high
    
  input_pin_val = input_pin.value()  # read input pin value
  time.sleep_ms(100)  # wait for 100 milliseconds
    
