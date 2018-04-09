# CodeArena

class CodeArena1(object):

	def __init__(self):
		self.set_input(0, list(), 0, list())

	def get_user_input(self):
		number_of_workers = int(input())
		speciality_list = list(input())
		number_of_orders = int(input())
		order_list = list()
		for counter in range(0, number_of_orders):
			order_list.append(list(input()))
		self.set_input(number_of_workers, speciality_list, number_of_orders, order_list)

	def set_input(self, number_of_workers, speciality_list, number_of_orders, order_list):
		self.number_of_workers = number_of_workers
		self.speciality_list = speciality_list
		self.number_of_orders = number_of_orders
		self.order_list = order_list

	def get_output(self):
		speciality_dictionary = dict()
		output = list()
		for speciality in self.speciality_list:
			if speciality in speciality_dictionary:
				speciality_dictionary[speciality] = speciality_dictionary[speciality] + 1
			else:
				speciality_dictionary[speciality] = 1
		for order in self.order_list:
			speciality1 = order[0]
			speciality2 = order[1]
			speciality3 = order[2]
			if (speciality1 in speciality_dictionary and speciality_dictionary[speciality1] > 0
				and speciality2 in speciality_dictionary and speciality_dictionary[speciality2] > 0
				and speciality3 in speciality_dictionary and speciality_dictionary[speciality3] > 0):
				output.append(speciality_dictionary[speciality1]*
					speciality_dictionary[speciality2]*speciality_dictionary[speciality3])
				speciality_dictionary[speciality1] -= 1
				speciality_dictionary[speciality2] -= 1
				speciality_dictionary[speciality3] -= 1
			else:
				output.append(0)
		return output


code_arena1 = CodeArena1()

code_arena1.get_user_input()
output_list = code_arena1.get_output()
for output in output_list:
	print (output)