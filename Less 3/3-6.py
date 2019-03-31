"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

input_array = [random.randint(1,20) for _ in range(1,15)]
print('Новый массив отрицательных цисел создан:')
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

sum=0
if max_pos>min_pos:
    for a in range(min_pos+1, max_pos):
        print ('In range num for sum use : ', input_array[a])
        sum = sum + input_array[a]
    print('Total Sum is: ', sum)
elif max_pos<min_pos:
    for a in range(max_pos+1, min_pos):
        print('n range num for sum use: ', input_array[a])
        sum = sum + input_array[a]
    print('Total sum is: ', sum)








