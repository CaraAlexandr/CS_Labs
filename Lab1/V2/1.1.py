def caesar_cipher(text, key, mode):
    if key < 1 or key > 25:
        print("The key must be between 1 and 25.")
        return ""

    # English alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Remove spaces and convert the text to uppercase
    text = text.replace(" ", "").upper()

    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            if mode == 'encryption':
                index = (alphabet.index(char) + key) % 26
            else:
                index = (alphabet.index(char) - key) % 26
            result += alphabet[index]
        else:
            print(f"Character '{char}' is invalid. Only letters A-Z are allowed.")
            return ""

    return result

# User input
mode = input("Enter the mode (encryption/decryption): ").lower()
key = int(input("Enter the key (1-25): "))
message = input("Enter the message or ciphertext: ")

# Perform encryption or decryption based on the selected mode
if mode == 'encryption':
    result = caesar_cipher(message, key, 'encryption')
    print("Encrypted message:", result)
elif mode == 'decryption':
    result = caesar_cipher(message, key, 'decryption')
    print("Decrypted message:", result)
else:
    print("Invalid mode. Please enter 'encryption' or 'decryption'.")
