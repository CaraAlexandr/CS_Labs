def format_input(text):
    alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSŞTŢUVWXYZ"
    text = text.upper().replace(" ", "")
    for c in text:
        if c not in alphabet:
            print(f"Invalid character {c}. Please use characters from the Romanian alphabet or placeholders 0-4.")
            return None
    return text


def create_matrix(key):
    matrix = [[None for _ in range(6)] for _ in range(6)]
    alphabet = list("AĂÂBCDEFGHIÎKLMNOPQRSŞTŢUVWXYZ")

    # Remove characters from the alphabet that are in the key
    for char in key:
        if char in alphabet:
            alphabet.remove(char)

    x, y = 0, 0
    for char in key + ''.join(alphabet):
        matrix[x][y] = char
        y += 1
        if y == 6:
            y = 0
            x += 1
            if x == 6:
                break

    return matrix


def find_position(matrix, char):
    for x in range(6):
        for y in range(6):
            if matrix[x][y] == char:
                return x, y
    return None


def playfair(key, text, mode):
    if len(key) < 7:
        print("Key length must be at least 7 characters.")
        return

    matrix = create_matrix(key)
    if len(text) % 2 != 0:
        text += "X"

    processed_text = ""
    i = 0
    while i < len(text):
        x1, y1 = find_position(matrix, text[i])
        x2, y2 = find_position(matrix, text[i + 1])

        if x1 == x2:  # Same row
            if mode == "encrypt":
                processed_text += matrix[x1][(y1 + 1) % 6] + matrix[x2][(y2 + 1) % 6]
            else:
                processed_text += matrix[x1][(y1 - 1) % 6] + matrix[x2][(y2 - 1) % 6]
        elif y1 == y2:  # Same column
            if mode == "encrypt":
                processed_text += matrix[(x1 + 1) % 6][y1] + matrix[(x2 + 1) % 6][y2]
            else:
                processed_text += matrix[(x1 - 1) % 6][y1] + matrix[(x2 - 1) % 6][y2]
        else:
            processed_text += matrix[x1][y2] + matrix[x2][y1]

        i += 2

    if mode == "decrypt" and processed_text[-1] == "X":
        processed_text = processed_text[:-1]

    return processed_text

def print_matrix(matrix):
    print("Playfair Matrix:")
    for row in matrix:
        if None in row:
            break
        print(" ".join(row))


def main():
    mode = input("Choose operation (encrypt/decrypt): ").strip().lower()

    key = format_input(input("Enter the key (at least 7 characters long): "))
    if not key:
        return

    if mode == "encrypt":
        plaintext = format_input(input("Enter the plaintext: "))
        if not plaintext:
            return
        encrypted_text = playfair(key, plaintext, "encrypt")
        print_matrix(create_matrix(key))
        print(f"Encrypted text: {encrypted_text}")
    elif mode == "decrypt":
        cryptogram = format_input(input("Enter the cryptogram: "))
        if not cryptogram:
            return
        decrypted_text = playfair(key, cryptogram, "decrypt")
        print_matrix(create_matrix(key))
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
