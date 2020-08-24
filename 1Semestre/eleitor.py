eleitor = int(input())

if eleitor>=18 and eleitor<=65: print ("eleitor obrigatorio")
elif eleitor>65 or eleitor<=18 and eleitor>16: print ("eleitor facultativo")
else: print ("nao eleitor")
input ()
