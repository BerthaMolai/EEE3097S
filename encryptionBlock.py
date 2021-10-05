"""decyrption commented out"""
import base64
import string
import timeit
import random   
import string  
import secrets 
import gzip

num = 20 # define the length of the string  
# define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  

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

def encrypt(filepath):

    #times the algorithm
    start = timeit.timeit()
	#open with Gzipreader?
    global fille2
    file1 = gzip.open("encrypted.gzip",mode = "wt")
    #fille2 = gzip.open("decrypted.gzip",mode = "wt")
    with gzip.open(filepath, mode='rt') as file:
    		for line in file:
        		translated = encode(secret_key, line) 
                #decrypt = decode(secret_key, translated)
                #dcpt = bytes(decrypt, encoding = 'utf-8')
        		file1.write(translated)
                #fille2.write(dcpt)

    end = abs(timeit.timeit())
    #timeComplexity = start-end
    #print("Time Complexity of Algorithm to Encrypt the Data : " , timeComplexity)
    print("Successfully Encrypted!")
    print("Decryption private key :", secret_key)

    return "encrypted.gzip"

def decryption(encryptedFile) :

    key = input("Enter the private key: \n")
    if key==secret_key :
    #print(" Time Complexity of Algorithm for Decryption : " , timeComplexity)
        """file2 = gzip.open("decrypted.gzip",mode="wt")
        with gzip.open(encryptedFile, mode='rt') as file:
            for line in file:
                decrypt= decode(key, line)
                file2.write(decrypt)
                #print(translated)
        print("Successfully Decrypted!")"""
        return "decrypted.gzip"

    else :
        print("Invalid Key, Cannot decrypt the data.")
        return None