"""
2. Во втором массиве сохранить индексы четных элементов первого массива. Например,
если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""


for pos in range(0,len(input_array)):
    if input_array[pos] % 2 ==0:
        print(f"{input_array[pos]} / 2 is even number. Add in output array")
        output_array.append(pos)

print('Index of even nums in input array found:')
print(output_array)






