#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os,traceback
from PIL import Image

class ResizeImageBuilder:
    def __init__(self):
        # print(self.__class__)
        pass

    def setOriginImagePath(self, filePath):
        try:
            img = Image.open(filePath)
            # img = img.convert('RGB')
            # size = 32, 32
            # img.thumbnail(size)
            print('origin image mode:', img.mode)
            img = img.convert('RGB')
            print('target image mode:', img.mode)
            # img.show()
            self.baseImage = img
            return None
        except (BaseException,e):
            return str(filePath + " open error: " + traceback.format_exc(e))

    def createImageWithOriginImage(self, img, imageSize):
        return img.resize((imageSize, imageSize),Image.ANTIALIAS)

    def saveImageWithPath(self, img, savePath):
        img.save(savePath)

    def createImage(self, savePath, imageSize):
        if self.baseImage == None:
            print('error: self.baseImage == None, please call setOriginImagePath() before createImage()')
            return

        try:
            newimg = self.createImageWithOriginImage(self.baseImage, imageSize)
            self.saveImageWithPath(newimg, savePath)
            # print('done')
        except (BaseException,e):
            return 'createImage error: ' + traceback.format_exc(e)

def main():
    # builder = ResizeImageBuilder()
    # builder.setOriginImagePath(originImagePath)
    # builder.createImage(path1, size1)
    # builder.createImage(path2, size2)
    pass

if __name__ == '__main__':
    main()