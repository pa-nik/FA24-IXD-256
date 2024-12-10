# non-blocking Serial input example for M5Stack AtomS3 Lite
# receive data beginning with 'A' or 'B' to change colors
# press button to send 'hello'

import os, sys, io
import M5
from M5 import *
from hardware import *
import time
from machine import UART
import uos
import select

M5.begin() 

# configure and turn on built-in RGB LED on AtomS3 Lite:
rgb = RGB()
rgb.fill_color(0x00ff00)  # green

print('serial input example for AtomS3 Lite')

while True:
  M5.update()
  
  if BtnA.wasPressed():
    rgb.fill_color(0xff0000)  # red
    print('hello')
    time.sleep_ms(500)

  # get data from python standard input:
  list = select.select([sys.stdin], [], [], 0)
  if list[0]:
    #print(ch)
    # read one input line:
    ch = sys.stdin.readline()
    if ch != '\n':
      if ch[0] == 'A':  # first character is 'A'
        rgb.fill_color(0x0000ff)  # blue
      else:  
        rgb.fill_color(0xff0066)  # purple
      time.sleep_ms(500)
      
  time.sleep_ms(100)

