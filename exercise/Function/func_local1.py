#!/usr/bin/python
# Filename: func_local1.py

def func(x):
	print 'x is', x
	x = 2
	print 'Changed loacl x to ', x

x = 50

func(50)

print 'x is still', x
