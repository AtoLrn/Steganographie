import os

file = open("image2.png", "rb")
newFile = open("imageStegano.png", "wb")
fileData = bytearray(file.read())
IDATstart = fileData.find(bytes("IDAT", "UTF-8"))
fileLength = os.stat("image2.png").st_size
print(fileData)
print(IDATstart)
for i in range(IDATstart + 4, IDATstart + 5):
	if fileData[i] == 0:
		fileData[i] = fileData[i] + 1
	else:
		fileData[i] = fileData[i] - 1
newFile.write(fileData)
