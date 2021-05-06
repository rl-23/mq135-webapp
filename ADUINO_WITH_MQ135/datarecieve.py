import serial
import time
import re
from flask import Flask, redirect, url_for, render_template
import random


datalist = []

arduino = serial.Serial("COM4", 9600)
if not arduino.isOpen():
    arduino.open()
    print(arduino.isOpen())
	  
while True:

    data = arduino.readline(20).decode('utf-8')
    re.sub(r'[^\w]', ' ', data)

    datalist.append(data)
    
    f =  open("appdatareads.txt", "w")
    insertthis = datalist[-1]
    f.write(str(insertthis))
    f.close()

    print(datalist)


