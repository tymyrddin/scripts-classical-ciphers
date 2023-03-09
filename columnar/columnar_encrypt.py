# Columnar transposition cipher encryption
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html


def main():
    # Get and parse the arguments
    options = get_args()

    ciphertext = encrypt_message(options.key, options.text)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + "|")


def get_args():
    parser = argparse.ArgumentParser(
        description="Columnar transposition cipher encryption",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            columnar_encrypt.py -t sometext
            columnar_encrypt.py -t sometext -k 13
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--text",
        default="This is a secret text.",
        help="Message to encrypt",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=int,
        default=13,
        help="Key (Number)",
    )
    values = parser.parse_args()
    return values


def encrypt_message(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [""] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        current_index = column

        # Keep looping until current_index goes past the message length.
        while current_index < len(message):
            # Place the character at current_index in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[current_index]

            # move current_index over
            current_index += key

    # Convert the ciphertext list into a single string value and return it.
    return "".join(ciphertext)


# If columnar_encrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main()
