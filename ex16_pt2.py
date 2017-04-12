from sys import argv

script, filename = argv

file = open(filename)

print file.read()
print "You've read the file we created in this exercise."
