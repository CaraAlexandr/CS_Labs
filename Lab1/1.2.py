def caesar_cipher(text, key1, key2, operation):
    result = []

    # Check if key2 contains only letters of the Latin alphabet and has length >= 7
    if not (key2.isalpha() and len(key2) >= 7):
        return "Invalid key 2. Key 2 must contain only Latin alphabet letters and have a length of at least 7."

    key2 = key2.upper()  # Convert key2 to uppercase

    for char in text:
        if 'A' <= char <= 'Z':
            base = ord('A')
        elif 'a' <= char <= 'z':
            base = ord('a')
        else:
            return "Invalid input. Only alphabetic characters are allowed."

        if operation == 'encrypt':
            shift = (ord(key2[len(result) % len(key2)]) - base) % 26  # Vary key2 for each character
            new_char = chr((ord(char) - base + key1 + shift) % 26 + base)
        elif operation == 'decrypt':
            shift = (ord(key2[len(result) % len(key2)]) - base) % 26  # Vary key2 for each character
            new_char = chr((ord(char) - base - key1 - shift) % 26 + base)
        else:
            return "Invalid operation. Choose 'encrypt' or 'decrypt'."

        result.append(new_char)

    return ''.join(result)


def main():
    operation = input("Choose operation (encrypt/decrypt): ").lower()
    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Choose 'encrypt' or 'decrypt'.")
        return

    key1 = int(input("Enter key 1 (1-25 inclusive): "))
    if not (1 <= key1 <= 25):
        print("Invalid key 1. Key 1 must be between 1 and 25 inclusive.")
        return

    key2 = input("Enter key 2 (must contain only Latin alphabet letters and have length >= 7): ")

    text = input("Enter the message or cryptogram: ").replace(" ", "").upper()

    result = caesar_cipher(text, key1, key2, operation)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
