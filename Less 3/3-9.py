"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

the_matrix = [[(random.randint(1,9)) for x in range(5)] for y in range(5)]

for line in the_matrix:
    print(line)


matrix_max=0
for y in range(0,len(line)):
    # print(f"Column: {y} :")
    min_in_column = the_matrix[0][y]
    for x in range(0,(len(the_matrix))):
        if min_in_column>the_matrix[x][y]:
            min_in_column=the_matrix[x][y]
        #print(the_matrix[x][y])
    print(f"min : {min_in_column} in column: {y}")
    if min_in_column>matrix_max:
        matrix_max=min_in_column
print('Max in minimum num in matrix: ', matrix_max)































