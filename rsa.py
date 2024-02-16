# Práctica de algoritmo RSA
# Cifrado de mensaje

# 2024-02-14 - Anahuac Mayab

# Hacer los imports
import Crypto.Util.number

# Número de bits
bits = 1024

# Obtener los primos para Alice y Bob
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("pA: ", pA, "\n")
qA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("qA: ", qA, "\n")

pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("pB: ", pB, "\n")
qB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("qB: ", qB, "\n")

# Obtener la primera parte de la llave pública de ALice y Bob
nA=pA*qA
print("nA: ", nA,"\n")

nB=pB*qB
print("nB: ", nB,"\n")

# Calcular el indicador de Euler Phi
phiA = (pA-1)*(qA-1)
print("phiA: ", phiA, "\n")

phiB = (pB-1)*(qB-1)
print("phiB: ", phiB, "\n")

# Por razones de eficiencia usaremos el número 4 de Fermat, 65537, debido a que es
# un primo largo y no es potencia de 2, y como forma parte de la clave pública
# no es necesario calcularlo

e = 65537

# Calcular la llave privada de Alice y Bob
dA = Crypto.Util.number.inverse(e, phiA)
print("dA: ", dA, "\n")

dB = Crypto.Util.number.inverse(e, phiB)
print("dB: ", dB, "\n")

# Cifrar el mensaje
msg = "Hola mundo"
print("Mensaje original: ", msg, "\n")
print("Longitud del mensaje en bytes: ", len(msg.encode("utf-8")))

# Convertir el mensaje a número
m = int.from_bytes(msg.encode("utf-8"), byteorder = "big")
print("Mensaje convertido en entero: ", m, "\n")

# Cifrar el mensaje
c = pow(m, e, nB)
print("Mensaje cifrado: ", c, "\n")

# Desciframos el mensaje
des = pow(c, dB, nB)
print("Mensaje descifrado: ", des, "\n")

# Convertimos el mensaje de número a texto
msg_final = int.to_bytes(des, len(msg), byteorder="big").decode("utf-8")
print("Mensaje final: ", msg_final, "\n")