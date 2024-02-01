# Cifrado Fernet

from cryptography.fernet import Fernet

clave = Fernet.generate_key()

f = Fernet(clave)

print(clave)

token = f.encrypt(b'ya casi cumplimos 22 como Taylor, tqm')

print(token)

des = f.decrypt(token)

print(des)
