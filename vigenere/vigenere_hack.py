# Vigenere Cipher Hack
# Adopted from https://www.nostarch.com/crackingcodes (BSD Licensed)
# and adapted
# - improved compliance with PEPs
# - naming conventions Python
# - removed pyperclip
# - added user defined input with argparse

import argparse  # https://docs.python.org/3/library/argparse.html
import itertools
import re
import textwrap  # https://docs.python.org/3/library/textwrap.html

import detect_english
import frequency_analysis
import vigenere_cipher

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SILENT_MODE = False  # If set to True, program doesn't print anything.
NUM_MOST_FREQ_LETTERS = 4  # Attempt this many letters per subkey.
MAX_KEY_LENGTH = 16  # Will not attempt keys longer than this.
NONLETTERS_PATTERN = re.compile("[^A-Z]")


def main():
    # Get and parse the arguments
    options = get_args()

    # Try
    hacked_message = hack_vigenere(options.ciphertext)

    if hacked_message is not None:
        print("Plaintext: \n")
        print(hacked_message)
    else:
        print("Failed to hack encryption.")


def get_args():
    parser = argparse.ArgumentParser(
        description="Vigenere Hack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
            vigenere_hack.py -c [ciphertext]
        """
        ),
    )
    parser.add_argument(
        "-c",
        "--ciphertext",
        default=(
            "Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf,"
            " kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad"
            " qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i"
            " rcmmstugvtawz ca tzm ocicwxfg jf 'stscmilpy' oid 'uwydptsbuci'"
            " wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm"
            " roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo"
            " Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm"
            " Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm."
            " Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr"
            " Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg"
            " aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm,"
            " mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw"
            " Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl"
            " Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a"
            " kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf"
            " Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq"
            " onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid"
            " tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab"
            " ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu"
            " xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz,"
            " kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk"
            " fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn"
            " wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh"
            " rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba"
            " dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id"
            " tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds"
            " vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc"
            " wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt"
            " uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog"
            " pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd 'hce"
            " sxboglavs kvy zm ion tjmmhzd.' Sa at Haq 2012 i bfdvsbq azmtmd'g"
            " widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a"
            " kbmhptgzk dvrvwz wa efiohzd."
        ),
        help="Ciphertext to hack",
    )
    values = parser.parse_args()
    return values


def find_repeat_sequences_spacings(message):
    # Goes through the message and finds any 3 to 5 letter sequences
    # that are repeated. Returns a dict with the keys of the sequence and
    # values of a list of spacings (num of letters between the repeats).

    # Use a regular expression to remove non-letters from the message:
    message = NONLETTERS_PATTERN.sub("", message.upper())

    # Compile a list of sequence_length-letter sequences found in the message:
    sequence_spacings = {}  # Keys are sequences, values are lists of int spacings.
    for sequence_length in range(3, 6):
        for sequence_start in range(len(message) - sequence_length):
            # Determine what the sequence is, and store it in seq:
            sequence = message[sequence_start : sequence_start + sequence_length]

            # Look for this sequence in the rest of the message:
            for i in range(
                sequence_start + sequence_length,
                len(message) - sequence_length,
            ):
                if message[i : i + sequence_length] == sequence:
                    # Found a repeated sequence.
                    if sequence not in sequence_spacings:
                        sequence_spacings[sequence] = []  # Initialize a blank list.

                    # Append the spacing distance between the repeated
                    # sequence and the original sequence:
                    sequence_spacings[sequence].append(i - sequence_start)
    return sequence_spacings


def get_useful_factors(num):
    # Returns a list of useful factors of num. By "useful" we mean factors
    # less than MAX_KEY_LENGTH + 1 and not 1. For example,
    # get_useful_factors(144) returns [2, 3, 4, 6, 8, 9, 12, 16]

    if num < 2:
        return []  # Numbers less than 2 have no useful factors.

    factors = []  # The list of factors found.

    # When finding factors, you only need to check the integers up to
    # MAX_KEY_LENGTH.
    for i in range(2, MAX_KEY_LENGTH + 1):  # Don't test 1: it's not useful.
        if num % i == 0:
            factors.append(i)
            other_factor = int(num / i)
            if other_factor < MAX_KEY_LENGTH + 1 and other_factor != 1:
                factors.append(other_factor)
    return list(set(factors))  # Remove duplicate factors.


def get_item_at_index_one(items):
    return items[1]


def get_most_common_factors(sequence_factors):
    # First, get a count of how many times a factor occurs in sequence_factors:
    factor_counts = {}  # Key is a factor, value is how often it occurs.

    # sequence_factors keys are sequences, values are lists of factors of the
    # spacings. sequence_factors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
    # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
    for sequence in sequence_factors:
        factor_list = sequence_factors[sequence]
        for factor in factor_list:
            if factor not in factor_counts:
                factor_counts[factor] = 0
            factor_counts[factor] += 1

    # Second, put the factor and its count into a tuple, and make a list
    # of these tuples, so we can sort them:
    factors_by_count = []
    for factor in factor_counts:
        # Exclude factors larger than MAX_KEY_LENGTH:
        if factor <= MAX_KEY_LENGTH:
            # factors_by_count is a list of tuples: (factor, factorCount)
            # factors_by_count has a value like: [(3, 497), (2, 487), ...]
            factors_by_count.append((factor, factor_counts[factor]))

    # Sort the list by the factor count:
    factors_by_count.sort(key=get_item_at_index_one, reverse=True)

    return factors_by_count


def kasiski_examination(ciphertext):
    # Find out the sequences of 3 to 5 letters that occur multiple times
    # in the ciphertext. repeated sequence_spacings has a value like:
    # {'EXG': [192], 'NAF': [339, 972, 633], ... }
    repeated_sequence_spacings = find_repeat_sequences_spacings(ciphertext)

    # (See get_most_common_factors() for a description of sequence_factors.)
    sequence_factors = {}
    for sequence in repeated_sequence_spacings:
        sequence_factors[sequence] = []
        for spacing in repeated_sequence_spacings[sequence]:
            sequence_factors[sequence].extend(get_useful_factors(spacing))

    # (See get_most_common_factors() for a description of factors_by_count.)
    factors_by_count = get_most_common_factors(sequence_factors)

    # Now we extract the factor counts from factors_by_count and
    # put them in all_likely_key_lengths so that they are easier to
    # use later:
    all_likely_key_lengths = []
    for two_int_tuple in factors_by_count:
        all_likely_key_lengths.append(two_int_tuple[0])

    return all_likely_key_lengths


def get_nth_subkeys_letters(nth, key_length, message):
    # Returns every nth letter for each key_length set of letters in text.
    # E.g. get_nth_subkeys_letters(1, 3, 'ABCABCABC') returns 'AAA'
    #      get_nth_subkeys_letters(2, 3, 'ABCABCABC') returns 'BBB'
    #      get_nth_subkeys_letters(3, 3, 'ABCABCABC') returns 'CCC'
    #      get_nth_subkeys_letters(1, 5, 'ABCDEFGHI') returns 'AF'

    # Use a regular expression to remove non-letters from the message:
    message = NONLETTERS_PATTERN.sub("", message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += key_length
    return "".join(letters)


def attempt_hack_with_key_length(ciphertext, most_likely_key_length):
    # Determine the most likely letters for each letter in the key:
    ciphertext_upper = ciphertext.upper()
    # all_frequency_scores is a list of most_likely_key_length number of lists.
    # These inner lists are the frequency_scores lists.
    all_frequency_scores = []
    for nth in range(1, most_likely_key_length + 1):
        nth_letters = get_nth_subkeys_letters(
            nth, most_likely_key_length, ciphertext_upper
        )

        # frequency_scores is a list of tuples like:
        # [(<letter>, <Eng. Freq. match score>), ... ]
        # List is sorted by match score. Higher score means better match.
        # See the english_frequency_match_score() comments in
        # frequency_analysis.py.
        frequency_scores = []
        for possible_key in LETTERS:
            decrypted_text = vigenere_cipher.decrypt_message(possible_key, nth_letters)
            key_and_frequency_match_tuple = (
                possible_key,
                frequency_analysis.english_frequency_match_score(decrypted_text),
            )
            frequency_scores.append(key_and_frequency_match_tuple)
        # Sort by match score:
        frequency_scores.sort(key=get_item_at_index_one, reverse=True)

        all_frequency_scores.append(frequency_scores[:NUM_MOST_FREQ_LETTERS])

    if not SILENT_MODE:
        for i in range(len(all_frequency_scores)):
            # Use i + 1 so the first letter is not called the "0th" letter:
            print("Possible letters for letter %s of the key: " % (i + 1), end="")
            for frequency_score in all_frequency_scores[i]:
                print("%s " % frequency_score[0], end="")
            print()  # Print a newline.

    # Try every combination of the most likely letters for each position
    # in the key:
    for indexes in itertools.product(
        range(NUM_MOST_FREQ_LETTERS), repeat=most_likely_key_length
    ):
        # Create a possible key from the letters in all_frequency_scores:
        possible_key = ""
        for i in range(most_likely_key_length):
            possible_key += all_frequency_scores[i][indexes[i]][0]

        if not SILENT_MODE:
            print("Attempting with key: %s" % possible_key)

        decrypted_text = vigenere_cipher.decrypt_message(possible_key, ciphertext_upper)

        if detect_english.is_english(decrypted_text):
            # Set the hacked ciphertext to the original casing:
            original_casing = []
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    original_casing.append(decrypted_text[i].upper())
                else:
                    original_casing.append(decrypted_text[i].lower())
            decrypted_text = "".join(original_casing)

            # Check with user to see if the key has been found:
            print("Possible encryption hack with key %s:" % possible_key)
            print(decrypted_text[:200])  # Only show first 200 characters.
            print()
            print("Enter D if done, anything else to continue hacking:")
            response = input("> ")

            if response.strip().upper().startswith("D"):
                return decrypted_text

    # No English-looking decryption found, so return None:
    return None


def hack_vigenere(ciphertext):
    # First, we need to do Kasiski Examination to figure out what the
    # length of the ciphertext's encryption key is:
    all_likely_key_lengths = kasiski_examination(ciphertext)
    if not SILENT_MODE:
        key_length_string = ""
        for key_length in all_likely_key_lengths:
            key_length_string += "%s " % key_length
        print(
            "Kasiski Examination results say the most likely key lengths are: "
            + key_length_string
            + "\n"
        )
    hacked_message = None
    for key_length in all_likely_key_lengths:
        if not SILENT_MODE:
            print(
                "Attempting hack with key length %s (%s possible keys)..."
                % (key_length, NUM_MOST_FREQ_LETTERS**key_length)
            )
        hacked_message = attempt_hack_with_key_length(ciphertext, key_length)
        if hacked_message is not None:
            break

    # If none of the key lengths we found using Kasiski Examination
    # worked, start brute-forcing through key lengths:
    if hacked_message is None:
        if not SILENT_MODE:
            print(
                "Unable to hack message with likely key length(s). Brute"
                " forcing key length..."
            )
        for key_length in range(1, MAX_KEY_LENGTH + 1):
            # Don't re-check key lengths already tried from Kasiski:
            if key_length not in all_likely_key_lengths:
                if not SILENT_MODE:
                    print(
                        "Attempting hack with key length %s (%s possible keys)..."
                        % (key_length, NUM_MOST_FREQ_LETTERS**key_length)
                    )
                hacked_message = attempt_hack_with_key_length(ciphertext, key_length)
                if hacked_message is not None:
                    break
    return hacked_message


# If vigenere_hack.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main()
