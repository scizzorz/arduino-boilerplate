#!/usr/bin/env python
import serial

# TODO how can this select with a wildcard?
port='/dev/ttyACM0';
baud=9600;

ser=serial.Serial(port,baud);

while True:
	line = ser.readline().strip();
	print line
