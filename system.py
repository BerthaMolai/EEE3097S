import time
import compression as comp

file = input("Enter the filename to open.")

#start timer for compression 
start = time.time()
comp.openfile(file)
comp.compressFile()

print("now encrypting")
#encryption now takes place
end = time.time()

gFile = input("Would you like to access your now?\n")
#
if gFile == 'yes':
    comp.decompressFile()
    #decryption here