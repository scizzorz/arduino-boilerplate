#!/usr/bin/env python
import serial,os

port='/dev/ttyACM0';
baud=9600;

ser=serial.Serial(port,baud);

while True:
	line = ser.readline().strip();
	print line
