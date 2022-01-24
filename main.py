
# Урок 1

# Задание 1
a = 12
b = 21
print(f"a={a}, b={b}")
a, b = b, a
print(f"a={a}, b={b}")

name = input("What's your name? ")
age = input("How old are you? ")
print(f"Your name is {name} and you are {age} years old.")
#

# Задание 2
seconds = int(input("Введите время в секундах: "))

minutes = seconds // 60
seconds = seconds % 60

hours = minutes // 60
minutes = minutes % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
#

# Задание 3
n = int(input("Введите число: "))
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))
print(f"Сумма: {n + nn + nnn}")
#

# Задание 4
n = int(input("Введите число: "))
max_digit = -1
while n % 10 != 0:
    if n % 10 > max_digit:
        max_digit = n % 10
    n = n//10

if n > max_digit:
    max_digit = n

print(f"Самая большая цифра в числе: {max_digit}")
#

# Задание 5
proceeds = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

if proceeds > costs:
    print(f"Прибыль: {proceeds - costs}")
else:
    print(f"Убыток: {proceeds - costs}")
#

# Задание 6
proceeds = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

if proceeds > costs:
    print(f"Прибыль: {proceeds - costs}")
    print(f"Рентабельность выручки: {(proceeds - costs)/proceeds}")
    employee_amount = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {(proceeds - costs)/employee_amount}")
else:
    print(f"Убыток: {proceeds - costs}")
#

# Задание 7
a = int(input("Введите a: "))
b = int(input("Введите b: "))
n = 1
while a < b:
    n += 1
    a *= 1.1

print(n)
#



