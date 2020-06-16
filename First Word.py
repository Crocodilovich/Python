'''
Дана строка и нужно найти ее первое слово.

При решении задачи обратите внимание на следующие моменты:
 - В строке могут встречатся точки и запятые
 - Строка может начинаться с буквы или, к примеру, с пробела или точки
 - В слове может быть апостроф и он является частью слова
 - Весь текст может быть представлен только одним словом и все
'''

string = 'greetings, friends'

def first_word(string):
    array = string.split()
    new_string = ''

    for element in array:
        if element[0].isalpha():
            for letter in element:
                if letter.isalpha() or letter == "'":
                    new_string += letter
                else:
                    return new_string
            return new_string

def first_word_version_one(text: str) -> str:

    text = text.replace(',', '')
    text = text.replace('.', ' ')

    li = text.split()

    return li[0]


print(first_word(string))

