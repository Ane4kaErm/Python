"""""
Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""""

a = input('Введите трехзначное число: ')

b = int(a[0])
c = int(a[1])
d = int(a[2])

print('Сумма цифр числа: ', b + c + d)