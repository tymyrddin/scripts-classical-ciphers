# Rail fence transposition cipher encryption
# https://en.wikipedia.org/wiki/Rail_fence_cipher
# Shuffles the characters of a plaintext by placing each of them
# in a grid (height of grid is dependent on the key) in a zigzag
# formation, then reading it left to right.

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html


def main():
    # Get and parse the arguments
    options = get_args()

    ciphertext = encrypt_message(options.plaintext, options.key)

    # Print the encrypted string in ciphertext to the screen.
    print("Ciphertext: \n")
    print(ciphertext)


def get_args():
    parser = argparse.ArgumentParser(
        description="Rail fence transposition cipher encryption",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            railfence_encrypt.py -t plaintext
            railfence_encrypt.py -t plaintext -k 4
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--plaintext",
        default="This is a secret text.",
        help="Plaintext to encrypt",
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


def encrypt_message(message: str, key: int):
    temp_grid: list[list[str]] = [[] for _ in range(key)]
    lowest = key - 1

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1 or len(message) <= key:
        return message

    for position, character in enumerate(message):
        # Puts it in bounds
        num = position % (lowest * 2)
        # Create zigzag pattern
        num = min(num, lowest * 2 - num)
        temp_grid[num].append(character)
    grid = ["".join(row) for row in temp_grid]
    translated = "".join(grid)

    return translated


# If railfence_encrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main()
