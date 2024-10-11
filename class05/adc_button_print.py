# read ADC and button inputs and print values separated by comma
# use this code to test webserial_pyscript_template

import os, sys, io
import M5
from M5 import *
import time
import m5utils
from hardware import *

# configure analog to digital converter (ADC) on pin 1:
adc = ADC(Pin(1), atten=ADC.ATTN_11DB)
adc_val = None

button = Pin(41, mode=Pin.IN)
button_val = None


M5.begin()

while True:
  M5.update()
  
  # read analog value from ADC:
  adc_val = adc.read()
  
  # read digital value from top button:
  button_val = button.value()
  
  # remap the range of values from 0 - 4095 to 0 - 255:
  adc_val = int(m5utils.remap(adc_val, 0, 4095, 0, 255))
  
  print(adc_val, ',', button_val)
  
  time.sleep_ms(50)




