string1 = input()
string2 = input()

if string1 == string2[(len(string2)-2):] +  string2[:(len(string2)-2)]:
	print ("Positive")
elif string2 == string1[(len(string1)-2):] +  string1[:(len(string1)-2)]:
	print ("Positive")
else:
	print ("Negative")
