print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
# we add a , at the end of each print line so print doesn't end the line with a newline character
# Can also use raw_input like this:
#   name = raw_input("What is your name? ")
# in python there is also an input() method but it's generally best
#  to use raw_input b/c then you can do with the string what you want
#  instead of trying to have python figure out what data type the input is

# IN PYTHON 3 THERE IS NO RAW INPUT ONLY INPUT()

# another form
name = raw_input("What is your name? ")
favorite_color = raw_input("What is your favorite color? ")
velocity = raw_input("What is the air speed velocity of a sparrow? ")

print "%r likes %r and knows that a sparrow flies at %r." % (name, favorite_color, velocity)
