# Report: Caesar Cipher Implementation

## Subject: Caesar Cipher

### Task 1
#### Implementation of Caesar Algorithm for Single Key

The Caesar cipher is a simple encryption technique for the English alphabet. In this task, we implemented the Caesar algorithm using Python while adhering to specific constraints:

- We used only letter encodings, not relying on programming language-specific encodings like ASCII or Unicode.
- Key values were limited to the range of 1 to 25, and no other values were allowed.
- Text characters were restricted to 'A' to 'Z' and 'a' to 'z,' excluding any other characters.
- User input validation was implemented to ensure the correctness of the input.

We provided the following functionality:

- Transformation of the input text to uppercase and removal of spaces.
- Option for the user to choose between encryption and decryption.
- Input of the key and message or cryptogram.
- Display of the encrypted or decrypted result.

#### Code Implementation
```python
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
```

#### Example
![Task 1 encrypt](Img/1.1encrypt.png)

![Task 1 decrypt](Img/1.1decrypt.png)


### Task 2
#### Implementation of Caesar Algorithm with Two Keys

In this task, we extended the Caesar cipher algorithm to use two keys while preserving the conditions specified in Task 1. Additionally, key 2 was required to meet the following conditions:

- Key 2 should contain only letters of the Latin alphabet.
- Key 2 must have a length of at least 7 characters.

We provided the following functionality:

- Variation of key 2 for each character in the text.
- Implementation of user input validation for key 2.

#### Code Implementation
```python
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
```
#### Example
![Task 2 encrypt](Img/1.2encrypt.png)

![Task 2 decrypt](Img/1.2decrypt.png)

### Conclusion

In conclusion, this report outlined the implementation of the Caesar cipher algorithm with both single and double keys in Python. The Caesar cipher is a straightforward encryption method for the English alphabet. While the version with two keys may not seem significantly more complex, it significantly reduces the likelihood of decryption through brute force. This dual-key approach increases the computational complexity required to crack the cipher, making it more secure compared to the single-key version.