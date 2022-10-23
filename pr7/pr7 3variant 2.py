'''Вариант 3
2. Преобразовать строку так, чтобы буквы каждого слова в ней были
отсортированы по алфавиту.'''

n = input("Впишите строку из слов - ").lower().split(' ')
def sort(n):
    for i in range(len(n)):
        n[i] = ''.join(sorted(n[i]))
    return(sorted(n))
print(sort(n))