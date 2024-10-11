import os, sys, io
import M5
from M5 import *
import time
from hardware import *
import m5utils

adc_val = None

M5.begin()

# configure analog to digital converter (ADC) on pin 1:
adc = ADC(Pin(1), atten=ADC.ATTN_11DB)

# configure RGB strip on pin 38 (red connector) with 30 LEDs enabled:
rgb_strip = RGB(io=38, n=30, type="SK6812")

# function that takes r, g, b values and returns combined rgb_color:
def get_rgb_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

while True:
  M5.update()
  
  # read analog value from ADC:
  adc_val = adc.read()
  
  # remap the range of adc_val from 0 - 4095 to 0 - 255:
  adc_val = int(m5utils.remap(adc_val, 0, 4095, 0, 255))

  # change red color of RGB strip according to adc_val:
  rgb_color = get_rgb_color(255 - adc_val, 0, 0)
  rgb_strip.fill_color(rgb_color)
  
  print(adc_val)
  time.sleep_ms(100)



