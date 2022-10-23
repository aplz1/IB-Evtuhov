'''Вариант 2
2. Пользователь вводит две стороны трех прямоугольников. Вывести их площади.'''

def s(a1, a2, a3, b1, b2, b3):
     s1 = (a1 * b1) 
     s2 = (a2 * b2)
     s3 = (a3 * b3) 
     return(s1, s2, s3)

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())

print(s(a1, a2, a3, b1, b2, b3))