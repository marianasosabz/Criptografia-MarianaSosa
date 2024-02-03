import random
import hashlib

# parámetros globales
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 2

# generar clave privada aleatoria de 256 bits
def generar_clave_privada():
    return random.randint(0, 2**256)

# simula el intercambio de números entre Alice y Bob
a = generar_clave_privada()
A = pow(g, a, p)

b = generar_clave_privada()
B = pow(g, b, p)

print("Clave pública de Alice: ", A)
print("Clave pública de Bob: ", B)

# cálculo de la clave secreta
s1 = pow(B, a, p)
s2 = pow(A, b, p)

print("Clave secreta de Alice: ", s1)
print("Clave secreta de Bob: ", s2)

# verificación con SHA256
hash1 = hashlib.sha256(str(s1).encode("utf-8")).hexdigest()
hash2 = hashlib.sha256(str(s2).encode("utf-8")).hexdigest()

print("Hash de la clave de Alice:", hash1)
print("Hash de la clave de Bob:", hash2)

if hash1 == hash2:
    print("Las claves coinciden!")
else:
    print("Las claves no coinciden!")
