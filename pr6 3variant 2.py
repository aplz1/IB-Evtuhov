'''Вариант 3
2. Дан одномерный массив из 8 элементов. Заменить все элементы массива
меньшие 15 их удвоенными значениями. Вывести на экран монитора
преобразованный массив.'''

n = 8
a = []
for i in range(n):
    print('Введите ',i,'элемент: ')
    a.append(int(input()))
print('Исходный массив - ', a)
for i in range(n):
    if a[i] < 15:
        a[i] = a[i]*2
print('Преобразованный массив - ', a)