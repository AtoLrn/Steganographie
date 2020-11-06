import zlib


def steganoBMP(fileData, pixelStart, data):
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


def steganoBMPReverse(fileData, pixelStart):
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


def steganoPNG(fileData,pixelStart):
	# TODO
	return 1


def DES(data):

	return data


def permutation(data):
	permut = []
	for i in range (64):
		if i < 32:
			half = 0
		else:
			half = 1
		index = 57 - (((i % 32) % 8) * 8) + 2 * int((i % 32) / 8) - half
		permut.append(data[index])
	return permut


def S1(data):
	switcher = {
		0: 14, 1: 0, 2: 4, 3: 15, 4: 13, 5: 7, 6: 1, 7: 4, 8: 2, 9: 14, 10: 15, 11: 2, 12: 11, 13: 13, 14: 8, 15: 1,
		16: 3, 17: 10, 18: 10, 19: 6, 20: 6, 21: 12, 22: 12, 23: 11, 24: 5, 25: 9, 26: 9, 27: 5, 28: 0, 29: 3, 30: 7, 31: 8,
		32: 4, 33: 15, 34: 1, 35: 12, 36: 14, 37: 8, 38: 8, 39: 2, 40: 13, 41: 4, 42: 6, 43: 9, 44: 2, 45: 1, 46: 11, 47: 7,
		48: 15, 49: 5, 50: 12, 51: 11, 52: 9, 53: 3, 54: 7, 55: 14, 56: 3, 57: 10, 58: 10, 59: 0, 60: 5, 61: 6, 62: 0, 63: 13,
	}
	value = switcher.get(data, "error")


def S2(data):
	switcher = {
		0: 15, 1: 3, 2: 1, 3: 13, 4: 8, 5: 4, 6: 14, 7: 7, 8: 6, 9: 15, 10: 11, 11: 2, 12: 3, 13: 8, 14: 4, 15: 14,
		16: 9, 17: 12, 18: 7, 19: 0, 20: 2, 21: 1, 22: 13, 23: 10, 24: 12, 25: 6, 26: 0, 27: 9, 28: 5, 29: 11, 30: 10, 31: 5,
		32: 0, 33: 13, 34: 14, 35: 8, 36: 7, 37: 10, 38: 11, 39: 1, 40: 10, 41: 3, 42: 4, 43: 15, 44: 13, 45: 4, 46: 1, 47: 2,
		48: 5, 49: 11, 50: 8, 51: 6, 52: 12, 53: 7, 54: 6, 55: 12, 56: 9, 57: 0, 58: 3, 59: 5, 60: 2, 61: 14, 62: 15, 63: 9,
	}
	value = switcher.get(data, "error")


def S3(data):
	switcher = {
		0: 14, 1: 0, 2: 4, 3: 15, 4: 13, 5: 7, 6: 1, 7: 4, 8: 2, 9: 14, 10: 15, 11: 2, 12: 11, 13: 13, 14: 8, 15: 1,
		16: 3, 17: 10, 18: 10, 19: 6, 20: 6, 21: 12, 22: 12, 23: 11, 24: 5, 25: 9, 26: 9, 27: 5, 28: 0, 29: 3, 30: 7, 31: 8,
		32: 4, 33: 15, 34: 1, 35: 12, 36: 14, 37: 8, 38: 8, 39: 2, 40: 13, 41: 4, 42: 6, 43: 9, 44: 2, 45: 1, 46: 11, 47: 7,
		48: 15, 49: 5, 50: 12, 51: 11, 52: 9, 53: 3, 54: 7, 55: 14, 56: 3, 57: 10, 58: 10, 59: 0, 60: 5, 61: 6, 62: 0, 63: 13,
	}
	value = switcher.get(data, "error")


def S4(data):
	switcher = {
		0: 14, 1: 0, 2: 4, 3: 15, 4: 13, 5: 7, 6: 1, 7: 4, 8: 2, 9: 14, 10: 15, 11: 2, 12: 11, 13: 13, 14: 8, 15: 1,
		16: 3, 17: 10, 18: 10, 19: 6, 20: 6, 21: 12, 22: 12, 23: 11, 24: 5, 25: 9, 26: 9, 27: 5, 28: 0, 29: 3, 30: 7, 31: 8,
		32: 4, 33: 15, 34: 1, 35: 12, 36: 14, 37: 8, 38: 8, 39: 2, 40: 13, 41: 4, 42: 6, 43: 9, 44: 2, 45: 1, 46: 11, 47: 7,
		48: 15, 49: 5, 50: 12, 51: 11, 52: 9, 53: 3, 54: 7, 55: 14, 56: 3, 57: 10, 58: 10, 59: 0, 60: 5, 61: 6, 62: 0, 63: 13,
	}
	value = switcher.get(data, "error")


def S5(data):
	switcher = {
		0: 14, 1: 0, 2: 4, 3: 15, 4: 13, 5: 7, 6: 1, 7: 4, 8: 2, 9: 14, 10: 15, 11: 2, 12: 11, 13: 13, 14: 8, 15: 1,
		16: 3, 17: 10, 18: 10, 19: 6, 20: 6, 21: 12, 22: 12, 23: 11, 24: 5, 25: 9, 26: 9, 27: 5, 28: 0, 29: 3, 30: 7, 31: 8,
		32: 4, 33: 15, 34: 1, 35: 12, 36: 14, 37: 8, 38: 8, 39: 2, 40: 13, 41: 4, 42: 6, 43: 9, 44: 2, 45: 1, 46: 11, 47: 7,
		48: 15, 49: 5, 50: 12, 51: 11, 52: 9, 53: 3, 54: 7, 55: 14, 56: 3, 57: 10, 58: 10, 59: 0, 60: 5, 61: 6, 62: 0, 63: 13,
	}
	value = switcher.get(data, "error")


def S6(data):
	switcher = {
		0: 14, 1: 0, 2: 4, 3: 15, 4: 13, 5: 7, 6: 1, 7: 4, 8: 2, 9: 14, 10: 15, 11: 2, 12: 11, 13: 13, 14: 8, 15: 1,
		16: 3, 17: 10, 18: 10, 19: 6, 20: 6, 21: 12, 22: 12, 23: 11, 24: 5, 25: 9, 26: 9, 27: 5, 28: 0, 29: 3, 30: 7, 31: 8,
		32: 4, 33: 15, 34: 1, 35: 12, 36: 14, 37: 8, 38: 8, 39: 2, 40: 13, 41: 4, 42: 6, 43: 9, 44: 2, 45: 1, 46: 11, 47: 7,
		48: 15, 49: 5, 50: 12, 51: 11, 52: 9, 53: 3, 54: 7, 55: 14, 56: 3, 57: 10, 58: 10, 59: 0, 60: 5, 61: 6, 62: 0, 63: 13,
	}
	value = switcher.get(data, "error")


def S7(data):
	switcher = {
		0: 14, 1: 0, 2: 4, 3: 15, 4: 13, 5: 7, 6: 1, 7: 4, 8: 2, 9: 14, 10: 15, 11: 2, 12: 11, 13: 13, 14: 8, 15: 1,
		16: 3, 17: 10, 18: 10, 19: 6, 20: 6, 21: 12, 22: 12, 23: 11, 24: 5, 25: 9, 26: 9, 27: 5, 28: 0, 29: 3, 30: 7, 31: 8,
		32: 4, 33: 15, 34: 1, 35: 12, 36: 14, 37: 8, 38: 8, 39: 2, 40: 13, 41: 4, 42: 6, 43: 9, 44: 2, 45: 1, 46: 11, 47: 7,
		48: 15, 49: 5, 50: 12, 51: 11, 52: 9, 53: 3, 54: 7, 55: 14, 56: 3, 57: 10, 58: 10, 59: 0, 60: 5, 61: 6, 62: 0, 63: 13,
	}
	value = switcher.get(data, "error")


def S8(data):
	switcher = {
		0: 14, 1: 0, 2: 4, 3: 15, 4: 13, 5: 7, 6: 1, 7: 4, 8: 2, 9: 14, 10: 15, 11: 2, 12: 11, 13: 13, 14: 8, 15: 1,
		16: 3, 17: 10, 18: 10, 19: 6, 20: 6, 21: 12, 22: 12, 23: 11, 24: 5, 25: 9, 26: 9, 27: 5, 28: 0, 29: 3, 30: 7, 31: 8,
		32: 4, 33: 15, 34: 1, 35: 12, 36: 14, 37: 8, 38: 8, 39: 2, 40: 13, 41: 4, 42: 6, 43: 9, 44: 2, 45: 1, 46: 11, 47: 7,
		48: 15, 49: 5, 50: 12, 51: 11, 52: 9, 53: 3, 54: 7, 55: 14, 56: 3, 57: 10, 58: 10, 59: 0, 60: 5, 61: 6, 62: 0, 63: 13,
	}
	value = switcher.get(data, "error")

