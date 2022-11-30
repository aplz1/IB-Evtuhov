#Вариант 3, блок а
'''Вывести число в обратном порядке'''

n = int(input("Введите число: ")) 
rever_n = 0    

def reverse(n): 
	global rever_n   
	if (n > 0): 
		a = n % 10 
		rever_n = (rever_n * 10) + a 
		reverse(n // 10) 
	return rever_n 

rever_n = reverse(n) 
print("Число в обратном порядке: %d" % rever_n)


#Вариант 3, блок б
'''Дана последовательность натуральных чисел (одно число в строке),
завершающаяся числом 0. Выведите первое, третье, пятое и т.д. из
введенных чисел. Завершающий ноль выводить не надо.'''

#все числа в одной строке
def func():
    a = [int(i) for i in input("Введите последовательность натуральных чисел: ").split() if int(i)]
    print(*a[::2])
func()


#одно число в строке
print("Введите последовательность натуральных чисел: ")
def nat_numbers():
    a = int(input())
    if a > 0: 
        if a % 2:
            print('--->',a)
            nat_numbers()
        else:
            nat_numbers()

nat_numbers()