def fat(num):
    c = num
    f = 1
    print('calculando {}! = '.format(num), end="")
    while c > 0:
        print('{}'.format(c), end='')
        print(' X 'if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    print('{}'.format(f))


num = int(input())
fat(num)
