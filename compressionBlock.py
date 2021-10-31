import os
import gzip

def openfile(filename):
    global text
    with open(filename, 'rb') as infile:
        text = infile.read()

def compressFile():
    #directory to print to
    OutputDirName = 'output'
    # Delete any current test files in the output directory.
    for fn in os.listdir(OutputDirName):    
        fullname = os.path.join(OutputDirName, fn)
        print(fullname)
        os.remove(fullname)
    compressedDataCode = gzip.compress(text)

    global targetFileName
    #"sampleOut" will contain diff file names
    targetFileName = os.path.join(OutputDirName, "sampleOut_" + ".csv.gzip")

    #targetFileName = "sampleOut_" + ".csv.gzip"
    with open(targetFileName, 'wb') as outfile:
        outfile.write(compressedDataCode)
    print("Done compressing ")

    return targetFileName

def decompressFile(compressedFile):
    #decompression and comparison
    with open(compressedFile, mode='rt', encoding ='utf-8') as f:
        decomp_content = f.read() 
        with open('systemOutput.csv', 'w', encoding='utf-8') as fout:
            fout.write(decomp_content)
            #we can always write this data to a normal file
    print("Compressed and decompressed data the same?", text== decomp_content)

