import os

def steganoBMPFile(fileData, pixelStart, data):
	for i in range(len(data)):
		byte = ord(data[i]) * 2  # mise sur 9 bits de l'octet
		if i == len(data) - 1:
			byte += 1  # pour terminer le message
		for j in range(3):  # decoupe des 9 bits en 3 * 3 bits
			tb = int(byte % 8)  # 3 bits car 2³ = 8
			byte = (byte - byte % 8) / 8  # supression des 3 bits traités
			actualByte = pixelStart + i*4 + (2-j)  # détermination de l'octet a modifier
			# (début image + octet du message * 4 (taille d'un pixel en BMP RGB+0xFF) + 3 - position des 3 bits en utilisation)
			fileData[actualByte] = fileData[actualByte] - (fileData[actualByte] % 8) + tb  # mise a jour des data de l'image
	return fileData


def steganoBMPFileReverse(fileData, pixelStart):
	byteValue = 0  # octet actuel
	data = []
	actualByte = pixelStart  # octet dans les données du BMP
	while byteValue % 2 == 0:  # 9bits a récupérer si poid faible a 1 alors fin du message
		byteValue = 0  # initialisation
		for i in range(3):
			byteValue *= 8  # déplacement de 3 bits (2³ = 8) vers la gauche du nombre
			byteValue += fileData[actualByte] % 8  # récupération des 3 bits de poids faible
			actualByte += 1  # déplacement de l'octet vers le suivant
		data.append(chr(int((byteValue - (byteValue % 2)) / 2)))  # récupération de 8bits (sans le bit de poids faible indiquant la fin du message)
		actualByte += 1  # déplacement de l'octet a lire (car pixel RGB+0xFF en BMP)
	return data


def steganoBMP(filename, message, length):
	f = open(filename, "rb")
	fData = bytearray(f.read())
	f.close()
	pS = fData[10]
	width = fData[21] * 16 * 16 * 16 + fData[20] * 16 * 16 + fData[19] * 16 + fData[18]
	heigth = fData[25] * 16 * 16 * 16 + fData[24] * 16 * 16 + fData[23] * 16 + fData[22]
	if length > ((width * length) / 3):
		print("Error message length too long for this file")
		return -1
	newData = steganoBMPFile(fData, pS, message)
	f = open("result.bmp", "wb")
	f.write(newData)
	f.close()
	return 0


def steganoBMPReverse(filename):
	f = open(filename, "rb")
	fData = bytearray(f.read())
	f.close()
	pS = fData[10]
	return steganoBMPFileReverse(fData, pS)
