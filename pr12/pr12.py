#Вариант 3, блок а
'''Вывести число в обратном порядке (через int)'''

def rever_num(n): 
	global rever_n   
	if (n > 0): 
        # находим остаток - последнюю цифру
		a = n % 10 
        # увеличиваем разрядность числа
		rever_n = (rever_n * 10) + a 
        # делим нацело - удаляем последнюю цифру
		rever_num(n // 10) 
	return rever_n 

rever_n = 0   
n = int(input("Введите число: ")) 
rever_n = rever_num(n) 
print("Число в обратном порядке: %d" % rever_n)



#Вариант 3, блок а
'''Вывести число в обратном порядке (через строки)'''

def reverse(n):
    if len(n) != 0:
        return reverse(n[1:]) + n[0]
    else:
        return(n)

n = input("Введите число: ")
print("Число в обратном порядке: %s" % reverse(n))



#Вариант 1, блок б
'''Вводим последовательность натуральных чисел (одно число в строке),
завершающаяся числом 0. Определите наибольшее значение числа в этой
последовательности. В этой задаче нельзя использовать глобальные
переменные и передавать какие-либо параметры в рекурсивную функцию.
Функция получает данные, считывая их с клавиатуры. Функция
возвращает единственное значение: максимум считанной
последовательности. Гарантируется, что последовательность содержит
хотя бы одно число (кроме нуля).'''

def func():
    n = int(input())
    if n != 0:
        return max(n, func())
    else: 
        return 0

print("Наибольшее значение в последовательности: %d" % func())