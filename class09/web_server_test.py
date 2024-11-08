import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import network
from usocket import *

M5.begin()

ssid = 'INSERT_WIFI_NAME'
password = 'INSERT_WIFI_PASSWORD'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while wifi.isconnected() == False:
  print('.', end='')
  time.sleep_ms(100)

ip_list = wifi.ifconfig()
ip_address = ip_list[0]
print('IP address:', ip_address)

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

program_state = 'ON'

def web_page():
    global program_state
    html = """
    <html>
        <head>
            <title>Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,">
            <style>
                html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                h1{color: #0F3376; padding: 2vh;}
                p{font-size: 1.5rem;}
                .button{display: inline-block; background-color: #e7bd3b; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                .button2{background-color: #4286f4;}
            </style>
        </head>
        <body>
            <h1>Web Server</h1> 
            <p>program state: <strong>""" + program_state + """</strong></p>
            <p><a href="/?state=on"><button class="button">ON</button></a></p>
            <p><a href="/?state=off"><button class="button button2">OFF</button></a></p>
        </body>
    </html>"""
    return html

while True:
    M5.update()
    
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    #print('Request =', request)
    
    state_on = request.find('/?state=on')
    state_off = request.find('/?state=off')
    
    if state_on == 6:
        program_state = 'ON'
        print(program_state)
    elif state_off == 6:
        program_state = 'OFF'
        print(program_state)
    
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    
    # wait for 100 milliseconds (1/10 second):
    time.sleep_ms(100)