# Cifrado Fernet con mensaje de Sofi

from cryptography.fernet import Fernet

clave_sofi = input("Ingresa tu token: ")

f = Fernet(clave_sofi)

msg = input("Ingresa el mensaje encriptado: ")

decrypted_msg = f.decrypt(msg)

print(decrypted_msg)
