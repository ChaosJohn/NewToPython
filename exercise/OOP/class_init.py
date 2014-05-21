#!/usr/bin/python
# Filename: class_init.py

class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print 'Hello, myname is', self.name

p = Person('chaos')

p.sayHi()
