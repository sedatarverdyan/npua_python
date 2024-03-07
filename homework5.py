# 1
import random
import numpy as np
def generate_random_matrix(rows, cols):
    arr = np.random.randint(1, 100, size=(rows, cols))
    print(arr)
    
i,j=map(int,input('Give me 2 numbers ').split())
generate_random_matrix(i,j)
A = [[77, 22, 49, 79, 38, 75],
 [57, 18,  2, 85, 35, 43],
 [ 4, 99, 11, 35, 93, 33],
 [88, 90, 25, 84, 36, 52]]

# 2
import random
import numpy as np
A =np.random.randint(1, 100, size=(5, 6))
print(A)
def get_column_sum(matrix,col):
    sum = 0
    
    for row in matrix:
        if col<len(row):
            sum = sum + row[col]
    return sum
column = int(input('give me column less than 6 '))
print(get_column_sum(A,column))

# 3
import random
import numpy as np
A = np.random.randint(1, 100, size=(5, 6))
print(A)
def get_row_average(matrix, row):
    sum =0
    print(matrix[row])
    for i in matrix[row]:
        sum = sum + i
        average = sum /len(matrix[row])
    return average, sum
rows = int(input('give me row less than 5 '))
print(get_row_average(A, rows))