from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

text = input('Entrer Text : ').encode('utf-8')

cipher_text = cipher_suite.encrypt(text)
plain_text = cipher_suite.decrypt(cipher_text)


print(cipher_text)
print(plain_text.decode('utf-8'))
