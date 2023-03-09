# Vigenere Cipher Dictionary Hack
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions Python
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html

import detect_english
import vigenere_cipher


def main():
    # Get and parse the arguments
    options = get_args()

    hacked_message = hack_vigenere_dictionary(options.ciphertext)

    if hacked_message is not None:
        print(hacked_message)
    else:
        print("Failed to hack encryption.")


def get_args():
    parser = argparse.ArgumentParser(
        description="Vigenere Dictionary Hack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            vigenere_dictionary_hack.py -c [ciphertext]
        """
        ),
    )
    parser.add_argument(
        "-c",
        "--ciphertext",
        default="Tzx isnz eccjxkg nfq lol mys bbqq I lxcz.",
        help="Ciphertext to hack",
    )
    values = parser.parse_args()
    return values


def hack_vigenere_dictionary(ciphertext):
    fo = open("dictionary.txt")
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip()  # Remove the newline at the end.
        decrypted_text = vigenere_cipher.decrypt_message(word, ciphertext)
        if detect_english.is_english(decrypted_text, word_percentage=40):
            # Check with user to see if the decrypted key has been found:
            print()
            print("Possible encryption break:")
            print("Key " + str(word) + ": " + decrypted_text[:100])
            print()
            print("Enter D for done, or just press Enter to continue breaking:")
            response = input("> ")

            if response.upper().startswith("D"):
                return decrypted_text


if __name__ == "__main__":
    main()
