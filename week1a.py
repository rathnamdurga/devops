def decrypt(text,a):
    result=""
    for i in range(0,len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+a-65) % 26 + 65)
        elif(char.islower()):
            result+=chr((ord(char)+a-97 )% 26 + 97)
    return result
text=input("enter a string: ")
s=int(input("Enter shift: "))
a=26-s
print(decrypt(text,a))