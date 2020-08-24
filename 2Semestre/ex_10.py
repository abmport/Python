import random

list = []
for i in range(10):
    list.append(random.randint(1, 6))

for i in range(1, 6):
    print("Número {} foi sorteado {} vezes".format(i, list.count(i)))
