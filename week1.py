def encrypt( text,s):
    result=""
    for i in range(0,len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+s-65) % 26 + 65)
        elif(char.islower()):
            result+=chr((ord(char)+s-97 )% 26 + 97)
    return result
text=input("enter a string" )
s=int(input("enter shift" ))
print(encrypt(text,s))


        
