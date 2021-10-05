import time
import compressionBlock as comp
import encryptionBlock as encrypt

file = input("Enter the filename to open:\n")

#start timer for compression 
start = time.time()
comp.openfile(file)

#filepath for encryption algorithm to open compressed file
outputFile = comp.compressFile()

print("now encrypting")
#encryption now takes place
encFile = encrypt.encrypt(outputFile)
end = time.time()

print("Time taken to compress and encyrpt: " +"{:.2f}".format(end - start) +"s" )

gFile = input("Would you like to access your now?\n")
#
if gFile == 'yes':
    #decryption here
    decFile = encrypt.decryption(encFile)
    if decFile  != None:
        comp.decompressFile(decFile)
    