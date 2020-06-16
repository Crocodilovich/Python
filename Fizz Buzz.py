'''
"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.

Входные данные: Число, как целочисленное (int).
Выходные данные: Ответ, как строка (str).
'''

def checkio(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)

def checkio_best_one(n):
    return 'Fizz' * (not n % 3) + ' ' * (not n % 15) + 'Buzz' * (not n % 5) or str(n)