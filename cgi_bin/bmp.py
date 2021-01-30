import function

data = "bonjour bande de con"
function.steganoBMP("test.bmp", data, 52)
res = function.steganoBMPReverse("result.bmp")
for i in range(len(res)):
	print(str(res[i]), end="")

