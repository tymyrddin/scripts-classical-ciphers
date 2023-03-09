# Rail fence transposition cipher decryption
# https://en.wikipedia.org/wiki/Rail_fence_cipher
# Generates a template based on the key and fills it in with
# the characters of the ciphertext and then reading it in
# a zigzag formation.

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html


def main():
    # Get and parse the arguments
    options = get_args()

    plaintext = decrypt_message(options.ciphertext, options.key)

    # Print the decrypted string in plaintext to the screen.
    print("Plaintext: \n")
    print(plaintext)


def get_args():
    parser = argparse.ArgumentParser(
        description="Rail fence transposition cipher decryption",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            railfence_decrypt.py -t ciphertext
            railfence_decrypt.py -t ciphertext -k 4
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--ciphertext",
        default="Tscehi ertxi ase ts t.",
        help="Ciphertext to decrypt",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=int,
        default=4,
        help="Number of layers",
    )
    values = parser.parse_args()
    return values


def decrypt_message(message: str, key: int) -> str:
    grid = []
    lowest = key - 1

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1:
        return message

    # Generate template
    temp_grid: list[list[str]] = [[] for _ in range(key)]
    for position in range(len(message)):
        # Put it in bounds
        num = position % (lowest * 2)
        # Create zigzag pattern
        num = min(num, lowest * 2 - num)
        temp_grid[num].append("*")

    counter = 0
    # Fill in the characters
    for row in temp_grid:
        splice = message[counter : counter + len(row)]
        grid.append(list(splice))
        counter += len(row)

    # Read as zigzag
    translated = ""
    for position in range(len(message)):
        num = position % (lowest * 2)  # puts it in bounds
        num = min(num, lowest * 2 - num)  # creates zigzag pattern
        translated += grid[num][0]
        grid[num].pop(0)
    return translated


# If railfence_decrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main()
