name = 'Shubham Shamanyu'
age = 21
height = 68
height_in_cms = height * 2.54
weight = 176
weight_in_kgs = weight/2.2
eyes = 'brown'
teeth = 'white'
hair = 'black'

print "let's talk about %s." %name
print "he's %d inches tall." %height_in_cms
print "He's %d pounds heavy." %weight_in_kgs
print "Actually that's not too heavy."
print "he's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (age, height_in_cms, weight_in_kgs, age + height + weight)
