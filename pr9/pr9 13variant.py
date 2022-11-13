#считывание матрицы из файла
with open('/repriritory/IB-Evtuhov/pr9/test2.txt', 'r', encoding='utf-8-sig') as f:
	line = f.readlines()
	matrix = [element.replace("\n", "").split() for element in line]
n = len(matrix)
m = len(matrix[0])
a = matrix
for i in range(n):  
   for j in range(m):  
      print(a[i][j], end = " ")  
   print()  


'''Вариант 13
1. Определить наименьший элемент каждой четной строки матрицы А[М, N].'''

print('наименьший элемент каждой четной строки матрицы')
print(*map(min, a[::2]))


'''Вариант 13
2. Найти наибольший и наименьший элементы прямоугольной матрицы и поменять их местами.'''

print('Отсортированная матрица')
for i, row in enumerate(a):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
for row in a:
    print(row)
with open('/repriritory/IB-Evtuhov/pr9/otvet2.txt', 'w') as file:
    file.write('12, 23 \n')
    for x in a:
        file.write(' '.join(map(str,x)) + '\n')