def calc(salary):
    b1 = salary * 0.07
    b2 = salary * 0.15
    if salary > 2000:
        salary += b1
    else:
        salary += b2
    return print('Your salary is {:.3f}'.format(salary))


salary = float(input('Enter your salary: '))

calc(salary)
