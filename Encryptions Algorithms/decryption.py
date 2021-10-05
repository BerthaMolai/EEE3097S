import base64
import string
import timeit
#from  encryption import secret_key

start = timeit.timeit()
key=""
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

def decrption() :
    file2 = open("decrypted2.txt","w")
    with open('encrypted.txt.') as file:
        for line in file:
            decrypt= decode(key, line)
            file2.write(decrypt)
            #print(translated)

end = abs(timeit.timeit())
timeComplexity = start-end
key = input("Enter the private key.")
if key==secret_key :
   print(" Time Complexity of Algorithm for Decryption : " , timeComplexity)
   print("Scuccessfully Decrypted!")
else :
   print("Invalid Key, Cannot decrypt the data.")