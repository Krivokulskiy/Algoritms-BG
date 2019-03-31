"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

"""

import random

input_array = [random.randint(-15,-1) for _ in range(1,15)]
print('Новый массив отрицательных цисел создан:')
print (input_array)
find=input_array[0]
pos=0

for a in range(0,len(input_array)):
    if input_array[a]>find:
        find=input_array[a]
        pos=a
print(f" минимальный отрицательный элемент: {find} в позиции {pos}")




