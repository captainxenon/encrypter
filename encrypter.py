# IMPORTS

import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# KEY GENERATION

# usually is an input in the form of a string
password_provided = input("Please provide a Password for Encryption: ")
password = password_provided.encode()  # convert this to bytes

salt = b'\xaes\xff\x80\xe2{\xfcG\xbdk\xed\xb9\x15n7'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))
print()
print("This is the key in byte format: "+str(key))

# SAVING THE KEY TO A FILE

with open("./encrypter/newkey.key", "wb") as f:
    f.write(key)

# SAMPLE TEXT FILE CONTENT PRINTED IN THE TERMINAL

with open('./encrypter/sample.txt', 'r') as f:
    f_contents = f.read()
    print()
    print("This is the content in the file: "+f_contents)
    print()

# OPEN KEY FROM NEWKEY.KEY AND STORE IT INTO THE KEY VARIABLE

file = open('./encrypter/newkey.key', 'rb')
key = file.read()
file.close()

# OPEN THE SAMPLE.TXT FILE AND STORE IT IN THE DATA VARIABLE

with open('./encrypter/sample.txt', 'rb') as f:
    data = f.read()

# ENCRYPT THE DATA

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

print("This is the encrypted version of sample.txt: "+str(encrypted))
print()

# MAKE THE ENCRYPTED VERSION OF THE SAMPLE.TXT FILE

with open('./encrypter/sample.txt.encrypted', 'wb') as f:
    data = f.write(encrypted)

# DELETE THE ORIGINAL SAMPLE.TXT TO MAKE IT MORE INTERESTING

os.remove("./encrypter/sample.txt")
