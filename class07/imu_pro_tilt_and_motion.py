# IMU tilt and motion detection in X and Y axes 
# this example works on AtomS3 Lite with IMU Pro Unit 

import os, sys, io
import M5
from M5 import *
import time
import math
from hardware import *
from unit import IMUProUnit

imu_x_val = 0.0   # X-axis acceleration value now
imu_x_last = 0.0  # last X-axis acceleration value
imu_y_val = 0.0   # Y-axis acceleration value now
imu_y_last = 0.0  # last Y-axis acceleration value


M5.begin()

# configure built-in RGB LED on AtomS3 Lite:
rgb = RGB()

# configure I2C on PortA (red connector):
i2c0 = I2C(0, scl=Pin(39), sda=Pin(38), freq=100000)

# initialize IMU Pro unit:
imupro = IMUProUnit(i2c0)

# function that takes r, g, b values and
# returns combined rgb_color
def get_rgb_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

while True:
  M5.update()
  
  # read the IMU accelerometer values:
  imu_val = imupro.get_accelerometer()
  
  # print X, Y, Z IMU values separated by comma:
  # print(imu_val[0], ',', imu_val[1], ',', imu_val[2])
  
  # print X, Y, Z IMU values formatted with 2 points precision:
  imu_val_str  = '{:0.2f}'.format(imu_val[0]) + ', '
  imu_val_str += '{:0.2f}'.format(imu_val[1]) + ', '
  imu_val_str += '{:0.2f}'.format(imu_val[2])
  print(imu_val_str)
  
  # save the last X-axis acceleration value:
  imu_x_last = imu_x_val
  # update X-axis acceleration value:
  imu_x_val = imu_val[0]
  
  # save the last Y-axis acceleration value:
  imu_y_last = imu_y_val
  # update Y-axis acceleration value:
  imu_y_val = imu_val[1]
  
  r = 0
  g = 0
  b = 0
  
  # set r variable to 255 for Y-axis tilt:
  if imu_x_val < -0.5 or imu_x_val > 0.5:
    r = 255
  else:
    r = 0  # no X-axis tilt

  # set g variable to 255 for X-axis tilt:
  if imu_y_val < -0.5 or imu_y_val > 0.5:
    g = 255
  else:
    g = 0  # no Y-axis tilt
    
  # set b variable to 255 for X-axis motion:
  if (imu_x_val - imu_x_last > 0.5) or (imu_x_val - imu_x_last < -0.5):
    b = 255
  else:
    b = 0  # no X-axis motion
  
  rgb.fill_color(get_rgb_color(r, g, b))
  time.sleep_ms(100)
