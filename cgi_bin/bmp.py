import s_function

data = "Un jour je deviendrai hokage"
key = "12345678"

encrypted_message = s_function.encryptage(data, key)
s_function.steganoBMP("test.bmp", encrypted_message, 52)

res = s_function.steganoBMPReverse("result.bmp")
decrypted_message = s_function.decryptage(res, key)

print(decrypted_message)

