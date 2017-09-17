string1 = raw_input("Enter the first string:\n")
string2 = raw_input("Enter the second string:\n")
string1_sorted = ''.join(sorted(string1))
string2_sorted = ''.join(sorted(string2))
print string1_sorted == string2_sorted
