# escape characters are good to escape a single quote or double quote

# \t is the tab escape character it allows you to print a tab
tabby_cat = "\tI'm tabbed in."
# \n is the newline escape character it allows you to print a new line
persian_cat = "I'm split\non a line."
# \ itself is an escape character so it escapes one of the two \s
backslash_cat = "I'm \\ a \\ cat."
# output will look like this I'm \ a \ cat.

# This is a great example of nice formatting
# it allows you to make a tab before each list item
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# output looks like this:
# I'll do a list:
	# * Cat food
	# * Fishies
	# * Catnip
	# * Grass

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# playing around with escape characters:
# prints a single quote
print "I\'m escaping here!"

# trying the triple-single-quote
print '''
What is up here?
Anyone know?
heyyyyyyyy
'''
# works just the same

# Note: not quite sure what is up with the \' that still prints a '
