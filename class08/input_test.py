# 
import os, sys, io
import M5
from M5 import *
from hardware import *
import time

# initialize M5 board:
M5.begin()

while True:           # infinite loop
  M5.update()         # update M5 board
  # input function waits for input on serial connection:
  input_data = input('type something and press return: ')
  print(input_data)
  time.sleep_ms(100)
    

