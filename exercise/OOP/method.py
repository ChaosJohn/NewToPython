#!/usr/bin/python
# Filename: method.py

class Person:
	def sayHi(self):
#	def sayHi():	# must give the param - 'self'
		print 'Hello, how are you?'

p = Person()
p.sayHi()


