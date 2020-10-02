import os

file = open("test.bmp", "rb")
newFile = open("testStegano.bmp", "wb")
fileData = bytearray(file.read())
pixelStart = fileData[10]
width = fileData[21] * 16 * 16 * 16 + fileData[20] * 16 * 16 + fileData[19] * 16 + fileData[18]
heigth = fileData[25] * 16 * 16 * 16 + fileData[24] * 16 * 16 + fileData[23] * 16 + fileData[22]
fileLength = os.stat("test.bmp").st_size
print(len(fileData))
print(str(width) + " : " + str(heigth))
data = "ABCD"
for i in range(len(data)):
	byte = ord(data[i]) * 2 # mise sur 9 bits de l'octet
	if i == len(data) - 1:
		byte += 1
	for j in range(3):
		tb = int(byte % 8)
		byte = (byte - byte % 8) / 8
		actualByte = pixelStart + i*3 + (3-j)
		fileData[actualByte] = fileData[actualByte] - fileData[actualByte]%8 + tb
newFile.write(fileData)
