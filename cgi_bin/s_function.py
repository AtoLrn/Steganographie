from PIL import Image
from des import DesKey


def writeValue(encodeValue, initialValue):
	step = initialValue % 8

	return initialValue + (encodeValue - step)


def encodePng(File, data):
	im = Image.open(File)
	size = im.size
	pix = im.load()
	totalSize = size[0] * size[1]
	encodingTotalSize = (2 * totalSize) / 3

	if len(data) > encodingTotalSize:
		return -1

	y = 0
	for i in range(0, len(data)):
		byte = ord(data[i]) * 2
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
	return 0


def decodePng(File):
	im = Image.open(File)
	size = im.size
	pix = im.load()
	result = []
	y = 0
	while (True):
		data = 0
		for i in range(3):
			value = pix[y % size[0], int(y / size[0])][2 - i] % 8
			data *= 8
			data += value
			print(value)
		result.append(chr(int(data / 2)))
		if (pix[y % size[0], int(y / size[0])][0] % 2 != 0):
			break
		y += 1
	result = "".join(result)
	print(result)
	return bytes(result, "utf-8")


def steganoBMPFile(fileData, pixelStart, data):
	for i in range(len(data)):
		byte = data[i] * 2  # mise sur 9 bits de l'octet
		if i == len(data) - 1:
			byte += 1  # pour terminer le message
		for j in range(3):  # decoupe des 9 bits en 3 * 3 bits
			tb = int(byte % 8)  # 3 bits car 2³ = 8
			byte = (byte - byte % 8) / 8  # supression des 3 bits traités
			# détermination de l'octet a modifier
			actualByte = pixelStart + i * 4 + (2 - j)
			# (début image + octet du message * 4 (taille d'un pixel en BMP RGB+0xFF) + 3 - position des 3 bits en utilisation)
			# mise a jour des data de l'image
			fileData[actualByte] = fileData[actualByte] - \
								   (fileData[actualByte] % 8) + tb
	return fileData


def steganoBMPFileReverse(fileData, pixelStart):
	byteValue = 0  # octet actuel
	data = []
	actualByte = pixelStart  # octet dans les données du BMP
	while byteValue % 2 == 0:  # 9bits a récupérer si poid faible a 1 alors fin du message
		byteValue = 0  # initialisation
		for i in range(3):
			# déplacement de 3 bits (2³ = 8) vers la gauche du nombre
			byteValue *= 8
			# récupération des 3 bits de poids faible
			byteValue += fileData[actualByte] % 8
			actualByte += 1  # déplacement de l'octet vers le suivant
		# récupération de 8bits (sans le bit de poids faible indiquant la fin du message)
		data.append(int((byteValue - (byteValue % 2)) / 2))
		# déplacement de l'octet a lire (car pixel RGB+0xFF en BMP)
		actualByte += 1
	return bytes(data)


def steganoBMP(filename, message, length):
	f = open(filename, "rb")
	fData = bytearray(f.read())
	f.close()
	pS = fData[10]
	width = fData[21] * 16 * 16 * 16 + fData[20] * 16 * 16 + fData[19] * 16 + fData[18]
	heigth = fData[25] * 16 * 16 * 16 + fData[24] * 16 * 16 + fData[23] * 16 + fData[22]
	if length > (width * heigth):
		print("Error message length too long for this file")
		return -1
	newData = steganoBMPFile(fData, pS, message)
	f = open(filename, "wb")
	f.write(newData)
	f.close()
	return 0


def steganoBMPReverse(filename):
	f = open(filename, "rb")
	fData = bytearray(f.read())
	f.close()
	pS = fData[10]
	return steganoBMPFileReverse(fData, pS)


def encryptage(data, key):
	ndata = data.encode('utf-8')
	key = parsekey(key)
	nkey = key.encode('utf-8')
	key0 = DesKey(nkey)
	encrypted_message = key0.encrypt(ndata, padding=True)
	return encrypted_message


def decryptage(data, key):
	key = parsekey(key)
	nkey = key.encode('utf-8')
	key0 = DesKey(nkey)
	decrypted_message = key0.decrypt(data, padding=True)
	decrypted_message = decrypted_message.decode('utf-8')
	return decrypted_message


def parsekey(key):
	if 24 > len(key) > 0:
		while len(key) % 8 != 0:
			key += key[len(key) - 1]
	if len(key) > 24:
		key = key[:24]
	return key
