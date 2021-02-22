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
    xstr = str(bin(x))
    jlit = [0, 0, 0, 0, 0, 0]
    lit = [0, 0, 0, 0, 0, 0]
    for i in range(0, 31):
        if i == 0:
            lit[0] = x % 10
            x /= 10
        elif 1 <= i <= 8:
            lit[1] += (x % 10) * pow(10, jlit[1])
            x /= 10
            jlit[1] += 1
        elif 9 <= i <= 16:
            lit[2] += (x % 10) * pow(10, jlit[2])
            x /= 10
            jlit[2] += 1
        elif 17 <= i <= 28:
            lit[3] += (x % 10) * pow(10, jlit[3])
            x /= 10
            jlit[3] += 1
        elif 29 <= i <= 30:
            lit[4] += (x % 10) * pow(10, jlit[4])
            x /= 10
            jlit[4] += 1
        elif i == 31:
            lit[5] += (x % 10) * pow(10, jlit[5])
            x /= 10
            jlit[5] += 1
    # for i in range(0, 5):
        # print(bin(lit[i]))
        # print(bin(jlit[i]))
    print(lit)
    print(jlit)

f2(0x000007b)