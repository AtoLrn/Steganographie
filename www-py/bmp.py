import function

data = "bonjour bande de con"
# for i in range(len(data)):
# 	byte = ord(data[i]) * 2 # mise sur 9 bits de l'octet
# 	if i == len(data) - 1:
# 		byte += 1
# 	for j in range(3):
# 		tb = int(byte % 8)
# 		byte = (byte - byte % 8) / 8
# 		actualByte = pixelStart + i*3 + (3-j)
# 		fileData[actualByte] = fileData[actualByte] - fileData[actualByte]%8 + tb

function.steganoBMP("test.bmp", data, 52)
res = function.steganoBMPReverse("result.bmp")
for i in range(len(res)):
	print(str(res[i]), end="")

