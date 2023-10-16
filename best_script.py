# для установки библиотеки нужно в cmd прописать pip install numpy
import numpy as np 
MatA = np.array([[1,2,3,2], # Первая матрица, cюда записывай свою матрицу. Также можно записывать в строчку, но для удобства и понимания лучше записывать как я
                [2,2,3,4],
                [1,-1,0,0],
                [-1,6,4,4]],dtype=np.float32)
MatB = np.array([[6,2,3,2], # Вторая матрица, для умножения, решения системы линейных уравнений
                [3,4,1,3],
                [1,2,-1,0],
                [5,0,4,6]],dtype=np.float32)
#Возведение матрицы в степень 
n = 2 # Вместо "2" укажи степень, в которую надо возвести
print("Matrix in", n, "power:\n", np.linalg.matrix_power(MatA,n))

#Ранг матрицы
print("Rank of Matrix:", np.linalg.matrix_rank(MatA))

#Определитель матрицы (Считает определитель только квадратных матрицы)
print("Det of Matrix:", np.linalg.det(MatA)) # Det != 0, Матрица невырожденная => есть обратная матрица

#Транспонированная матрица:
print("Transposed matrix:\n", np.transpose(MatA))

#Обратная матрица:  
print("Inverse matrix:\n", np.linalg.inv(MatA))

#Умножение двух матриц:
print("Result of Multiplication:\n", np.dot(MatA,MatB))

#Решение системы линейных алгебраических уравнений вида Ax = B:
print("Solution of the system of equations:\n", np.linalg.solve(MatA, MatB))