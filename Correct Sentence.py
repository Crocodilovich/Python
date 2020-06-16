'''
На вход Вашей функции будет передано одно предложение.
Необходимо вернуть его исправленную копию так,
чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.

Обратите внимание на то, что не все исправления необходимы.
Если предложение уже заканчивается на точку, то добавлять еще одну не нужно,
это будет ошибкой

Входные аргументы: Строка (A string).
Выходные аргументы: Строка (A string).
'''

def correct_sentence_1(string):
    string = list(string)
    if string[0].islower():
        string[0] = string[0].title()

    if string[-1] != '.':
        string.append('.')

    new_string = ''
    for letter in string:
        new_string +=letter
    return new_string

def correct_sentence_2(string):
    if string[-1] != '.':
        return string[0].upper() + string[1:] + '.'
    else:
        return string[0].upper() + string[1:]

def correct_sentence_best(text: str) -> str:

    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """

    # your code here

    text = text[0].upper() + text[1:]

    if "." != text[-1]:
        text += "."
    return text
