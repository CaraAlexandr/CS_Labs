def caesar_cipher(text, key, operation):
    result = []

    for char in text:
        if 'A' <= char <= 'Z':
            base = ord('A')
        elif 'a' <= char <= 'z':
            base = ord('a')
        else:
            return "Invalid input. Only alphabetic characters are allowed."

        if operation == 'encrypt':
            new_char = chr((ord(char) - base + key) % 26 + base)
        elif operation == 'decrypt':
            new_char = chr((ord(char) - base - key) % 26 + base)
        else:
            return "Invalid operation. Choose 'encrypt' or 'decrypt'."

        result.append(new_char)

    return ''.join(result)


def main():
    operation = input("Choose operation (encrypt/decrypt): ").lower()
    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Choose 'encrypt' or 'decrypt'.")
        return

    key = int(input("Enter the key (1-25 inclusive): "))
    if not (1 <= key <= 25):
        print("Invalid key. Key must be between 1 and 25 inclusive.")
        return

    text = input("Enter the message or cryptogram: ").replace(" ", "").upper()

    result = caesar_cipher(text, key, operation)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
