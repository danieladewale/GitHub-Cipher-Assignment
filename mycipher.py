import sys

def caesar_cipher(input_string, shift):
    output_string = ""

    for char in input_string:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            output_string += chr((ord(char) - start + shift) % 26 + start)

    return output_string

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <shift_amount>")
        sys.exit(1)

    try:
        shift_amount = int(sys.argv[1]) % 26
    except ValueError:
        print("Shift amount must be an integer.")
        sys.exit(1)

    message = raw_input("").upper()

    encoded_message = ""
    block_count = 0
    blocks_per_line = 10
    for char in message:
        if char.isalpha():
            encoded_message += caesar_cipher(char, shift_amount)
            if len(encoded_message) % 5 == 0:
                print(encoded_message),
                block_count += 1
                if block_count % blocks_per_line == 0:
                    print("")
                encoded_message = ''

    if encoded_message:
        print(encoded_message)