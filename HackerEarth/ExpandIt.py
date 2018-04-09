class Stack:
     def __init__(self):
         self.container = []  # You don't want to assign [] to self - when you do that, you're just assigning to a new local variable called `self`.  You want your stack to *have* a list, not *be* a list.

     def isEmpty(self):
         return self.size() == 0   # While there's nothing wrong with self.container == [], there is a builtin function for that purpose, so we may as well use it.  And while we're at it, it's often nice to use your own internal functions, so behavior is more consistent.

     def push(self, item):
         self.container.append(item)  # appending to the *container*, not the instance itself.

     def pop(self):
         return self.container.pop()  # pop from the container, this was fixed from the old version which was wrong

     def size(self):
         return len(self.container) 

def start_counting(counter):
	s = Stack()
	counter += 1
        while len(input_string) > counter and (ord(input_string[counter]) >= ord('0') and ord(input_string[counter]) <= ord('9')):
		s.push(int(input_string[counter]))
		counter += 1
        multiplier = 1
        result = 0
        while (not s.isEmpty()):
                result += multiplier*s.pop()
                multiplier *= 10
        counter -= 1
	return result, counter-1

input_string = raw_input('')
Q = int(raw_input(''))
alphabet_count = [0]*26
for counter in range(0, len(input_string)):
	if (input_string[counter] >= 'a' and input_string[counter] <= 'z'):
		temp = input_string[counter]
		count, counter = start_counting(counter)
		alphabet_count[ord(temp) - 97] += count
for counter1 in range(0, Q):
	K = int(raw_input(''))
	present = 0
	result = -1
	for counter in range(0, 26):
		if present+alphabet_count[counter] >= K:
			result = chr(ord('a')+counter)
			break
		else:
			present += alphabet_count[counter]
	print result

