# this creates a variable of a string of raw string formats
# that can be passed an arugment with four variables
# b/c it's a raw string format, you can add any type of variable to be shown
formatter = "%r %r %r %r"

# Here we see fomatting where we send in 4 digit values
print formatter % (1, 2, 3, 4)
# here we send in strings
print formatter % ("one", "two", "three", "four")
# here we send in boolean values, where no quotes are needed
print formatter % (True, False, False, True)
# here we send in the formatter itself which is a string
print formatter % (formatter, formatter, formatter, formatter)
# Here we pass in four strings as variables and allow the formatting
# to show this in our code more elegantly and keep under the
# 80 character line limit
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    # This is the only one that in the console will print with double quotes
    # around it b/c it has a single ' in it already for didn't
    "But it didn't sing.",
    "So I said goodnight."
)
