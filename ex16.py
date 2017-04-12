# close - closes the file
# read - reads the contents of the file. can assign to a var
# readline - reads just one line of a text file
# truncate - empties the file
# write('stuff') - writes stuff to the file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#  W stands for writing permission for the opened file
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("line1\nline2\nline3")

print "And finally, we close it."
target.close()
