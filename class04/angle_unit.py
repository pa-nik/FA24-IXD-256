import os, sys, io
import M5
from M5 import *
from unit import AngleUnit
import time
import m5utils

angle_0 = None
angle_val = None

M5.begin()
angle_0 = AngleUnit((1, 2))

while True:
  M5.update()
  angle_val = angle_0.get_value()
  # remap the range of values from 0 - 65335 to 0 - 255:
  angle_val = int(m5utils.remap(angle_val, 0, 65535, 0, 255))
  print(angle_val)
  time.sleep_ms(500)


