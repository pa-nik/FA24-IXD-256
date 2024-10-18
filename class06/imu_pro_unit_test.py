import os, sys, io
import M5
from M5 import *
from hardware import *
from unit import IMUProUnit
import time

print('imu example')

M5.begin()

# configure I2C on bottom connector of Atom Board:
#i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)

# configure I2C on PortA (red connector):
i2c0 = I2C(0, scl=Pin(39), sda=Pin(38), freq=100000)

# initialize IMU Pro unit:
imupro_0 = IMUProUnit(i2c0)

while True:
  M5.update()
  
  imu_data = imupro_0.get_accelerometer()
  #print(imu_data)
  
  acc_x = imu_data[0]  # X acceleration value
  acc_y = imu_data[1]  # Y acceleration value
  acc_z = imu_data[2]  # Z acceleration value
  
  # print acceleration values separated by comma:
  print(acc_x, ',', acc_y, ',', acc_z)
  
  time.sleep_ms(50)
