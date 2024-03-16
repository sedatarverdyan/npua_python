import random
import numpy as np
class Matrix:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.arr = np.random.randint(1,100,size=(n,m))
    def print(self):
        print(self.arr)
    def mean(self):
        sum = 0
        for i in self.arr:
            for j in i:
                sum = sum + j
        print(sum)
    def sum(self, row):
        sum = 0
        for j in self.arr[row-1]:
            sum = sum +j
        print(sum)
    def column(self, col):
        sum = 0
        for i in self.arr:
            sum = sum + i[col-1]
        print(sum)
    def submatrix(self, col1, col2, row1, row2):
        
        for i in range(row1-1,row2):
            sub=[]
            for j in range(col1-1,col2):
                sub.append(self.arr[i][j])
            
            print(' '.join(map(str, sub))) 
            # print(sub)
            
                
    

        
matrix = Matrix(5,6)
matrix.print()
matrix.mean()
matrix.sum(4)
matrix.column(2)
matrix.submatrix(2, 5, 2, 4)
