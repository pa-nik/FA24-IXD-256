# 
import os, sys, io
import M5
from M5 import *
from hardware import *
import time

# initialize M5 board:
M5.begin()

# configure analog to digital converter (ADC) on pin 1:
adc = ADC(Pin(1), atten=ADC.ATTN_11DB)
adc_val = None

while True:           # infinite loop
  M5.update()         # update M5 board
  
  # read analog value from ADC:
  adc_val = adc.read()
  print(adc_val)
  
  if BtnA.wasPressed():
      print('b')
      
  time.sleep_ms(100)
    
