
# Junjar singh project 1

import os
from Crypto.Cipher import AES
from Crypto import Random
import hashlib


def encrypt(password, filename):
    chunksize = 64*1024
    
    outputFile = "(enc)"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    key = hashlib.sha256(password.encode('utf-8')).digest()
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    try:

        with open(filename, 'rb') as infile:  # rb means read in binary
            with open(outputFile, 'wb') as outfile:  # wb means write in the binary mode
                outfile.write(filesize.encode('utf-8'))
                outfile.write(IV)

                while True:
                    chunk = infile.read(chunksize)

                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' '*(16-(len(chunk) % 16))

                    outfile.write(encryptor.encrypt(chunk))
    except FileNotFoundError:
        print("file doesnt exist")


def decrypt(password, filename):
    chunksize = 64*1024
    
    outputFile = "(decre)"
    key = hashlib.sha256(password.encode('utf-8')).digest()
    try:

        with open(filename, 'rb') as infile:
            filesize = int(infile.read(16))
            IV = infile.read(16)

            decryptor = AES.new(key, AES.MODE_CBC, IV)

            with open(outputFile, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)

                    if len(chunk) == 0:
                        break

                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(filesize)
    except FileNotFoundError:
        print("file doesnt exist")


# def getKey(password):
#     hasher = SHA256.new(password.encode('utf-8'))
#     return hasher.digest()


while True:
   
    choice = input("Would you like to (e)encrypt or (d)Decrypt or (q)quit ")

    if choice == 'e':
        filename = input("File to encrypt: ")
        password = input("Password: ")
        encrypt(password, filename)
        print('Done.')
    elif choice == 'd':
        filename = input("File to decrypt: ")
        password = input("Password: ")
        decrypt(password, filename)
        print("Done.")

    elif choice == 'q':
        break
                
    else:
        print("No option selected, closing...")