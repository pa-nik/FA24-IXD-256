import os, sys, io
import M5
from M5 import *
from unit import AngleUnit
import time
from hardware import *
import m5utils

angle_0 = None
angle_val = None

M5.begin()

# configure ANGLE unit:
angle_0 = AngleUnit((1, 2))

# configure RGB strip connected to pin 2 with 30 LEDs enabled:
rgb_strip = RGB(io=38, n=30, type="SK6812")

# function that takes r, g, b values and
# returns combined rgb_color
def get_rgb_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

while True:
  M5.update()
  angle_val = angle_0.get_value()
  # remap the range of values from 0 - 65335 to 0 - 255:
  angle_val = int(m5utils.remap(angle_val, 0, 65535, 0, 255))
  
  # use angle_val as red component of rgb_color
  rgb_color = get_rgb_color(angle_val, 0, 0)
  rgb_strip.fill_color(rgb_color)
  
  print(angle_val)
  time.sleep_ms(100)



