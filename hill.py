import numpy as np

def MatrixInverse(K):
    det = int(np.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = np.delete(Dji, (j), axis=0)
            Dji = np.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv




def encrypt(pt_arr,key_arr,ct_matrix):
    ct=''
    ct_arr = np.multiply( key_arr, pt_arr)
    for i in range(n):
        for j in range(n):
            ct_matrix[i]+=ct_arr[i][j]
            ct_matrix[i]%=26
    for i in range(n):
        ct += chr(ct_matrix[i]+65)
    return ct


def decrypt(key_arr,ct_matrix):
    decrypt_text = ""
    key_inv = MatrixInverse(key_arr)
    encrypt_arr = np.array(ct_matrix)
    decrypt_arr = np.multiply( key_inv, encrypt_arr)
    decrypt_matrix=[0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            decrypt_matrix[i]+=decrypt_arr[i][j]
            decrypt_matrix[i]%=26
    for i in range(n):
        decrypt_text += chr(decrypt_matrix[i]+65)
    return decrypt_text

pt=input('Enter the plaintext in uppercase: ')
#ct = ""
n=len(pt)
key=input('Enter key in uppercase: ')
key_matrix = [[None for i in range(n)] for i in range(n)]
ct_matrix = [0 for i in range(n)]
pt_matrix = [ord(pt[i])-65 for i in range(n)]

k=0
for i in range(n):
    for j in range(n):
        key_matrix[i][j] = ord(key[k]) - 65
        k+=1
pt_arr = np.array(pt_matrix)
key_arr = np.array(key_matrix)
ct=encrypt(pt_arr,key_arr,ct_matrix)
print('Ciphertext is : ',ct)
decrypt_text= decrypt(key_arr,ct_matrix)
print("Decrypted ciphertext i.e. plaintext is: ",decrypt_text)