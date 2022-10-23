'''Вариант 3
2. Дана вещественная матрица размером n х m. Переставляя ее строки и
столбцы, добиться того, чтобы наибольший элемент (или один из них)
оказался в верхнем левом углу.'''

n = int(input('Введите кол-во строк в матрице - '))  
m = int(input('Введите кол-во столбцов в матрице - '))  
matrix = []  

print('Введите элементы матрицы - ')  

for i in range(n):     
   a =[]  
   for j in range(m):  
      a.append(int(input()))  
   matrix.append(a)  

for i in range(n):  
   for j in range(m):  
      print(matrix[i][j], end = " ")  
   print()  
print('Исходная матрица')
for row in matrix:
    print(*map('{:2d}'.format, row))
print()

print('Отсортированная матрица')
max_element = matrix[0][0]
ie = je = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
            ie = i 
            je = j 
matrix[0], matrix[ie] = matrix[ie], matrix[0]
matrix[0][0], matrix[0][je] = matrix[0][je], matrix[0][0]
for row in matrix:
    print(*map('{:2d}'.format, row))