# IMU tilt and motion detection in X and Y axes 
# this example works on AtomS3 with bult-in IMU

import os, sys, io
import M5
from M5 import *
import time
import math

imu_x_val = 0.0   # X-axis acceleration value now
imu_x_last = 0.0  # last X-axis acceleration value
imu_y_val = 0.0   # Y-axis acceleration value now
imu_y_last = 0.0  # last Y-axis acceleration value


M5.begin()

# display title at the top of the screen:
title = Widgets.Title("IMU motion", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)

# display text labels:
label0 = Widgets.Label("tilt or move", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
label1 = Widgets.Label("up, down", 3, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
label2 = Widgets.Label("left, right", 3, 60, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
label3 = Widgets.Label("--", 3, 80, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)

time.sleep(5)  # delay 5 seconds

while True:
  M5.update()
  
  # read the IMU accelerometer values:
  imu_val = Imu.getAccel()
  
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
  
  # display RIGHT or LEFT according to X-axis tilt:
  if imu_x_val < -0.5:
    label0.setText('RIGHT')
  elif imu_x_val > 0.5:
    label0.setText('LEFT')
  else:
    label0.setText('no X tilt')

  # display UP or DOWN according to Y-axis tilt:
  if imu_y_val < -0.5:
    label1.setText('DOWN')
  elif imu_y_val > 0.5:
    label1.setText('UP')
  else:
    label1.setText('no Y tilt')
    
  # display X MOTION according to change in X-axis:
  if (imu_x_val - imu_x_last > 0.5) or (imu_x_val - imu_x_last < -0.5):
    label2.setText('X MOTION')
  else:
    label2.setText('no X motion')

  # display Y MOTION according to change in Y-axis:
  if (imu_y_val - imu_y_last > 0.5) or (imu_y_val - imu_y_last < -0.5):
    label3.setText('Y MOTION')
  else:
    label3.setText('no Y motion')
  
  time.sleep_ms(100)