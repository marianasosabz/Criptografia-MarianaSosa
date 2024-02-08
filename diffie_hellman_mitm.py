import hashlib

p = 23 
g = 5

# Eve genera su llave privada 
e = 19  

# Bob y Alice comparten la misma llave privada  
b = 15  
a = b

yb = pow(g, b, p)
wa = pow(g, a, p)

# Eve calcula la llave secreta para ambas comunicaciones
kb = pow(yb, e, p)  
ka = pow(wa, e, p)  

hash_kb = hashlib.md5(str(kb).encode('utf-8')).hexdigest()
hash_ka = hashlib.md5(str(ka).encode('utf-8')).hexdigest()

print("Hash llave Eve-Bob:", hash_kb) 
print("Hash llave Eve-Alice:", hash_ka)

if hash_kb == hash_ka:
  print("MITM exitoso - Eve obtuvo la misma llave")
else:
  print("MITM fallido - llaves diferentes")
