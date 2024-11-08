# basic MicroPython template for M5Stack hardware such as AtomS3

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

M5.begin() 

# display title and label on AtomS3 with with a screen:
# display title ("title text", text offset, fg color, bg color, font):
#title0 = Widgets.Title("TITLE", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
# display label ("label text", x, y, layer number, fg color, bg color, font):
#label0 = Widgets.Label("label", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)

# configure and turn on built-in RGB LED on AtomS3 Lite:
#rgb = RGB()
#rgb.fill_color(0xff6600)  # orange

while True:
  M5.update()  
  # wait for 100 milliseconds (1/10 second):
  time.sleep_ms(100)