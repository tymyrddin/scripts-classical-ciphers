# Caesar Cipher 65
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted:
# - improved compliance with PEPs
# - naming conventions
# - refactored translation code into a function
# - added user defined input with argparse
# - added "__main__"
# - factored mode out of the loop
# - added encrypt_message and decrypt_message for use as module

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html

# Every possible symbol that can be encrypted:
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."


def main():
    # Get and parse the arguments
    options = get_args()

    # Stores the encrypted/decrypted form of the message:
    translated = ""

    if options.mode == "encrypt":
        translated = encrypt_message(options.shift, options.text)
    elif options.mode == "decrypt":
        translated = decrypt_message(options.shift, options.text)

    # Print the translated string:
    print("%sed message:" % (options.mode.title()))
    print(translated)


def get_args():
    parser = argparse.ArgumentParser(
        description="Caesar Cipher 65",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            caesar_cipher65.py -t [text]
            caesar_cipher65.py -t [text] -s 3             # shift 3 places
            caesar_cipher65.py -t [text] -s 3 -m decrypt  # decrypt
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--text",
        default="This is my secret message.",
        help="Message to encrypt or decrypt",
    )
    parser.add_argument(
        "-s",
        "--shift",
        type=int,
        default=13,
        help="Shift/Key (Number), may be negative",
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
    # Stores the encrypted/decrypted form of the message:
    translated = ""

    # Reverse for decrypt:
    if mode == "decrypt":
        key = -key

    for symbol in message:
        # Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = symbol_index + key

            # Handle wrap-around, if needed:
            if translated_index >= len(SYMBOLS):
                translated_index = translated_index - len(SYMBOLS)
            elif translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)

            translated = translated + SYMBOLS[translated_index]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    return translated


# If caesar_cipher65.py is run (instead of imported as a module), call main().
if __name__ == "__main__":
    main()
