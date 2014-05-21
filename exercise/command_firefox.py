#!/usr/bin/python
# Filename: command_firefox.py

import os

if os.system('firefox&') == 0:
	print 'Successful launch firefox'
else:
	print 'Launch Failed'
