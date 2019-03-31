"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

input_array = [random.randint(1,50) for _ in range(1,10)]
print('Crated new random array:')
print (input_array)

print('MIN and MAX search in progress...')
max =0
min = input_array[0]
max_pos = 0
min_pos = 0

for pos in range(0,len(input_array)):
    if input_array[pos]>max:
        max = input_array[pos]
        max_pos = pos

    if input_array[pos] < min:
        min = input_array[pos]
        min_pos = pos

print(f"Result: max is {max} found in pos {max_pos}, min is {min} found in {min_pos}.")

buf = input_array[max_pos]
input_array[max_pos] = input_array[min_pos]
input_array[min_pos]= buf

print('Revers array:')
print (input_array)







