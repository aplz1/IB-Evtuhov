'''Вариант 2
1. Дан одномерный массив, состоящий из N целочисленных элементов. Ввести
массив с клавиатуры. Найти минимальный элемент. Вывести индекс
минимального элемента на экран.'''

n = int(input('Введите длину массива - '))
x = []
y = []
print('Заданная длина массива - ', n)
for i in range(n):
    print('Введите ',i,'элемент: ')
    x.append(int(input()))
print(x)
print('Минимальный элемент в массива - ', min(x))
print('Индекс минимального элемента - ', x.index(min(x)))