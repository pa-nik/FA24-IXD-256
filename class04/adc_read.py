import os, sys, io
import M5
from M5 import *
import time
import m5utils
from hardware import *

adc1 = ADC(Pin(1), atten=ADC.ATTN_11DB)
angle_val = None

M5.begin()

while True:
  M5.update()
  angle_val = adc1.read()
  # remap the range of values from 0 - 4095 to 0 - 255:
  angle_val = int(m5utils.remap(angle_val, 0, 4095, 0, 255))
  print(angle_val)
  time.sleep_ms(500)



