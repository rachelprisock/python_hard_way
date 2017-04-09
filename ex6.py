# note to self: to switch python environments use:
# source active py27

# %d is a format string for a digit, 10 is a digit so we need that
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# we can pass multiple format strings into a string, by including them after the % in parens ()
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r displays raw data of the variable. Best for debugging not for displaying to end users
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# above is the concatenation of strings, we can see that we can add two strings together

# the joke in the output is funny b/c in binary 1,0 = 2 not 10
