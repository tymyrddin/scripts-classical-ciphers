# Columnar transposition cipher encrypt/decrypt file
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html
import time

import columnar_decrypt
import columnar_encrypt


def main():
    # Get and parse the arguments
    options = get_args()

    input_file = open(options.input_filename.name)
    content = input_file.read()
    input_file.close()

    translated = ""

    print("%sing..." % (options.mode.title()))

    # Measure how long the encryption/decryption takes:
    start_time = time.time()
    if options.mode == "encrypt":
        translated = columnar_encrypt.encrypt_message(options.key, content)
    elif options.mode == "decrypt":
        translated = columnar_decrypt.decrypt_message(options.key, content)
    total_time = round(time.time() - start_time, 2)
    print("%sion time: %s seconds" % (options.mode.title(), total_time))

    print("Writing translated text to %s." % options.output_filename.name)

    # Write out the translated message to the output file:
    output_file = open(options.output_filename.name, "w")
    output_file.write(translated)
    output_file.close()

    print(
        "Done %sing %s (%s characters)."
        % (options.mode, options.input_filename.name, len(content))
    )
    print("%sed file is %s." % (options.mode.title(), options.output_filename.name))


def get_args():
    parser = argparse.ArgumentParser(
        description="Columnar transposition cipher encrypt/decrypt file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            columnar_file_cipher.py -i file1.txt -o file2.txt -k 13 -m encrypt
        """
        ),
    )
    parser.add_argument(
        "-i",
        "--input_filename",
        action="store",
        dest="input_filename",
        default="frankenstein.txt",
        type=argparse.FileType("r"),
        help="Takes input from a file name of your choice",
    )
    parser.add_argument(
        "-o",
        "--output_filename",
        action="store",
        dest="output_filename",
        default="frankenstein_encrypted.txt",
        type=argparse.FileType("w"),
        help="Directs the output to a name of your choice",
    )
    parser.add_argument(
        "-k",
        "--key",
        type=int,
        default=13,
        help="Key (Number)",
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


# If columnar_file_cipher.py is run (instead of imported as a module)
# call the main() function.
if __name__ == "__main__":
    main()
