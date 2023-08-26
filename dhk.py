q=int(input('enter q:'))
a=int(input('enter a:'))
xa=int(input('enter private key of a:'))
xb=int(input('enter private key of b:'))
ya=pow(a,xa)%q
print(ya)
yb=pow(a,xb)%q
print(yb)
k1=pow(yb,xa)%q
k2=pow(ya,xb)%q
if k1==k2:
    print('keys exchanged successfully')
else:
    print("no")