# built-in IMU test for AtomS3 board
# does not work on AtomS3 Lite

import os, sys, io
import M5
from M5 import *
import time

M5.begin()

while True:
  M5.update()
  
  imu_data = Imu.getAccel()
  #print(imu_data)
  
  acc_x = imu_data[0]  # X acceleration value
  acc_y = imu_data[1]  # Y acceleration value
  acc_z = imu_data[2]  # Z acceleration value
  
  # print acceleration values separated by comma:
  print(acc_x, ',', acc_y, ',', acc_z)
  
  time.sleep_ms(50)

