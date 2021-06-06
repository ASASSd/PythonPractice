def f23(x):
    outx = []
    j=0
    for i in range(len(x)):
        if x[i] != [None, None]:
            x[i][1] = x[i][1].split('#')
            x[i][0] = str(round(float(x[i][0]), 1))
            outx.append([str(x[i][0]), x[i][1][1], x[i][1][0]])
            date = outx[j][1].split('‐')
            date_str = date[2] + '/' + date[1] + '/' + date[0]
            outx[j][1] = date_str
            outx[j][2] = outx[j][2][6:16]
            j += 1
    return outx