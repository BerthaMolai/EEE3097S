#!/usr/bin/env python3
#
#    https://github.com/cosinekitty/compressgame
#
#    MIT License
#
#    Copyright (c) 2020 Don Cross <cosinekitty@gmail.com>
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.
#
#   last modified by Bertha Molai, ~4/10/21
import sys
import os
import gzip
import zlib
import lzma
import time

#--------------------------------------------------------------------

AlgorithmList = [ gzip, zlib, lzma
]

#--------------------------------------------------------------------

if __name__ == '__main__':

    # Create a directory to add zipped files
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

    words = text.split()
    print('Read {} words, {} bytes.'.format(len(words), len(text)))

    bestSize = None
    bestTime = None
    bestSourceCode = None
    times = []
    dectimes = []
    
    for algorithm in AlgorithmList:
        for i in range(1, 11):
            start = time.time()
            compressedDataCode = algorithm.compress(text)
            finish = time.time()
            cTime = finish - start
            times.append(cTime)            
            #stubFileName = os.path.join(StubDirName, algorithm.Name() + '.py')
            targetFileName = os.path.join(OutputDirName, "sampleOut_" + algorithm.__name__ + ".csv." +algorithm.__name__)
            with open(targetFileName, 'wb') as outfile:
                outfile.write(compressedDataCode)
            size = len(compressedDataCode)
            
            #result = subprocess.run([sys.executable, targetFileName], check=True, stdout=subprocess.PIPE)
            start = time.time()
            check = algorithm.decompress(compressedDataCode)
            finish = time.time()
            dTime = finish - start
            dectimes.append(dTime)
            
        if check != text:
            print('FAILURE: Generated text does not match original.')
            sys.exit(1)
        if (bestSize is None) or (size < bestSize):
            bestSize = size
            bestAlgorithm = algorithm
        
        #print out compressed file size
        print('{:9d} {:s}'.format(size, targetFileName))
        compRatio = len(text) / size
        reduction = (1- size/len(text))*100
        avg = sum(times)/len(times)
        print("Average compression time: ", str(avg))
        print("Compression ratio: " + str(int(compRatio)) + " with reduction of " + "{:.2f}".format(reduction) +"%")

        if (bestTime is None) or (avg < bestTime):
            bestTime = avg
            bestTAlgorithm = algorithm
        
        avg_d = sum(dectimes)/len(dectimes)
        print("Average decompression time: ", str(avg_d))        

    print()
    print('The size winner is:', bestAlgorithm.__name__)
    print('The time winner is:', bestTAlgorithm.__name__)
    sys.exit(0)