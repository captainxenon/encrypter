from cryptography.fernet import Fernet

# OPEN KEY FROM NEWKEY.KEY AND STORE IT INTO THE KEY VARIABLE

file = open('./encrypter/newkey.key', 'rb')
key = file.read()
file.close()

# DECRYPTION ALGORITHM(ASSUMING YOU ALREADY HAVE ACCESS TO THE KEY GENERATED PREVIOUSLY)

with open('./encrypter/sample.txt.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open('./encrypter/sample.txt.decrypted', 'wb') as f:
    data = f.write(encrypted)
