# -*- coding: utf-8 -*-
 
import sys, os, resizeImage

sys.path.append('../utility')
from utility_encode import encodeUtf8

rootDir = sys.path[0] + os.sep
targetDir = sys.path[0] + os.sep + 'output' + os.sep
fileName = 'Icon.jpg'

def batchResize(sizeList):
    try:
        if not os.path.exists(targetDir) or os.path.isfile(targetDir):
            os.mkdir(targetDir)
        errFile = open(targetDir + 'errFile.txt','w')
    except (BaseException),e:
        print encodeUtf8('errFile打开失败')

    filePath = rootDir + fileName
    print 'origin file', filePath
    
    for x in sizeList:

        targetFileBasename = os.path.basename(filePath)
        targetFileNames = os.path.splitext(targetFileBasename)
        savePath = targetDir + targetFileNames[0] + '-' + str(x) + targetFileNames[1]

        print('createImage: ' + savePath)
        errMsg = resizeImage.createImage(filePath, savePath, x)
        if errMsg != None:
            errFile.write(errMsg + '\n')
            print errMsg
    print encodeUtf8('处理完毕')
    errFile.close()

def main():
    sizeList = [16,20,28,29,32,36,40,48,50,57,58,60,64,72,76,80,87,90,96,100,108,114,120,128,144,152,155,167,180,192,256,512]
    batchResize(sizeList)

if __name__ == '__main__':
    main()
