from PIL import Image

def transform(binary, rgb):
    if ((int(binary) % 2) == (rgb % 2)):
        return rgb
    else:
        return rgb+1

        #TODO : 255 < 0s

def encode(Text):
    im = Image.open('image1.jpg')
    pix = im.load()
    startPixels = [ 0, 0]
    for  i in range(len(Text)):
        binaryChar = bin(int.from_bytes(Text[i].encode(), 'big'))   
        binaryChar = binaryChar[2:len(binaryChar)]
        #print(binaryChar)
        while (len(binaryChar)  < 8):
            binaryChar = ('0' + binaryChar)
        binaryChar = (binaryChar + '1')
        RGB_Start = list(pix[startPixels[0], 0])
        RGB_Middle = list(pix[startPixels[0]+1, 0])
        RGB_End = list(pix[startPixels[0]+2, 0])
        RGB = [RGB_Start, RGB_Middle, RGB_End]
        #print(RGB)
        #print(binaryChar)
        for binar in range(0, len(binaryChar)):

            indexOfPixel = int((binar) / 3)
            indexOfRGB = (binar)%3
            RGB[indexOfPixel][indexOfRGB]
            #print(RGB[indexOfPixel][indexOfRGB] , ' / ' , binaryChar[binar])
            RGB[indexOfPixel][indexOfRGB] = transform(binaryChar[binar], RGB[indexOfPixel][indexOfRGB])
            #print(RGB[indexOfPixel][indexOfRGB])

        pix[startPixels[0], 0] = tuple(RGB[0])
        pix[startPixels[0]+1, 0] = tuple(RGB[1])
        pix[startPixels[0]+2, 0] = tuple(RGB[2])
        startPixels = [startPixels[0] + 3, 0]

        #print(pix[0, 0], pix[1, 0], pix[2, 0])
    im.save('codedImage.png')


def decode(fileName):
    im = Image.open(fileName) # Can be many different formats.
    pix = im.load()
    #print(pix[0, 0], pix[1, 0], pix[2, 0])
    i = 0
    y = 0
    RGB = [list(pix[i, y]), list(pix[i+1,y]), list(pix[i+2, y])]
    Text = []
    while(RGB[2][2] % 2 != 0):
        RGB = [list(pix[i, y]), list(pix[i+1,y]), list(pix[i+2, y])]
        binaryText = ''
        for binary in range(0,8):
            indexOfPixel = int((binary) / 3)
            indexOfRGB = (binary)%3
            binaryText += str(RGB[indexOfPixel][indexOfRGB] % 2)
        #print(binaryText)
        Text.append(binaryText)
        i += 3

    finalStr = ''
    for char in Text:
        finalStr += chr(int(char,2))
    print(finalStr)


#encode('Mot Cacher')
#decode('codedImage.png')

print(open('image1.jpg','rb').read(1))