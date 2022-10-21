'''Вариант 3
1. Определить, является ли заданная целая квадратная матрица n-го
порядка симметричной (относительно главной диагонали).'''

n=int(input('Введите кол-во строк и столбцов в матрице - '))
a=[]
z=('')
for i in range(n):
    b=[]
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
for i in range(0, n-1):
    for j in range(i+1, n):
        if a[i][j] != a[j][i]:
            z=('False')
            break
if z != ('False'):
    print('Матрица симметрична')
else:
    print('Матрица несимметрична')