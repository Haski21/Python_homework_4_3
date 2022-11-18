""" 
Написать программу, которая расшифрует строку,
используя набор букв из модуля string(string.ascii_lowercase),
Каждая символ - это две цифры.
Отчет с 00 -> 'a' и до 25 -> 'z', 26 - это пробел, он не входит в набор букв
Вход: строка из цифр. Выход: Текст.
Проверка работы функции выполняется через вторую строку.
"""
import string as line


str_code = '070411111426152419071413'
str = input('Enter string: ') # для общего случая

if len(str) % 2 != 0 or len(str) == 0: # проверка для общего случая
    print('Bad string')
else:
    var = 0
    for n in range(len(str_code) - len(str_code) // 2):
        foo = str_code[int(var)] + str_code[int(var) + 1]
        print(end = ' ') if foo == '26' else print(line.ascii_lowercase[int(foo)], end = '')
        var += 2
    