'''
В этой миссии вы должны написать функцию, которая представит человека по переданным параметрам.

Входные данные: Два аргумента строка(str) и положительное число(int)
Выходные данные: Строка(str).
'''

def say_hi(name, age):
    return "Hi. My name is %s and I'm %s years old" % (name, age)

say_hi_alternative = lambda name, age: ("Hi. My name is %s and I'm %s years old" % (name, age))

a = 'text'
b = 123456789
c = f'{a}...{b}'
print(c)