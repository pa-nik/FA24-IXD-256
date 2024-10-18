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
  print(imu_data)
  time.sleep_ms(50)

