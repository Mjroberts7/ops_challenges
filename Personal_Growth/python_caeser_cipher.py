class Caesar():

    def __init__(self):
        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''

    def __crypt(self, mode):
        for symbol in self.message.upper():
            if symbol in self.LETTERS:
                num = self.LETTERS.find(symbol)
                if mode == 'encrypt':
                    num = num + self.key
                elif mode == 'decrypt':
                    num = num - self.key

                if num >= len(self.LETTERS):
                    num = num - len(self.LETTERS)
                elif num < 0:
                    num = num + len(self.LETTERS)

                self.translated = self.translated + self.LETTERS[num]
            else:
                self.translated = self.translated + symbol

        return self.translated

    def encrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('encrypt')

    def decrypt(self, message, key=0):
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('decrypt')

if __name__ == '__main__':
    cipher = Caesar()
    print('Choose 1 or 2.')
    question = int(input('Do you want to [1]encrypt or [2]decrypt a Caeser Cipher? '))
    key1 = int(input('How many spaces do you want the letters shifted? '))
    if question == 1:
        secret_message = str(input('What is your secret message you want encrypted? '))
        # Takes your message and applies the caeser cipher to it. 
        print(cipher.encrypt(message=secret_message, key=key1))
    elif question == 2:
        # put the encrypted message into a variable. If you want to 
        encrypted_message = str(input('What is your secret message you want decrypted? '))
        # encrypted_message = cipher.encrypt(message=secret_message, key=1)
        print(cipher.decrypt(message=encrypted_message, key=key1))
    else:
        print('Invalid Input')
    #'FRPERG ZRFFNTR.'