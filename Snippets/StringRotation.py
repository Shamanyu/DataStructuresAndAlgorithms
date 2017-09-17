string1 = raw_input("Enter the first string: ")
string2 = raw_input("Enter the second string: ")
string_concatenated = string1+string1
if(string_concatenated.find(string2)) != -1 and len(string1) == len(string2):
	print "Yes! Yes! yes! OMG, I can't believe it!!!!!"
else:
	print "Nope!"
