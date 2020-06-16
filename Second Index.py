string_one = 'hi'
string_two = ' '

def second_index(string_one, string_two):
    index_one = string_one.find(string_two)
    if index_one == -1:
        return None
    else:
        index_two = string_one.find(string_two, index_one + 1)
        if index_two == -1:
            return None
        else:
            return index_two

print(second_index(string_one, string_two))

def second_index_(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    index_symbol = []
    for (index, letter) in list(enumerate(text)):
        if letter == symbol:
            index_symbol.append(index)

    if len(index_symbol) > 1:
        return index_symbol[1]

    else:
        return None

def second_index__(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    res = [i for i in range(len(text)) if text[i] == symbol]
    return res[1] if len(res) > 1 else None