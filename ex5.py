name = 'Zed A. Shaw'
age = 35
height_in_inches = 74
cm_in_an_inch = 2.54
height_in_cm = height_in_inches * cm_in_an_inch
weight_in_lbs = 180
kg_in_lb = 0.453592
weight_in_kg = weight_in_lbs * kg_in_lb
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# % are called format characters
print "Let's talk about %s." % name
print "He's %d cm tall." % height_in_cm
print "He's %d kg heavy." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % ( age, height_in_cm, weight_in_kg, age + height_in_cm + weight_in_kg )
