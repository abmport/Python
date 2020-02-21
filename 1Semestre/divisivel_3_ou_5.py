n1=float(input("Descubra se o número é divisível por 3 ou 5: "))

por3=n1%3
por5=n1%5

if por3==0 and por5==0: print ("O número",n1,"é divisível por 3 e 5")
elif por3==0 and por5!=0: print ("O número",n1,"é divisível por 3")
elif por5==0 and por3!=0: print ("O número",n1,"é divisível por 5")
else: print ("O número",n1,"nao é divisível por 3 ou 5")

input()
