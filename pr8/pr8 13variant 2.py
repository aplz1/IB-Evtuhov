'''Вариант 13
2. Найти наибольший и наименьший элементы прямоугольной матрицы и поменять их местами.'''

import random

n = int(input('Введите кол-во строк в матрице - '))
m = int(input('Введите кол-во столбцов в матрице - '))
matrix = [[random.randrange(100) for i in range(m)] for j in range(n)]

print('Исходная матрица')
for i in range(n):
    print(matrix[i])

print('Отсортированная матрица')
for i, row in enumerate(matrix):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]

for row in matrix:
    print(*map('{:2d}'.format, row))