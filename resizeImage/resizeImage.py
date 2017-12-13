# -*- coding: utf-8 -*-
 
import sys,os,traceback
from PIL import Image


def changeSize(im,newSize):
    newimg = im.resize((newSize, newSize),Image.ANTIALIAS)
    return newimg

def createImage(filePath, savePath, imageSize):
    try:
        img = Image.open(filePath)
    except (BaseException),e:
        return str(filePath + " open error: " + e.message)

    if(not filePath.endswith('.jpg') and not filePath.endswith('.png') and not filePath.endswith('.JPG') and not filePath.endswith('.PNG')):
        return str(filePath + '不是图片')
    else:
        try:
            newimg = changeSize(img,imageSize)
            newimg.save(savePath)
        except (BaseException),e:
            return str(filePath + " change error: " + traceback.format_exc(e))

        print "done"


def main():
    pass

if __name__ == '__main__':
    main()