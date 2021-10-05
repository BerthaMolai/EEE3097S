import base64
import string
import timeit

start = timeit.timeit()
secret_key = "786793Acgyhgfhk"

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
        # print encodedmsg 

end = timeit.timeit()
timeComplexity = start-end
print(" Time Complexity of Algorithm to Encrypt the Data : " , timeComplexity)
print("Scuccessfully Encrypted!")