#!/usr/bn/python
# Filename: func_param.py

def printMax(a, b):
	if a > b:
		print a, 'is maxium'
	else:
		print b, 'is maxium'

printMax(3, 4)	# directly give literal values

x = 5
y = 7

printMax(x, y) 	# give variables as arguments

x = int(raw_input('Please enter first integer: '))
y = int(raw_input('Plseae enter second integer: '))

printMax(x, y)

x = float(raw_input('Please enter first float: '))
y = float(raw_input('Please enter second float: '))

printMax(x, y)
