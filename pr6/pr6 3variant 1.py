'''Вариант 3
1. В одномерном числовом массиве D длиной n вычислить сумму элементов с
нечетными индексами. Вывести на экран массив D, полученную сумму.'''

n = int(input('Введите длину массива - '))
a = []
s = 0
print('Заданная длина массива - ', n)
for i in range (n):
    print('Введите ',i,'элемент: ')
    a.append(int(input()))
print('Исходный массив - ', a)
for i in range(n):
    if i % 2 == 1:
        s = a[i] + s
print('Сумма элементов - ', s)