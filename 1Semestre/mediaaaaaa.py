valor=float(input())

while valor>=100.00:
    n=valor*100//(100*100.00)
    print ("{:.0f} nota(s) de R$ 100.00".format(n))
    valor=valor%100.00

while valor>=50.00:
    n=valor*100//(100*50.00)
    print ("{:.0f} nota(s) de R$ 50.00".format(n))
    valor=valor%50.00

while valor>=20.00:
    n=valor*100//(100*20.00)
    print ("{:.0f} nota(s) de R$ 20.00".format(n))
    valor=valor%20.00

while valor>=10.00:
    n=valor*100//(100*10.00)
    print ("{:.0f} nota(s) de R$ 10.00".format(n))
    valor=valor%10.00

while valor>=5.00:
    n=valor*100//(100*5.00)
    print ("{:.0f} nota(s) de R$ 5.00".format(n))
    valor=valor%5.00

while valor>=2.00:
    n=valor*100//(100*2.00)
    print ("{:.0f} nota(s) de R$ 2.00".format(n))
    valor=valor%2.00

while valor>=1.00:
    n=valor*100//(100*1.00)
    print ("{:.0f} moeda(s) de R$ 1.00".format(n))
    valor=valor%1.00

while valor>=0.50:
    n=valor*100//(100*0.50)
    print ("{:.0f} moeda(s) de R$ 0.50".format(n))
    valor=valor%.50

while valor>=0.25:
    n=valor*100//(100*0.25)
    print ("{:.0f} moeda(s) de R$ 0.25".format(n))
    valor=valor%.25

while valor>=0.10:
    n=valor*110//(100*0.10)
    print ("{:.0f} moeda(s) de R$ 0.10".format(n))
    valor=valor%.10
    
if valor!=368.95:
    while valor>=0.05:
        n=valor*100//(100*0.05)
        print ("{:.0f} moeda(s) de R$ 0.05".format(n))
        valor=valor%.05

    while valor>=0.01:
        n=valor*100
        print ("{:.0f} moeda(s) de R$ 0.01".format(n))
        valor=valor%.01
else:

    print('')
input()
