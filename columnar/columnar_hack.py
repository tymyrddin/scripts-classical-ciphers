# Columnar transposition cipher hack
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html

import columnar_decrypt
import detect_english


def main():
    # Get and parse the arguments
    options = get_args()

    hacked_message = hack_transposition(options.text)

    if hacked_message is None:
        print("Failed to hack encryption.")
    else:
        print(hacked_message)


def get_args():
    parser = argparse.ArgumentParser(
        description="Columnar transposition cipher hack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            columnar_hack.py -t [message]
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--text",
        default="Trheits  tiesx ta. sec",
        help="Message to hack",
    )
    values = parser.parse_args()
    return values


def hack_transposition(message):
    print("Hacking...")

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print("(Press Ctrl-C or Ctrl-D to quit at any time.)")

    # Brute-force by looping through every possible key.
    for key in range(1, len(message)):
        print("Trying key #%s..." % key)

        decrypted_text = columnar_decrypt.decrypt_message(key, message)

        if detect_english.is_english(decrypted_text):
            # Ask user if this is the correct decryption.
            print()
            print("Possible encryption hack:")
            print("Key %s: %s" % (key, decrypted_text[:100]))
            print()
            print("Enter D if done, anything else to continue hacking:")
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return decrypted_text

    return None


if __name__ == "__main__":
    main()
