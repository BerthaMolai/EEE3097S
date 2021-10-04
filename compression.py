import os
import gzip

if __name__ == '__main__':
    #StubDirName = 'stubs'

    # Create a directory to hold the generated source code.
    OutputDirName = 'output'
    if not os.path.exists(OutputDirName):
        os.mkdir(OutputDirName)

    # Delete any stale files in the output directory.
    for fn in os.listdir(OutputDirName):
        fullname = os.path.join(OutputDirName, fn)
        print(fullname)
        os.remove(fullname)

    with open('sample.csv', 'rb') as infile:
        text = infile.read()
    
    compressedDataCode = gzip.compress(text)

    #"sampleOut" will contain diff file names
    targetFileName = os.path.join(OutputDirName, "sampleOut_" + ".csv.gzip")

    #targetFileName = "sampleOut_" + ".csv.gzip"
    with open(targetFileName, 'wb') as outfile:
        outfile.write(compressedDataCode)

    #decompression and comparison
    with gzip.open(targetFileName, 'rb') as f:
        decomp_content = f.read() 
        #we can always write this data to a normal file
    print("Compressed and decompressed data the same?", text== decomp_content)
    #print(text== decompressedData)
