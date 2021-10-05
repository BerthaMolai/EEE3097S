import rsa
import timeit

start = timeit.timeit()
print(start)

# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)


file1 = open("encrypted.txt","w")
file2 = open("decrypted.txt","w")
with open('plaintext.txt') as file:
    for line in file:
        for word in line.split():
            encMessage = rsa.encrypt(word.encode(),publicKey)
           # print("encrypted string: ", encMessage)
            #file1.write(encMessage)
            decMessage = rsa.decrypt(encMessage, privateKey).decode()
            file2.write(decMessage)


# this is the string that we will be encrypting
#message = "hello geeks"

# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method


#print("original string: ", message)
#rint("encrypted string: ", encMessage)

# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
#decMessage = rsa.decrypt(encMessage, privateKey).decode()

#print("decrypted string: ", decMessage)

end = timeit.timeit()
print(end)
timeComplexity = start-end
print(timeComplexity)
