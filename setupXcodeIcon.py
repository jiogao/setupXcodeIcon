#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#usage: ./setupXcodeIcon.py [-o originIconPath] [-t targetContentsPath]

#auto set up the Xcode icon file: Assets.xcassets/AppIcon.appiconset/Contents.json
#auto create images of corresponding resolution

#Contents.json:
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

import os,sys,traceback,json,getopt

sys.path.append(os.path.join(sys.path[0], 'Classes'))
from ResizeImageBuilder import ResizeImageBuilder

def usage():
    print(\
    '#\n'\
    'usage: ./setupXcodeIcon.py [-o originIconPath] [-t targetContentsPath]\n'\
    '#')

def help():
    print(\
    '#\n'\
    '  -h --help        display this help and exit\n'\
    '  -o --origin      origin icon path\n'\
    '  -t --target      file path of Assets.xcassets/AppIcon.appiconset/Contents.json\n'\
    '#')

def loadJson(path):
    # print('loadJson:', path)
    # os.path.join(path, 'Assets.xcassets/AppIcon.appiconset/Contents.json')
    jsonFile = open(path,'r')
    jsonString = jsonFile.read()
    # print('jsonString', jsonString)
    jsonFile.close()

    jsonData = json.loads(jsonString)
    # print('jsonData', jsonData)
    return jsonData

def saveJson(path, jsonData):
    # print 'saveJson:', path
    jsonString = json.dumps(jsonData, indent=2, separators=(',', ' : ')) #sort_keys=True, 
    jsonFile = open(path,'w')
    # print('jsonString', jsonString)
    jsonFile.write(jsonString)
    jsonFile.close()

#originImagePath: origin icon path
#jsonFilePath: Contents.json path
def autoSetImage(originImagePath, jsonFilePath):
    jsonData = loadJson(jsonFilePath)

    builder = ResizeImageBuilder()
    builder.setOriginImagePath(originImagePath)
    #origin icon file name
    baseImageBaseName = os.path.basename(originImagePath)
    #suffix
    imageType = os.path.splitext(baseImageBaseName)[1]

    print('createImage:')
    for imageConfig in jsonData['images']:
        sizeStr = imageConfig['size'].split('x', 1)[0]
        size = float(sizeStr)
        scaleStr = imageConfig['scale'].split('x', 1)[0]
        scale = int(scaleStr)

        #target file name
        imageName = imageConfig['idiom'] + '-' + sizeStr
        if scale != 1:
            imageName += 'x' + scaleStr
        imageName += imageType
        #target file full path
        savePath = os.path.join(os.path.dirname(jsonFilePath), imageName)

        # print(imageName),
        sys.stdout.write(imageName + ' ')
        errMsg = builder.createImage(savePath, int(size*scale))
        if errMsg != None:
            print(errMsg)
            return
        else:
            imageConfig['filename'] = imageName
    #save Contents.json
    saveJson(jsonFilePath, jsonData)
    print('\ndone')

def main():
    try:
        options,args = getopt.getopt(sys.argv[1:],"ho:t:",["help","origin=","target="])
    except (getopt.GetoptError, e):
        # print('sys.argv error' + traceback.format_exc(e))
        usage()
        sys.exit()

    origin = None
    target = None
    for name,value in options:
        if name in ("-h","--help"):
            help()
            sys.exit()
        
        if name in ("-o","--origin"):
            print('origin is----',value)
            origin = value
        if name in ("-t","--target"):
            print('target is----',value)
            target = value

    # for i in range(0, len(args)):
    #     print("args[", i, "]", args[i])

    if origin == None or target == None:
        usage()
        sys.exit()

    autoSetImage(origin, target)

if __name__ == '__main__':
    main()

