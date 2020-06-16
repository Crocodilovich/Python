def friendly_number(number, base=1000, decimals=0, suffix='', powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    import math
    k = 0
    i = 0
    powers_k = ''
    if decimals == 0:
        if number > 0:
            while abs(number) >= base and k < len(powers) - 1:
                number //= base
                number = math.floor(number)
                k += 1
            try:
                powers_k = powers[k]
            except IndexError:
                powers_k = powers[len(powers) - 1]
            return str(number) + powers_k + suffix
        else:
            while abs(number) > base:
                number /= base
                number = math.ceil(number)
                k += 1
            return str(number) + powers[k] + suffix
    elif number < base and  number >= 0:
        if decimals == 0:
            return str(number) + powers[0] + suffix
        else:
            return str(number) + '.' + '0' * decimals + suffix
    else:
        while abs(number) > base:
            number /= base
            number = round(number, decimals)
            print(number)
            k += 1
            i = len(str(round(number)) + '0' * decimals + '0')
            try:
                powers_k = powers[k]
            except IndexError:
                powers_k = powers[len(powers)-1]
        return str(number).ljust(i, '0') + powers_k + suffix
a = 100000000000000000000000000000000
base = 1000
print(friendly_number(42, powers=["u","d"], suffix="-n"))

#print('12345'.ljust(10, '0'))
#IndexError: list index out of range
powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
ass = []

for i, power in enumerate(powers):
    ass.append([i, power])
print(ass)
print(ass[0])
print(ass[1][1])

a = 1, 2, 3, 4, 5, 6
a = tuple(a)
print(a)

# пример

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    if number == 0:
        return "{0:.{1}f}".format(number, decimals) + suffix
    for i, power in enumerate(powers):
        operate = number / base ** i
        if 0 < abs(operate) < base or power == powers[-1]:
            number = round(operate, decimals) if decimals > 0 else int(operate)
            return "{0:.{1}f}".format(number, decimals) + power + suffix






