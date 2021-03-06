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

    with open('IMUdata.csv', 'rb') as infile:
        text = infile.read()

    #trying to read as string then turn to bytes
    #with open('sample.csv', 'rt') as infile:
        #txt = infile.read()

    #print(txt)

    #text = bytes(txt, 'utf-8')
    
    #print("\n")
    #print(text)
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

        #need to change from bytes to text first
        decomp_text = str(decomp_content)
        with open('sampleout.csv', 'wt') as w:
            w.write(decomp_text)
    print("Compressed and decompressed data the same?", text== decomp_content)