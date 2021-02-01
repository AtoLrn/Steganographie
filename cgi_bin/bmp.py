import function

data = "Un jour je deviendrai hokage"
key = "12345678"

encrypted_message = function.encryptage(data, key)
function.steganoBMP("test.bmp", encrypted_message, 52)

res = function.steganoBMPReverse("result.bmp")
decrypted_message = function.decryptage(res, key)

print(decrypted_message)

