#считывание матрицы из файла
with open('/repriritory/IB-Evtuhov/pr9/test1.txt', 'r', encoding='utf-8-sig') as f:
	line = f.readlines()
	matrix = [element.replace("\n", "").split() for element in line]
n = len(matrix)
m = len(matrix[0])
a = matrix
for i in range(n):  
   for j in range(m):  
      print(a[i][j], end = " ")  
   print()  


'''Вариант 3
1. Определить, является ли заданная целая квадратная матрица n-го
порядка симметричной (относительно главной диагонали).'''

z=('')
for i in range(0, n-1):
    for j in range(i+1, n):
        if a[i][j] != a[j][i]:
            z=('False')
            break
if z != ('False'):
    print('Матрица симметрична')
else:
    print('Матрица несимметрична')


'''Вариант 3
2. Дана вещественная матрица размером n х m. Переставляя ее строки и
столбцы, добиться того, чтобы наибольший элемент (или один из них)
оказался в верхнем левом углу.'''

print('Отсортированная матрица')
max_element = a[0][0]
ie = je = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] > max_element:
            max_element = a[i][j]
            ie = i 
            je = j 
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for i in range(n):  
   for j in range(m):  
      print(a[i][j], end = " ")  
   print()  