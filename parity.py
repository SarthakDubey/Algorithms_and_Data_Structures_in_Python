def parity(x):
    result = 0
    while x:
        #print (x)
        result ^= x & 1
        x >>= 1
    return result


print(parity(11))


def parity_1(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


print(parity_1(11))
