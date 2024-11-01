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
  if BtnA.wasPressed():
      print('b')
  time.sleep_ms(100)
    
