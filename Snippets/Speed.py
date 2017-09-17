test_cases_count = int(input(''))
max_speed = 1000000000+1

def userInput():
    car_count = int(input(''))
    car_speeds = input('').split(' ')
    car_speeds = car_speeds[0:car_count]
    return car_count, car_speeds

def carsAtMaxSpeed(car_count, car_speeds):
    global max_speed
    result = 0
    for car_speed in car_speeds:
        car_speed = int(car_speed)
        if car_speed < max_speed:
            max_speed = car_speed
            result += 1
    return result

for counter in range(0, test_cases_count):
    max_speed = 1000000000+1
    car_count, car_speeds = userInput()
    result = carsAtMaxSpeed(car_count, car_speeds)
    print (result)
