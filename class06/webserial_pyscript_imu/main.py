import js as p5
from js import document

imu_data = [0, 0, 0]

def setup():
  p5.createCanvas(300, 300)
  print('IMU data example')

def draw():
  p5.background(255)

  data = document.getElementById("data").innerText
  
  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText

  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  imu_data[0] = float(data_list[0])
  if (len(data_list)> 1):
    imu_data[1] = float(data_list[1])
  if (len(data_list)> 1):
    imu_data[2] = float(data_list[2])

  p5.fill(0)
  for i in range(3):
    p5.text(imu_data[i], 10, 20 + i*15)

  acc_x = imu_data[0]

  # map the X acceleration to range 0 - 255
  r = p5.map(acc_x, -5.0, 5.0, 0, 255)

  p5.fill(r, 0, 0)
  p5.ellipse(p5.width/2, p5.height/2, 100)


  
