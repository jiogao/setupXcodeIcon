# -*- coding: utf-8 -*-

#exp: python setupXcodeIcon.py testRes/Contents.json testRes/Icon.jpg
#auto set up Xcode icon file: Assets.xcassets/AppIcon.appiconset/Contents.json
#auto create images

import os,sys,traceback,json

sys.path.append('resizeImage')
import resizeImage

# {
#   "images" : [
#     {
#       "size" : "20x20",
#       "idiom" : "iphone",
#       "filename" : "Icon-40.jpg",
#       "scale" : "2x"
#     },
#
#     ...
#
#     {
#       "size" : "83.5x83.5",
#       "idiom" : "ipad",
#       "filename" : "Icon-167.jpg",
#       "scale" : "2x"
#     },
#     {
#       "idiom" : "ios-marketing",
#       "size" : "1024x1024",
#       "scale" : "1x"
#     }
#   ],
#   "info" : {
#     "version" : 1,
#     "author" : "xcode"
#   }
# }


def loadJson(path):
    print 'loadJson:', path
    # os.path.join(path, 'Assets.xcassets/AppIcon.appiconset/Contents.json')
    jsonFile = open(path,'r')
    jsonString = jsonFile.read()
    print 'jsonString', jsonString
    jsonFile.close()

    jsonData = json.loads(jsonString)
    # print 'jsonData', jsonData
    return jsonData

def saveJson(path, jsonData):
    print 'saveJson:', path
    jsonString = json.dumps(jsonData, indent=2, separators=(',', ' : ')) #sort_keys=True, 
    jsonFile = open(path,'w')
    print 'jsonString', jsonString
    jsonFile.write(jsonString)
    jsonFile.close()

#jsonFilePath: Contents.json 路径
#baseImagePath: 原始Icon 路径
def autoSetImage(jsonFilePath, baseImagePath):
    jsonData = loadJson(jsonFilePath)

    baseImageBaseName = os.path.basename(baseImagePath)#原文件名
    imageType = os.path.splitext(baseImageBaseName)[1]#原文件后缀

    for imageConfig in jsonData['images']:
        sizeStr = imageConfig['size'].split('x', 1)[0]
        print 'sizeStr' + sizeStr
        size = float(sizeStr)
        scaleStr = imageConfig['scale'].split('x', 1)[0]
        scale = int(scaleStr)


        imageName = 'Icon-' + sizeStr
        if scale != 1:
            imageName += 'x' + scaleStr
        imageName += imageType#各个分辨率的图片文件名
        savePath = os.path.join(os.path.dirname(jsonFilePath), imageName)

        print('createImage: ' + savePath)
        errMsg = resizeImage.createImage(baseImagePath, savePath, int(size*scale))
        if errMsg != None:
            print errMsg
        else:
            imageConfig['filename'] = imageName

        saveJson(jsonFilePath, jsonData)

def main():
    for i in range(0, len(sys.argv)):
        print "argv[", i, "]", sys.argv[i]


    if len(sys.argv) > 2:
        autoSetImage(sys.argv[1], sys.argv[2])
    else:
        # print 'Contents.json Icon.jpg'
        autoSetImage('testRes/Contents.json', 'testRes/Icon.jpg')

if __name__ == '__main__':
    main()

