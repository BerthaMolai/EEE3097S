import base64
import string
import timeit
import random   
import string  
import secrets 

num = 20 # define the length of the string  
# define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  

#times the algorithm
start = timeit.timeit()
secret_key = "amtkx3CpQdINJhOP94OX"

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

file1 = open("encrypted.txt","w")
file2 = open("decrypted.txt","w")
with open('plaintext.txt') as file:
    for line in file:
        translated = encode(secret_key, line) 
        file1.write(translated)
        decrypt= decode(secret_key, translated)
        file2.write(decrypt)
         

end = timeit.timeit()
timeComplexity = start-end
print("Time Complexity of Algorithm to Encrypt the Data : " , timeComplexity)
print("Scuccessfully Encrypted!")
print("Decryption private key :", secret_key)