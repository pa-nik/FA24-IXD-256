import os, sys, io
import M5
from M5 import *
from hardware import *
from unit import IMUProUnit
import time

print('imu example')

M5.begin()
i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
imupro_0 = IMUProUnit(i2c0)

while True:
  M5.update()
  imu_data = imupro_0.get_accelerometer()
  print(imu_data)
  time.sleep_ms(50)
