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
    targetFileName = "sampleOut_" + ".csv"
    with open(targetFileName, 'wb') as outfile:
        outfile.write(compressedDataCode)
