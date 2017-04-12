from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

from_file = open(from_file)
indata = from_file.read()
from_file.close()

to_file = open(to_file, 'w')
out_data = to_file.write(indata)
to_file.close()

print "Alright, all done."
