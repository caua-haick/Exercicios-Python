from hashlib import sha256
#SHA == Secure Hash Algoritm
texto = "Coração"

cod = texto.encode('utf-8')
#hash = hashlib.256(cod).hexdigest()
hash = sha256(cod).hexdigest()
print(hash)