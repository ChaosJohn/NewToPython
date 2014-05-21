#!/usr/bin/python
# Filename: using_sys.py

import sys

print 'The command line arguments are:'
for i in sys.argv:
	print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'

print '\n\nThe first string of sys.path is', sys.path[0], '\n'
print '\n\nThe sys.argv is', sys.argv, '\n'
print '\n\nThe first string of sys.argv is', sys.argv[0], '\n'
