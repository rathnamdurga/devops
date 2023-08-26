from math import gcd

p = int(input('enter prime1:'))
q =int(input('enter prime2:')) 
n = p * q
e = 2
phi = (p - 1) * (q - 1)

# Find a value of e that is coprime to phi
while e < phi and gcd(e, phi) != 1:
    e += 1

# Find a value of d using the extended Euclidean algorithm
k = 2
while ((k * phi) + 1) % e != 0:
    k += 1
d = int((1 + (k * phi)) / e)

# Prompt the user to enter the message to be encrypted
msg = int(input("Enter message: "))
c = pow(msg, e) % n
print("Encrypted data = ", c)

# Decrypt the message
m = pow(c, d) % n
print("Decrypted data: ", m)