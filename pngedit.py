from PIL import Image


def writeValue(encodeValue, initialValue):
    step = initialValue % 8

    return initialValue + (encodeValue - step)


def encodePng(File, data):
    im = Image.open(File)
    size = im.size
    pix = im.load()
    totalSize = size[0] * size[1]
    encodingTotalSize = (2 * totalSize)/3

    if (len(data) > encodingTotalSize):
        return 0

    y = 0
    for i in range(0, len(data)):
        byte = ord(data[i])*2
        pixel = list(pix[y % size[0], int(y / size[0])])

        if i == len(data) - 1:
            byte += 1  # pour terminer le message
        for j in range(3):  # decoupe des 9 bits en 3 * 3 bits
            tb = int(byte % 8)  # 3 bits car 2³ = 8

            byte = (byte - byte % 8) / 8
            pixel[j] = writeValue(
                tb, pixel[j])

        pix[y % size[0], int(y / size[0])] = tuple(pixel)

        y = y + 1

    im.save('encoded.png')
    return 1


def decodePng(File):
    im = Image.open(File)
    size = im.size
    pix = im.load()
    result = []
    y = 0
    while(True):
        data = 0
        for i in range(3):
            value = pix[y % size[0], int(y / size[0])][2-i] % 8
            data *= 8
            data += value
            print(value)
        result.append(chr(int(data/2)))
        if (pix[y % size[0], int(y / size[0])][0] % 2 != 0):
            break
        y += 1

    print(result)


encodePng('image1.jpg', ['b', 'e'])

decodePng('encoded.png')
# decodePng('image1.jpg')
