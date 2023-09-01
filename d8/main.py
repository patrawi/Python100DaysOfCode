"""caesar-cipher"""
from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

def caesar(start_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for e in start_text:
        cipher_char = ''
        if e in alphabet:
            cipher_char = (alphabet.index(e) + shift_amount) % 26
            cipher_text += alphabet[cipher_char]
        else:
            cipher_text += e
    return cipher_text



def main():
    print(logo)
    continue_program = True
    while continue_program:
        method = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
        message = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        result = caesar(message, shift, method)
        print(f'Here is your result {result}')
        repeat = input(
            "Type 'yes' if you want to go again. Otherwise type 'no': \n"
        ).lower()
        if repeat == "no":
            continue_program = False
            return


if __name__ == "__main__":
    main()
