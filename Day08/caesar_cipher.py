# Day 8 | Caesar Cypher - Function Parameters

from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    shifted_position = 0
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
                if shifted_position > 0:
                    shifted_position -= 26
            elif encode_or_decode == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
                if shifted_position < 0:
                    shifted_position += 26

            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

cypher_running = True

while cypher_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if again == "no":
        cypher_running = False
        print("Goodbye.")
