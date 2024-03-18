# The Vigenère cipher, where the offset for each letter is determined by another text, called the key.

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        #Append any non-letter character to the message
        if not char.isalpha():
            final_message += char

        else:
            #Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            #Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            
            index = alphabet.find(char)
            
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
        
    return final_message
    
def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

# Asking for encryption or decryption
def main():
    
    choice = input("\nDo you want to encrypt or decrypt the text message?  ")

    if choice == 'encrypt':
        text = input("\nEnter the message to encrypt:  ")
        key = input("What is the key:  ")
        print("\nThe encrypted message is :  ", encrypt(text, key))

    elif choice == 'decrypt':
        text = input("\nEnter the text to decrypt:  ")
        key = input("What is the key:  ")
        print("\nThe decrypted message is :  ", decrypt(text, key))

    else:
        print("\nEnter properly (encrypt or decrypt)")
        main()

print("<<<<<  Welcome to Vigenere Cipher / Decipher >>>>>")
main()