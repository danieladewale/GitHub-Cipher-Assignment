import sys

def caesar_cipher(input_string, shift):
    output_string = ""
    block_size = 5
    count = 0

    for char in input_string:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start).upper()

            output_string += new_char
            count += 1

            if count == block_size:
                output_string += ' '
                count = 0

    return output_string.strip()

if len(sys.argv) != 2:
    print("Usage: python mycipher.py <shift>".upper())
    sys.exit(1)

shift = int(sys.argv[1]) % 26

message = sys.stdin.read().rstrip()

encrypted_message = caesar_cipher(message, shift)

print(encrypted_message)