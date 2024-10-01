# assignment #1 example based on the diagram in assignment description
# RGB LED strip is configured on pin 2 (white 4-pin connector on the ATOM board)
# digital input is configured on pin 7 (black 5-pin connector on the ATOM board)

# this program uses program_state variable to keep track of state
# program begins in START state
#   RGB LED is initialized
# if digital input is high, program enters WAITING state
#   RGB LED pulsates blue
# if digital input is low, program enters RUN state
#   RGB LED fades in green
# if digital input is low for 5 seconds, program enters FINISH state
#   RGB LED fades in red, then fades out to black, program ends

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

print('assignment #1 example')

# variable to keep track of program state:
program_state = 'START'
print('program_state =', program_state)

# initialize M5 board:
M5.begin()

# configure built-in RGB LED (AtomS3 Lite only):
rgb = RGB()

# configure RGB strip connected to pin 2 with 30 LEDs enabled:
# rgb = RGB(io=2, n=30, type="SK6812")

# turn off rgb (fill with black):
rgb.fill_color(0)

# configure pin 8 as output:
#output_pin = Pin(8, mode=Pin.OUT)

# configure top button on AtomS3 as input:
# input_pin = Pin(41, mode=Pin.IN)
                
# configure pin 7 as input that is high by default:
input_pin = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)

print('finished setup..')

# function that takes r, g, b values and returns combined rgb_color:
def get_rgb_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

# function to set program_state variable and print it:
def set_program_state(state):
  global program_state
  program_state = state
  print('program_state =', program_state)
  
while True:           # infinite loop
  M5.update()         # update M5 board
  
  # conditions for changing from START to WAITING and RUN states:
  if program_state == 'START': # or program_state == 'WAITING' or program_state == 'RUN':
    #if input_pin_val == True:
    if input_pin.value() == True: # input pin is high
      set_program_state('WAITING')
    else:
      set_program_state('RUN')

  # pulsate RGB blue during WAITING state:
  if program_state == 'WAITING':
      
    # fade in RGB blue:
    for i in range(100):
      rgb_color = get_rgb_color(0, 0, i)
      rgb.fill_color(rgb_color)
      time.sleep_ms(2)
      
    # fade out RGB to black:
    for i in range(100):
      rgb_color = get_rgb_color(0, 0, 100-i)
      rgb.fill_color(rgb_color)
      time.sleep_ms(2)
      
    # condition for changing from WAITING to RUN state:
    if input_pin.value() == False: # input pin is low
      set_program_state('RUN')
      
  # fade in RGB green during RUN state:
  elif program_state == 'RUN':

    # fade in RGB to green:
    for i in range(100):
      rgb_color = get_rgb_color(0, i, 0)
      rgb.fill_color(rgb_color)
      time.sleep_ms(2)

    # wait 5 seconds, but keep check input pin every 100 milliseconds:
    for time_counter in range(50):
      time.sleep_ms(100)
      if input_pin.value() == True: # input pin is high
        break  # break the for loop (finish early)
    
    # condition for changing from RUN to WAITING state:
    if time_counter < 49:  # finished loop early due to input pin being high 
      set_program_state('WAITING')
    # condition for changing from RUN to FINISH state:
    else:
      print('5 seconds passed..')
      set_program_state('FINISH')
    
  # fade in RGB red and then fade out to black during FINISH state:
  elif program_state == 'FINISH':
    
    # fade in RGB from green to red
    for i in range(100):
      rgb_color = get_rgb_color(i, 100-i, 0)
      rgb.fill_color(rgb_color)
      time.sleep_ms(2)
      
    time.sleep(2) # wait 2 seconds
    print('2 seconds passed..')
    
    # fade out RGB from red to black
    for i in range(100):
      rgb_color = get_rgb_color(100-i, 0, 0)
      rgb.fill_color(rgb_color)
      time.sleep_ms(2)
      
    # turn off rgb (fill with black):
    rgb.fill_color(0)
      
    print('finished program')
    break  # break the while loop 
  
    




