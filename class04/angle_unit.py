import os, sys, io
import M5
from M5 import *
from unit import AngleUnit
import time

angle_0 = None
angle_val = None

M5.begin()
angle_0 = AngleUnit((1, 2))

while True:
  M5.update()
  angle_val = angle_0.get_value()
  print(angle_val)
  time.sleep_ms(500)


