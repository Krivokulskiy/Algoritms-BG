"""
4. Определить, какое число в массиве встречается чаще всего.

"""

import random

input_array = [random.randint(1,10) for _ in range(1,15)]
print('Новый массив создан:')
print (input_array)

max_count=0
out_array=[]

for a in input_array:
    print(f" {a} встречается в массиве {input_array.count(a)} раз")
    if max_count<input_array.count(a):
        max_count=input_array.count(a)

for a in input_array:
    if input_array.count(a)== max_count:
        if a not in out_array:
            out_array.append(a)

print(f"{out_array} c максимальным значением {max_count}")




















