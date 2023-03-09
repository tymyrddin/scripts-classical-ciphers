# Vigenere File Hack
# Wrapper to use files for bruteforce hack

import argparse  # https://docs.python.org/3/library/argparse.html
import textwrap  # https://docs.python.org/3/library/textwrap.html

import vigenere_hack


def main():
    # Get and parse the arguments
    options = get_args()

    input_file = open(options.input_filename.name)
    ciphertext = input_file.read()
    input_file.close()

    try:
        hacked_message = vigenere_hack.hack_vigenere(ciphertext)
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
        description="Vigenere File Hack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            vigenere_file_hack.py -i input_filename.txt -o output_filename.txt
        """
        ),
    )
    parser.add_argument(
        "-i",
        "--input_filename",
        action="store",
        dest="input_filename",
        type=argparse.FileType("r"),
        help="Takes input from a file name of your choice",
    )
    parser.add_argument(
        "-o",
        "--output_filename",
        action="store",
        dest="output_filename",
        type=argparse.FileType("w"),
        help="Directs the output to a name of your choice",
    )
    values = parser.parse_args()
    return values


# main() function.
if __name__ == "__main__":
    main()
