def caesar_cipher(text, key1, key2, mode):
    if key1 < 1 or key1 > 25:
        print("Key 1 must be between 1 and 25.")
        return ""

    if len(key2) < 7 or not key2.isalpha():
        print("Key 2 must contain only Latin alphabet letters and have a length of at least 7 characters.")
        return ""

    # English alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Remove spaces and convert the text to uppercase
    text = text.replace(" ", "").upper()

    result = ""
    key2_index = 0
    for char in text:
        if 'A' <= char <= 'Z':
            if mode == 'encryption':
                index1 = (alphabet.index(char) + key1) % 26
                index2 = (alphabet.index(key2[key2_index].upper())) % 26
                encrypted_char = alphabet[(index1 + index2) % 26]
                key2_index = (key2_index + 1) % len(key2)
                result += encrypted_char
            else:
                index1 = (alphabet.index(char) - key1) % 26
                index2 = (alphabet.index(key2[key2_index].upper())) % 26
                decrypted_char = alphabet[(index1 - index2) % 26]
                key2_index = (key2_index + 1) % len(key2)
                result += decrypted_char
        else:
            print(f"Character '{char}' is invalid. Only letters A-Z are allowed.")
            return ""

    return result

# User input
mode = input("Enter the mode (encryption/decryption): ").lower()
key1 = int(input("Enter the first key (1-25): "))
key2 = input("Enter the second key (at least 7 Latin letters): ")
message = input("Enter the message or ciphertext: ")

# Perform encryption or decryption based on the selected mode
if mode == 'encryption':
    result = caesar_cipher(message, key1, key2, 'encryption')
    print("Encrypted message:", result)
elif mode == 'decryption':
    result = caesar_cipher(message, key1, key2, 'decryption')
    print("Decrypted message:", result)
else:
    print("Invalid mode. Please enter 'encryption' or 'decryption'.")
