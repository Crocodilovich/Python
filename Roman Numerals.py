# проброзование целового числа в римскую системе счета

# 1 вариант
def checkio_1(data):
    ROMANS = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))

    roman_numeral = ""
    for roman, value in ROMANS:
        while data >= value:
            data -= value
            roman_numeral += roman

    return roman_numeral

# 2 вариант
def checkio_2(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result

# функция zip
a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b,)))





