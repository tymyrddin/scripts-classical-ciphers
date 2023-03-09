# Rail fence transposition cipher hack
# Uses decrypt function by guessing every key

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html

import railfence_decrypt


def main():
    # Get and parse the arguments
    options = get_args()

    hacked_message = bruteforce(options.ciphertext)

    if hacked_message is None:
        print("Failed to hack encryption.")
    else:
        for key in range(1, len(hacked_message)):
            print("Key #%s: %s" % (key, hacked_message[key - 1]))


def get_args():
    parser = argparse.ArgumentParser(
        description="Rail fence transposition cipher hack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            railfence_hack.py -t [message]
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--ciphertext",
        default="Tscehi ertxi ase ts t.",
        help="Ciphertext to hack",
    )
    values = parser.parse_args()
    return values


def bruteforce(message: str) -> dict[int, str]:
    translations = []
    # Try every key
    for key in range(1, len(message)):
        translated = railfence_decrypt.decrypt_message(message, key)

        translations.append(translated)
    return translations


if __name__ == "__main__":
    main()
