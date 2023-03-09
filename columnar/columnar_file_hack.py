# Columnar transposition hack file
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import sys
import textwrap  # https://docs.python.org/3/library/textwrap.html
import time

import columnar_decrypt
import detect_english


def main():
    # Get and parse the arguments
    options = get_args()

    input_file = open(options.input_filename.name)
    ciphertext = input_file.read()
    input_file.close()

    try:
        hacked_message = hack_transposition(ciphertext)
        if hacked_message is not None:
            print("Writing decrypted text to %s." % options.output_filename.name)

            output_file = open(options.output_filename.name, "w")
            output_file.write(hacked_message)
            output_file.close()
        else:
            print("Failed to hack encryption.")
    except KeyboardInterrupt:
        print("\n[+] Detected CTRL+C ... ")
        print("[+] Done")


def get_args():
    parser = argparse.ArgumentParser(
        description="Columnar transposition hack file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            columnar_file_hack.py -i input_filename.txt -o output_filename.txt
        """
        ),
    )
    parser.add_argument(
        "-i",
        "--input_filename",
        action="store",
        dest="input_filename",
        default="frankenstein_encrypted.txt",
        type=argparse.FileType("r"),
        help="Takes input from a file name of your choice",
    )
    parser.add_argument(
        "-o",
        "--output_filename",
        action="store",
        dest="output_filename",
        default="frankenstein2.txt",
        type=argparse.FileType("w"),
        help="Directs the output to a name of your choice",
    )
    values = parser.parse_args()
    return values


# The hack_transposition() function's code was copy/pasted from
# columnar_hack.py and had some modifications made.
def hack_transposition(message):
    print("Hacking...")
    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print("(Press Ctrl-C or Ctrl-D to quit at any time.)")

    for key in range(1, len(message)):
        print("Trying key #%s... " % key, end="")
        sys.stdout.flush()

        # We want to track the amount of time it takes to test a single key,
        # so we record the time in start_time.
        start_time = time.time()

        decrypted_text = columnar_decrypt.decrypt_message(key, message)
        english_percentage = round(
            detect_english.get_english_count(decrypted_text) * 100, 2
        )

        total_time = round(time.time() - start_time, 3)
        print("Test time: %s seconds, " % total_time, end="")
        sys.stdout.flush()  # Flush printed text to the screen.

        print("Percent English: %s%%" % english_percentage)
        if english_percentage > 20:
            print()
            print("Key " + str(key) + ": " + decrypted_text[:100])
            print()
            print("Enter D if done, anything else to continue hacking:")
            response = input("> ")
            if response.strip().upper().startswith("D"):
                return decrypted_text
    return None


# If columnar_file_hack.py is run (instead of imported as a module)
# call the main() function.
if __name__ == "__main__":
    main()
