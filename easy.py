﻿_author__ = 'Ершков Александр Вячеславович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

a = int(input ('введите число'))
while a > 0:
    print (a%10)
    a//=10

a = input ('введите число')
for i in a:
 print (i)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
#решение 1
a = input('a=')
b = input('b=')
c = a
a = b
b = c
print (a)
print (b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

a = int(input('укажите ваш возраст: '))
while a >= 18:
    print ('доступ разрешён')
    break
print('Извините, пользование данным ресурсом только с 18 лет')





