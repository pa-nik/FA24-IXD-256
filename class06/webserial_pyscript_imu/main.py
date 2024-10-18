import js as p5
from js import document

imu_data = [0, 0, 0]

acc_x = 0
acc_x_last = 0
acc_y = 0
acc_y_last = 0

def setup():
  p5.createCanvas(300, 300)
  print('IMU data example')

def draw():
  global acc_x, acc_x_last
  global acc_y, acc_y_last

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
  acc_y = imu_data[1]
  
  # show red rectangle if there is X motion:
  if (abs(acc_x - acc_x_last) > 0.5):
    p5.fill(255, 0, 0)
    p5.rect(100, 10, 15)
    acc_x_last = acc_x

  # show green rectangle if there is Y motion:
  if (abs(acc_y - acc_y_last) > 0.5):
    p5.fill(0, 255, 0)
    p5.rect(100, 25, 15)
    acc_y_last = acc_y

  # map the X acceleration to range 0 - 255
  r = p5.map(acc_x, -5.0, 5.0, 0, 255)

  # map the Y acceleration to range 0 - 255
  g = p5.map(acc_y, -5.0, 5.0, 0, 255)
  
  # change red component of color according to X acceleartion:
  p5.fill(r, g, 0)

  p5.ellipse(p5.width/2, p5.height/2, 100)


  
