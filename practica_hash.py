import hashlib

def hash_text(text):
    # Crear un objeto de hash
    hasher = hashlib.sha256()
    # Actualizar el objeto de hash con el texto
    hasher.update(text.encode('utf-8'))
    # Calcular el hash y devolverlo en formato hexadecimal
    return hasher.hexdigest()

def hash_file(file_path):
    # Crear un objeto de hash
    hasher = hashlib.sha256()
    # Leer el archivo en bloques para manejar archivos grandes
    with open(file_path, 'rb') as f:
        while True:
            # Leer un bloque de 4096 bytes del archivo
            chunk = f.read(4096)
            if not chunk:
                break
            # Actualizar el objeto de hash con el bloque
            hasher.update(chunk)
    # Calcular el hash y devolverlo en formato hexadecimal
    return hasher.hexdigest()

# 1. Hash de una cadena de texto de 8 bits
text_8_bits = "12345678"
hash_8_bits = hash_text(text_8_bits)
print("Hash de una cadena de texto de 8 bits:", hash_8_bits)

# 2. Hash de una cadena de texto de 1024 bits
text_1024_bits = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 32
hash_1024_bits = hash_text(text_1024_bits)
print("Hash de una cadena de texto de 1024 bits:", hash_1024_bits)

# 3. Hash de un archivo PDF
file_path = "cdarchivo_dummy.pdf"
hash_pdf = hash_file(file_path)
print("Hash del archivo PDF:", hash_pdf)
