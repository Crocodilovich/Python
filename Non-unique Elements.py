# возвращает не уникальные числа

def checkio_1(data):
    result = []
    for element in data:
        if data.count(element) > 1:
            result.append(element)
    return result

def checkio_2(data):
    return [i for i in data if data.count(i) > 1]

print(checkio_2([1, 1, 2, 3, 4, 5, 2]))