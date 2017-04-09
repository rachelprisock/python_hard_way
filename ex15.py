from sys import argv

script, filename = argv # uses argv to get the filename

txt = open(filename) # a function to open a new file

print "Here's your file %r:" % filename
print txt.read() # reads the contents of the file that was opened in line 5
# use the . to apply a function on a file
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
