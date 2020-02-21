import math
print ("Digite o lado do Hexagono: ")
lado = float(input())
p = lado*6
result = p*(math.pow(lado,2)*math.sqrt(3))/4

print ("Lado do hexagono:",lado,"metros,")
print ("Area:",result,"metros quadrados,")
print ("Perimetro: ",p,"metros.")

input()