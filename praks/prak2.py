def f1(x):
    if x[3] == 1986:
        if x[4] == 'muf':
            if x[2] == 'idl':
                return 0
            elif x[2] == 'clean':
                return 1
            elif x[2] == 'jflex':
                if x[1] == 'nsis':
                    return 2
                elif x[1] == 'sqlpl':
                    return 3
                elif x[1] == 'cirru':
                    return 4
        elif x[4] == 'golo':
            if x[0] == 2000:
                if x[1] == 'nsis':
                    return 5
                elif x[1] == 'sqlpl':
                    return 6
                elif x[1] == 'cirru':
                    return 7
            elif x[0] == 1987:
                return 8
            elif x[0] == 1980:
                return 9
        elif x[4] == 'boo':
            return 10
    elif x[3] == 1972:
        return 11
    elif x[3] == 2018:
        return 12


print(f1([1980, 'nsis', 'jflex', 1986, 'golo']))
print(f1([1987, 'nsis', 'clean', 1986, 'muf']))


def f2(x):
    a = x & 0b00000000000000000000000000000001
    b = x & 0b00000000000000000000000111111110
    c = x & 0b00000000000000011111111000000000
    d = x & 0b00011111111111100000000000000000
    e = x & 0b01100000000000000000000000000000
    f = x & 0b10000000000000000000000000000000
    a <<= 29
    b >>= 1
    c >>= 1
    e <<= 1
    f >>= 15
    xstr = a | b | c | d | e | f
    return xstr


print(hex(f2(0x4562240c)))
print(hex(f2(0x8f6903fd)))


