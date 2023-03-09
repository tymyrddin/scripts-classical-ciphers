# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions Python
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html

CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    # Get and parse the arguments
    options = get_args()

    # Stores the encrypted/decrypted form of the message:
    translated = ""

    if options.mode == "encrypt":
        translated = encrypt_message(options.key, options.text)
    elif options.mode == "decrypt":
        translated = decrypt_message(options.key, options.text)

    print("%sed message:" % (options.mode.title()))
    print(translated)


def get_args():
    parser = argparse.ArgumentParser(
        description="Vigenere Cipher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            vigenere_cipher.py -t sometext
            vigenere_cipher.py -t sometext -k "ASIMOV" -m encrypt
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--text",
        default=(
            "Alan Mathison Turing was a British mathematician, logician,"
            " cryptanalyst, and computer scientist."
        ),
        help="Message to encrypt or decrypt",
    )
    parser.add_argument(
        "-k",
        "--key",
        default="ASIMOV",
        help="String",
    )
    parser.add_argument(
        "-m",
        "--mode",
        default="encrypt",
        choices=["encrypt", "decrypt"],
        help="encrypt or decrypt",
    )
    values = parser.parse_args()
    return values


def encrypt_message(key, message):
    return translate_message(key, message, "encrypt")


def decrypt_message(key, message):
    return translate_message(key, message, "decrypt")


def translate_message(key, message, mode):
    translated = []  # Stores the encrypted/decrypted message string.

    key_index = 0
    key = key.upper()

    for symbol in message:  # Loop through each symbol in message.
        num = CAPITAL_LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in CAPITAL_LETTERS.
            if mode == "encrypt":
                num += CAPITAL_LETTERS.find(key[key_index])  # Add if encrypting.
            elif mode == "decrypt":
                num -= CAPITAL_LETTERS.find(key[key_index])  # Subtract if decrypting.

            num %= len(CAPITAL_LETTERS)  # Handle any wraparound.

            # Add the encrypted/decrypted symbol to the end of translated:
            if symbol.isupper():
                translated.append(CAPITAL_LETTERS[num])
            elif symbol.islower():
                translated.append(CAPITAL_LETTERS[num].lower())

            key_index += 1  # Move to the next letter in the key.
            if key_index == len(key):
                key_index = 0
        else:
            # Append the symbol without encrypting/decrypting.
            translated.append(symbol)

    return "".join(translated)


# If vigenere_cipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main()
