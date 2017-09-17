string=raw_input('Enter the string:\n')
alphabet_count=[0]*127
flag=True
for alphabet in string:
	if alphabet_count[ord(alphabet)]==0:
		alphabet_count[ord(alphabet)]+=1
	else:
		flag=False
		break
if(not(flag)):
	print('The string has duplicate characters')
else:
	print('The string has only unique characters')
