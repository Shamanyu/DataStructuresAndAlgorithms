def handleCustomer():
    if (len(food_pile)>0):
        output_array.insert(len(output_array), food_pile[0])
        del food_pile[0]
    else:
        output_array.insert(len(output_array), "No Food")

def handleChef(cost):
    food_pile.insert(0, cost)

query_count = int(input(''))
food_pile = list()
output_array = list()

for counter in range(0, query_count):
    query = input('')
    if query == '1':
        handleCustomer()
    else:
        query_type, cost = query.split(' ')
        handleChef(int(cost))

for counter in range (0, len(output_array)):
    print (output_array[counter])
