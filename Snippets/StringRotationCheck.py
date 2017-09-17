string1 = input('')
string2 = input('')

if len(string1) != len(string2):
    result = False
else:
    string1 = string1 + string1
    if string2 in string1:
        result = True
    else:
        result = False

print (result)
