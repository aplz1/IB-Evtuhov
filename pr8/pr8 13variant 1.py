'''Вариант 13
1. Определить наименьший элемент каждой четной строки матрицы А[М, N].'''

N = int(input('Введите кол-во строк в матрице - '))  
M = int(input('Введите кол-во столбцов в матрице - '))  
A = []  

print('Введите элементы матрицы - ')  

for i in range(N):     
   a =[]  
   for j in range(M):  
      a.append(int(input()))  
   A.append(a)  

for i in range(N):  
   for j in range(M):  
      print(A[i][j], end = " ")  
   print()

print('Исходная матрица')
for row in A:
    print(*map('{:2d}'.format, row))
print()

print('Наименьшие элементы четных строк')
print(*map(min, A[::2]))