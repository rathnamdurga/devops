from math import gcd
p=int(input('enter prime1:'))
q=int(input('enter prime2:'))
n=p*q
e=2
phi=(p-1)*(q-1)
while e<phi and gcd(e,phi)!=1:
    e+=1
k=2
while((k*phi)+1)%e!=0:
    k+=1
d=int((1+(k*phi))/e)
msg=int(input('enter msg:'))
c=pow(msg,e)%n
print(c)
m=pow(c,d)%n
print(m)

