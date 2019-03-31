"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

import random

the_matrix = [[int(input(f"Введите число для {x}:{y}  матрицы: ")) for x in range(4)] for y in range(4)]


print('New matrix was created:')
for line in the_matrix:
    print(line)

for line in the_matrix:
    sum =0
    for num_in_line in line:
        sum = sum+num_in_line
    line.append(sum)

print('Result matrix:')
for line in the_matrix:
    print(line)



