# Caesar Cipher 26 Hack
# Adapted from Caesar Cipher 65 Hack

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html

SYMBOLS = "abcdefghijklmnopqrstuvwxyz"


def main():
    # Get and parse the arguments
    options = get_args()

    texts = hack_message(options.text.lower())

    # Print the keys with translated strings:
    for shift in range(len(SYMBOLS)):
        print("Key #%s: %s" % (shift, texts[shift]))


def get_args():
    parser = argparse.ArgumentParser(
        description="Caesar Cipher 26 Hack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            caesar_hack26.py -t [message]
        """
        ),
    )
    parser.add_argument(
        "-t",
        "--text",
        default="guvf vf zl frperg zrffntr.",
        help="Message to hack",
    )
    values = parser.parse_args()
    return values


def hack_message(message):
    translations = []

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ""

        # The rest of the program is almost the same as the original program:
        # Loop through each symbol in `message`:
        for symbol in message:
            if symbol in SYMBOLS:
                symbol_index = SYMBOLS.find(symbol)
                translated_index = symbol_index - key

                # Handle the wrap-around:
                if translated_index < 0:
                    translated_index = translated_index + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translated_index]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        translations.append(translated)
    return translations


# If caesar_hack65.py is run (instead of imported as a module), call
# the hack() function from here and print the results.
if __name__ == "__main__":
    main()
