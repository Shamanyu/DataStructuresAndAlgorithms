import math
import random
from random import randint

butler_faces_count = int(input(''))
coordinate_pairs_count = int(input(''))

class MyRand(object):
    def __init__(self):
        self.last = None

    def __call__(self):
        r = random.randint(0, 50) - 25
        while r == self.last:
            r = random.randint(0, 50) - 25
        self.last = r
        return r

def formula1(butler_face, coordinate_pair):
    butler_face_deviation_sum = 0
    coordinate_pair_deviation_sum = 0
    for butler_face_deviation_counter in range(0, butler_faces_count):
        coordinate_pair_deviation_sum += deviation_table[butler_face_deviation_counter][coordinate_pair]
    for coordinate_pair_deviation_counter in range(0, coordinate_pairs_count):
        butler_face_deviation_sum += deviation_table[butler_face][coordinate_pair_deviation_counter]
    return (butler_face_deviation_sum/coordinate_pairs_count + coordinate_pair_deviation_sum/butler_faces_count)/2

def formula2(butler_face, coordinate_pair):
    golden_butler_face = math.floor(butler_faces_count/2)
    butler_face_deviation_sum = 0
    golden_butler_face_deviation_sum = 0
    for coordinate_pair_deviation_counter in range(0, coordinate_pairs_count):
        butler_face_deviation_sum += deviation_table[butler_face][coordinate_pair_deviation_counter]
        golden_butler_face_deviation_sum += deviation_table[golden_butler_face][coordinate_pair_deviation_counter]
    return butler_face_deviation_sum/coordinate_pairs_count - golden_butler_face_deviation_sum/coordinate_pairs_count + deviation_table[golden_butler_face][coordinate_pair]

def accuracy(formula):
    total_deviation = 0
    calculated_deviation_table = [[0 for i in range(0, coordinate_pairs_count)] for j in range(0, butler_faces_count)]
    for butler_face_deviation_counter in range(0, butler_faces_count):
        for coordinate_pair_deviation_counter in range(0, coordinate_pairs_count):
            deviation = formula(butler_face_deviation_counter, coordinate_pair_deviation_counter)
            correction = deviation - deviation_table[butler_face_deviation_counter][coordinate_pair_deviation_counter]
            if correction > 0:
                total_deviation += correction
            else:
                total_deviation -= correction 
            calculated_deviation_table[butler_face_deviation_counter][coordinate_pair_deviation_counter] = deviation
    return calculated_deviation_table, total_deviation/(butler_faces_count*coordinate_pairs_count)

def generate_list_random_numbers(list_size):
    random_list = list()
    for counter in range(0, list_size):
        random_list.append(randint())
    return random_list

randint = MyRand()
deviation_table = [[0 for i in range(0, coordinate_pairs_count)] for j in range(0, butler_faces_count)]

butler_faces_deviation_table = generate_list_random_numbers(butler_faces_count)
coordinate_pairs_deviation_table = generate_list_random_numbers(coordinate_pairs_count)

for butler_face_deviation_counter in range(0, butler_faces_count):
    for coordinate_pair_deviation_counter in range(0, coordinate_pairs_count):
        deviation_table[butler_face_deviation_counter][coordinate_pair_deviation_counter] = \
          butler_faces_deviation_table[butler_face_deviation_counter] + \
          coordinate_pairs_deviation_table[coordinate_pair_deviation_counter]

formula1_calculated_deviation_table, formula1_deviation = accuracy(formula1)
formula2_calculated_deviation_table, formula2_deviation = accuracy(formula2)

#print ("Butler face table is ", butler_faces_deviation_table)
#print ("Coordinate pair table is ", coordinate_pairs_deviation_table)
#print ("Actual deviation table is ", deviation_table)
#print ("Calculated deviation table 1 is ", formula1_calculated_deviation_table)
print("Calculated deviation 1 is ", formula1_deviation)
#print ("Calculated deviation table 2 is ", formula2_calculated_deviation_table)
print("Calculated deviation 2 is ", formula2_deviation)
