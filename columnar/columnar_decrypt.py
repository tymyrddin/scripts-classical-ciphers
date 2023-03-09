# Columnar transposition cipher decryption
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import math
import textwrap  # https://docs.python.org/3/library/textwrap.html


def main():
    # Get and parse the arguments
    options = get_args()

    plaintext = decrypt_message(options.key, options.text)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + "|")


def get_args():
    parser = argparse.ArgumentParser(
        description="Columnar transposition cipher decryption",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            columnar_decrypt.py -t sometext
            columnar_decrypt.py -t sometext -k 13
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--text",
        default="Trheits  tiesx ta. sec",
        help="Message to decrypt",
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


def decrypt_message(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    number_of_columns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
    number_of_rows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    number_of_shaded_boxes = (number_of_columns * number_of_rows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [""] * number_of_columns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1  # Point to next column.

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == number_of_columns) or (
            column == number_of_columns - 1
            and row >= number_of_rows - number_of_shaded_boxes
        ):
            column = 0
            row += 1

    return "".join(plaintext)


# If columnar_decrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main()
