#!/usr/bin/python
# Filename: pickling.py

import cPickle as p
# import pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store the object

shoplist = ['apple', 'mango', 'carrot']

# write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f)	# dump the object to a file
f.close()

del shoplist	# remove the shoplist

# read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
