def strtoint(x):
    return {
        '-': -1,
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }[x]

def convert_strtoint(mystring):
    answer = 0
    for s in mystring:
        answer = -answer if s == '-' else answer*10 + strtoint(s)
    return answer

def convert_inttostr(x):
    is_negative = False
    if x < 0:
        is_negative = True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    return ('-' if is_negative else '') + ''.join(reversed(s))


def main():
    demostring = '00012378005623358720'
    print(convert_strtoint(demostring))
    demonumber = 12378614936542
    print(convert_inttostr(demonumber))

if __name__ == '__main__':
    main()