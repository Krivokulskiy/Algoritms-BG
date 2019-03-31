"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

input_array = [random.randint(1,50) for _ in range(1,10)]
print('Crated new random array:')
print (input_array)

print('first MIN  search in progress...')
min = input_array[0]
min_first_pos = 0

for pos in range(0,len(input_array)):

    if input_array[pos] < min:
        min = input_array[pos]
        min_first_pos = pos

print(f"Result: first min is {min} found in {min_first_pos}.")

print('second MIN  search in progress...')

min = input_array[0]
min_second_pos = 0

for pos in range(0,len(input_array)):

    if input_array[pos] < min and pos !=min_first_pos:
        min = input_array[pos]
        min_second_pos = pos

print(f"Result: second min is {min} found in {min_second_pos}.")




