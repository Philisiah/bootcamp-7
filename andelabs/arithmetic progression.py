def arith_geo(x):
    if len(x) != 0:
        y = []
        z = []
        for i in range(len(x) - 1):
            if x[i + 1] == 0 or x[i] == 0:
                y.append(0)
            else:
                y.append( x[i + 1] / float(x[i]))
            z.append( x[i + 1] - x[i])
        y = set(y)
        z = set(z)
        if len(y) == 1:
            return 'Geometric'
        elif len(z) == 1:
            return 'Arithmetic'
        else:
            return -1
    return 0