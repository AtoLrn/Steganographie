from PIL import Image


def transform(binary, rgb):
    if ((int(binary) % 2) == (rgb % 2)):
        return rgb
    else:
        return rgb+1

        # TODO : 255 < 0s


def FileToArray(fileName):
    fileArray = [fileName]
    fileData = open(fileName, 'rb').read()

    for i in range(len(fileData)):
        fileArray.append(hex(fileData[i])[2:].zfill(2))
    return fileArray


def ArrayToFile(array):
    file = open('a'+array[0], 'wb')

    rawData = array[1:]
    for i in range(len(rawData)):
        file.write(bytearray.fromhex(rawData[i]))
    file.close()


def encode(array, File):

    im = Image.open(File)
    size = im.size
    pix = im.load()
    # startPixels = [0, 0]
    pixel = 0
    y = 0
    for i in range(0, len(array)):
        binaryChar = bin(int(array[i], 16))
        binaryChar = binaryChar[2:len(binaryChar)]
        binaryChar = binaryChar.zfill(8)

        binaryChar = (binaryChar + '1')

        # RGB_Start = list(pix[startPixels[0], startPixels[1]])
        # RGB_Middle = list(pix[startPixels[0]+1, startPixels[1]])
        # RGB_End = list(pix[startPixels[0]+2, startPixels[1]])
        RGB_Start = list(pix[pixel % size[0], int(pixel / size[0])])
        pixel = pixel+1
        RGB_Middle = list(pix[pixel % size[0], int(pixel / size[0])])
        pixel = pixel+1
        RGB_End = list(pix[pixel % size[0], int(pixel / size[0])])
        RGB = [RGB_Start, RGB_Middle, RGB_End]
        # print(RGB)
        # print(binaryChar)
        for binar in range(0, len(binaryChar)):

            indexOfPixel = int((binar) / 3)
            indexOfRGB = (binar) % 3
            RGB[indexOfPixel][indexOfRGB]
            # print(RGB[indexOfPixel][indexOfRGB] , ' / ' , binaryChar[binar])
            RGB[indexOfPixel][indexOfRGB] = transform(
                binaryChar[binar], RGB[indexOfPixel][indexOfRGB])
            # print(RGB[indexOfPixel][indexOfRGB])

        pix[(pixel % size[0]) - 2, int(pixel / size[0])] = tuple(RGB[0])
        pix[(pixel % size[0]) - 1, int(pixel / size[0])] = tuple(RGB[1])
        pix[pixel % size[0], int(pixel / size[0])] = tuple(RGB[2])

        # print(pix[0, 0], pix[1, 0], pix[2, 0])
    im.save('codedImage.png')


def decode(fileName):
    im = Image.open(fileName)  # Can be many different formats.
    pix = im.load()
    # print(pix[0, 0], pix[1, 0], pix[2, 0])
    i = 0
    y = 0
    RGB = [list(pix[i, y]), list(pix[i+1, y]), list(pix[i+2, y])]
    Text = []
    while(RGB[2][2] % 2 != 0):
        RGB = [list(pix[i, y]), list(pix[i+1, y]), list(pix[i+2, y])]
        binaryText = ''
        for binary in range(0, 8):
            indexOfPixel = int((binary) / 3)
            indexOfRGB = (binary) % 3
            binaryText += str(RGB[indexOfPixel][indexOfRGB] % 2)
        # print(binaryText)
        Text.append(binaryText)
        i += 3

    finalStr = ''
    file = ''
    isFileName = True
    for char in Text:
        if (char == '00000001'):
            isFileName = False
            continue
        if (isFileName == True):
            file += chr(int(char, 2))
        else:
            finalStr += chr(int(char, 2))
    print(file, finalStr)
    returnFile = open('a'+file, 'w')
    for char in finalStr:
        returnFile.write(char)
    returnFile.close()


def transformArray(array):
    tmpArray = []
    for char in array[0]:
        tmpArray.append(hex(ord(char))[2:].zfill(2))
    tmpArray.append('01')
    tmpArray.extend(array[1:])
    return tmpArray


array = FileToArray('image1.jpg')
# print(array)
array = transformArray(array)
# print(array)
encode(array, 'imageTest.jpg')

# decode('codedImage.png')
