import sys
import re

#create key same length as message in cases of different lengths
def create_key(message, key):
    key = list(key)
    key_len = len(key)
    message_len = len(message)

    if message_len == key_len:
        return key
    else:
        for i in range(message_len - key_len):
            key.append(key[i % key_len])
    return "".join(key)

def encrypt(message, key):
    cipher = []
    message_len = len(message)
    key = create_key(message, key)

    #encrypt message through vigenere cypher using ascii values
    for i in range(message_len):
        char = message[i]
        if char.isupper():
            cipher_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            cipher_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            cipher_char = char
        cipher.append(cipher_char)

    return "".join(cipher)

#decrypt message through vigenere cypher using ascii values
def decrypt(message, key):
    cipher = []
    message_len = len(message)
    key = create_key(message, key)

    for i in range(message_len):
        char = message[i]
        if char.isupper():
            cipher_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            cipher_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            cipher_char = char
        cipher.append(cipher_char)

    return "".join(cipher)

def main():
    key = ''

    while True:
        message = input()

        #seperate action from message
        tokenized_message = re.split(r'(\s+)', message)
        command = tokenized_message[0]
        tokenized_message.remove(command)
        message = "".join(tokenized_message).strip()
        
        #accept actions
        if command.lower() == 'quit':
            sys.exit()
        elif command.lower() == 'passkey':
            key = message
            print('RESULT')
        elif command.lower() == 'encrypt':
            if key == '':
                print('ERROR No passkey')
            else:
                print(f"RESULT {encrypt(message, key)}")
        elif command.lower() == 'decrypt':
            if key == '':
                print('ERROR No passkey')
            else:
                print(f"RESULT {decrypt(message, key)}")
        else:
            print('ERROR Unknown message')

if __name__ == "__main__":
    main()