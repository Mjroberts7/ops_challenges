# this file is to be testing breakdowns of certain code snippets 


from cryptography.fernet import Fernet

# This line writes creates an encryption key called encKey.
# It then opens the key value of encKey and writes it to binary.
def writekey():
    encKey = Fernet.generate_key()
    with open("encKey.key", "wb") as key_file:
        key_file.write(encKey)

# this is a function that calls for the key so we dont have to create it every time with writekey.
def loadkey():
    return open("encKey.key", "rb").read()

# This is calling the function that writes the encryption key
writekey()

# this is assigning a variable the function that reads the key
key = loadkey()

# here we are creating a string that we are going to encrypt
message = str(input("what would you like to put? ")).encode()
print(message)

# if __name__ == "__main__"
f = Fernet(key)

encMessage = f.encrypt(message)
print(encMessage)

decMessage = f.decrypt(encMessage)
print(decMessage)