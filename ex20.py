from sys import argv

script, input_file = argv

# a function to read the file
def print_all(f):
    print f.read()

# a function to rewind or jump to the beginning of the file
# 0 jumps to the beginning, 1 means seek relative to current position
# 2 means seek relative to the file's end
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 0
current_line += 1
print_a_line(current_line, current_file)
print_a_line(current_line, current_file)
print_a_line(current_line, current_file)
