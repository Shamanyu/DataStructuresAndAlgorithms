def brokerTime(peopleTickets, brokerIndex):

    timeTaken = 0
    while (peopleTickets[brokerIndex] > 1):
        #peopleTickets = list(filter(lambda x: x > 0, list(map(lambda x: x-1, peopleTickets))))
        flag = False
        for counter, peopleTicket in enumerate(peopleTickets):
            if peopleTicket > 0:
                if counter != brokerIndex:
                    flag = True
                peopleTickets[counter] -= 1
                timeTaken += 1
        if not flag:
            return timeTaken + peopleTickets[brokerIndex]
            # return False

    if (peopleTickets[brokerIndex] == 1):
        timeTaken += len(peopleTickets[0:brokerIndex+1])

    return timeTaken

print(brokerTime([2 , 3 , 5, 1, 2], 2))

# print(brokerTime([2 , 3 , 5, 1, 2], 2))
