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

# configure RGB strip connected to pin 2 with 10 LEDs enabled:
rgb_strip = RGB(io=2, n=10, type="SK6812")

# fill all pixels of rgb_strip to green color:
rgb_strip.fill_color(0x00ffff)
time.sleep_ms(1000)  # wait 1 second

r = 0
g = 255
b = 0
# convert r, g, b colors to one number:
rgb_color = (r << 16) | (g << 8) | b
print('decimal rgb_color =', rgb_color)
print('hexadecimal rgb_color =', hex(rgb_color))
print('binary rgb_color =', bin(rgb_color))

# fill all pixels of rgb_strip with rgb_color:
rgb_strip.fill_color(rgb_color)

# variable to keep track of program state:
program_state = 'GREEN'

# configure pin 8 as output:
output_pin = Pin(8, mode=Pin.OUT)
  
# configure pin 7 as input that is high by default:
input_pin = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)
input_pin_val = input_pin.value()  # read input pin value

# function that takes r, g, b values and
# returns combined rgb_color
def get_rgb_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

# function that toggles output pin (change it to opposite state)
def output_toggle():
  global output_pin_val, output_pin
  global program_state, rgb_strip
  
  print('output toggle')
  if output_pin.value() == True: # if output pin is on (high or True)
    output_pin.value(False)      # set output pin low
  else:                          # if output pin is off (low or False)
    output_pin.value(True)       # turn output pin high
   
  # if program_state is GREEN change it to YELLOW: 
  if program_state == 'GREEN':
    program_state = 'YELLOW'
    
    # fill rgb_strip with yellow using a hexadecimal value:
    # rgb_strip.fill_color(0xffff00)
    # fill rgb_strip with yellow using r, g, b values:
    # yellow = get_rgb_color(255, 255, 0)
    # rgb_strip.fill_color(yellow)
    
    # fade from green to yellow:
    for i in range(255):
      rgb_strip.fill_color(get_rgb_color(i, 255, 0))
      time.sleep_ms(5)
    
  # otherwise if program_state is YELLOW change it to RED: 
  elif program_state == 'YELLOW':
    program_state = 'RED'
    # fade from yellow to red:
    for i in range(255):
      rgb_strip.fill_color(get_rgb_color(255, 255-i, 0))
      time.sleep_ms(5)
  
  # otherwise if program_state is RED change it to GREEN:
  elif program_state == 'RED':
    program_state = 'GREEN'
    # fade from red to green:
    for i in range(255):
      rgb_strip.fill_color(get_rgb_color(255-i, i, 0))
      time.sleep_ms(5)
    
  print('program_state =', program_state)
  
  
while True:           # infinite loop
  M5.update()         # update M5 board
  
  if input_pin_val == True:
    if input_pin.value() == False: # if the input pin is off (low or False)
      print('input pin changed from high to low')
      output_toggle()
      
  input_pin_val = input_pin.value()  # read input pin value
  time.sleep_ms(100)  # wait for 100 milliseconds
    

