# 
import os, sys, io
import M5
from M5 import *
from hardware import *
import time

# initialize M5 board:
M5.begin()

# configure PWM on pin 38 (PortABC red connector)
pwm1 = PWM(Pin(38))

# configure PWM frequency at 50Hz for servo:
pwm1.freq(50)

# configure duty cycle to stop the servo:
duty_cycle = 75
pwm1.duty(duty_cycle)

# try values between 60 to 90 for 360 degree servo

while True:           # infinite loop
  M5.update()         # update M5 board
  # input function waits for input on serial connection:
  input_data = input('type duty cycle value and press return: ')
  duty_cycle = int(input_data)
  pwm1.duty(duty_cycle)
  print('duty cycle = ', duty_cycle)
  time.sleep_ms(100)
    


