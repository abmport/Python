def intercala(tup1, tup2):
    tup3 = ()

    for i in range(len(tup1)):
        tup3 += (tup1[i],) + (tup2[i],)
    return tup3
