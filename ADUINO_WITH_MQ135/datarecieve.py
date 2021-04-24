import serial
import time
import re


arduino = serial.Serial("COM4", 9600)
if not arduino.isOpen():
    arduino.open()
print(arduino.isOpen())

while True:
	data = arduino.readline(30).decode('utf-8')
	#print(data)

	formdata = [float(s) for s in re.findall(r'-?\d+\.?\d*', data)]
	print(formdata)
