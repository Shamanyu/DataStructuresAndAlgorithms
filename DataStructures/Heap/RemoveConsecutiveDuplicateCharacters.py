from heapq import heappush, heappop

data = str(input(''))

data_dictionary = dict()

heap = list()

for element in data:
	data_dictionary[element] = data_dictionary.get(element, 0) + 1

data_list = list()
for key in data_dictionary:
	data_list.append((key, data_dictionary[key]))

for element in data:
	heappush(heap, element)

print (heap)
