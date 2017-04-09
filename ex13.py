# this is how you add modules to python
# acts as good documentation for future programmers
# argv is the argument variable
# the varible hold the arguments you pass to your script
from sys import argv

# this unpacks argv it's getting assigned to four variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# to run this you must pass three command line arguments
#  python ex13.py first 2nd 3rd

# if you give less than three arguments, then you will get a ValueError
