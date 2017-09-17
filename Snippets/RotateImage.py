import math

image_size = int(input(''))

image_array = [[0]*image_size]*image_size

def perform_exchanges(n, x, y):
    temp = image_array[x][y]
    image_array[x][y] = image_array[y][n-x]
    image_array[y][n-x] = image_array[n-x][n-y]
    image_array[n-x][n-y] = image_array[n-y][x]
    image_array[n-y][x] = temp

for x in range(0, image_size):
    image_array[x] = input('').split(' ')
   
for x_counter in range (0, int(image_size/2)):
    for y_counter in range(0, math.ceil(image_size/2)):
        perform_exchanges(image_size-1, x_counter, y_counter)

print (image_array)
