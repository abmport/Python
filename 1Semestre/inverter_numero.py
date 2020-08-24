num = int(input("Escolha um número de três dígitos para o invertermos: "))
print("O número escolhido é: ",num)
          
p1=num%10
p2=num//10
p2=p2*11
p2=p2%10
p3=p1+p2*10
p3=num-p3
p3=p3//100
print("O número invertido é: ",p1,p2,p3)

input ()
