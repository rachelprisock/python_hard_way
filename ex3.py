from __future__ import division

print "I will now count my chickens:"

# PEMDAS so 30 / 6 = 5 and 25 + 5 = 30
print "Hens", 25 + 30 / 6
# 25 * 3 = 75, 75 % 4 = 3, so 100 - 3 = 97
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# 4 % 2 = 0, 1 / 4 (no floats with /) = 0
# so 3 + 2 + 1 - 5 + 0 - 0 + 6 = 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

# 5 < -2 False.
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is is greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# NOTE: this difference in division between Python 2 and 3.
# If I ran this file using Python 3 I would get floating
# point integers instead of only whole numbers
# In python 2 it's best to import division from the future version
# otherwise you can use float() or just multiply the number with a float, ex:
# 1/(2 * 1.0) = 0.5
