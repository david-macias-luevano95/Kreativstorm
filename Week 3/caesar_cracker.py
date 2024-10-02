'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''


def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            if encrypt:
                result += chr((ord(char) - offset + shift) % 26 + offset)
            else:
                result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

def brute_force_caesar_cipher(text):
    print("Brute-Force Decryption Results:")
    for key in range(26):
        decrypted_text = caesar_cipher(text, key, encrypt=False)
        print(f"Key {key}: {decrypted_text}")

def main():
    while True:
        choice = input("Choose an operation: (e)ncrypt, (d)ecrypt, or (b)rute-force decrypt?\n> ").lower()
        if choice not in ('e', 'd', 'b'):
            print("Invalid choice. Please enter 'e' for encrypt, 'd' for decrypt, or 'b' for brute-force decryption.")
            continue

        if choice == 'b':
            encrypted_text = input("Enter the text to brute-force decrypt.\n> ")
            brute_force_caesar_cipher(encrypted_text)
        else:
            key = int(input("Please enter the Caesar cipher key (0 to 25).\n> "))
            if not 0 <= key <= 25:
                print("Invalid key. Please enter a key between 0 and 25.")
                continue

            input_text = input("Enter the text to {}.\n> ".format("encrypt" if choice == 'e' else "decrypt"))

            if choice == 'e':
                encrypted_text = caesar_cipher(input_text, key)
                print(encrypted_text)
            else:
                decrypted_text = caesar_cipher(input_text, key, encrypt=False)
                print(decrypted_text)

        another_operation = input("Do you want to perform another operation? (yes/no)\n> ").lower()
        if another_operation != 'yes':
            break

if __name__ == "__main__":
    main()
