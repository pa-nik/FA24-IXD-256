# 
import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import m5utils

# initialize M5 board:
M5.begin()

# configure PWM on pin 38 (PortABC red connector)
pwm1 = PWM(Pin(38))

# configure PWM frequency at 50Hz for servo:
pwm1.freq(50)

# configure duty cycle to stop the servo:
duty_cycle = 75
pwm1.duty(duty_cycle)

# configure analog to digital converter (ADC) on pin 1:
adc = ADC(Pin(1), atten=ADC.ATTN_11DB)
adc_val = None

while True:           # infinite loop
  M5.update()         # update M5 board
  
  # read analog value from ADC:
  adc_val = adc.read()
  
  # remap the range of adc_val from 0 - 4095 to 30 - 130:
  duty_cycle = int(m5utils.remap(adc_val, 0, 4095, 30, 130))
  print('duty cycle = ', duty_cycle)
  pwm1.duty(duty_cycle)
  
  time.sleep_ms(100)
    



