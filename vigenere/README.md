# Vigenere Cipher

![Vigenere example](../assets/images/vigenere.png?raw=true)

Perhaps the most widely known multi-alphabet cipher is the Vigenère cipher. This cipher was described in 1553 by Giovan Battista Bellaso, but was misattributed to nineteenth century cryptographer Blaise de Vigenère. It is a method of encrypting alphabetic text by using a series of different mono-alphabet ciphers selected based on the letters of a keyword. Bellaso also added the concept of using any keyword, thereby making the choice of substitution alphabets difficult to calculate.

For many years, Vigenère was considered very strong, even unbreakable. In the nineteenth century, Friedrich Kasiski published a technique for breaking the Vigenère cipher.

## Scripts

* vigenere_cipher.py
* vigenere_hack.py
* vigenere_dictionary_hack.py (interactive)
* vigenere_file_hack.py (can take a long time)

## Usages

### Cipher

```shell
usage: vigenere_cipher.py [-h] [-t TEXT] [-k KEY] [-m {encrypt,decrypt}]

Vigenere Cipher

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to encrypt or decrypt
  -k KEY, --key KEY     String
  -m {encrypt,decrypt}, --mode {encrypt,decrypt}
                        encrypt or decrypt

Example:
            vigenere_cipher.py -t sometext
            vigenere_cipher.py -t sometext -k "ASIMOV" -m encrypt    
```

### Hacks

#### Bruteforce Hack

```shell
usage: vigenere_hack.py [-h] [-c CIPHERTEXT]

Vigenere Hack

options:
  -h, --help            show this help message and exit
  -c CIPHERTEXT, --ciphertext CIPHERTEXT
                        Ciphertext to hack

Example:
            vigenere_hack.py -c [ciphertext]
```

#### Dictionary hack

```shell
usage: vigenere_dictionary_hack.py [-h] [-c CIPHERTEXT]

Vigenere Dictionary Hack

options:
  -h, --help            show this help message and exit
  -c CIPHERTEXT, --ciphertext CIPHERTEXT
                        Ciphertext to hack

Example:
            vigenere_dictionary_hack.py -c [ciphertext]
```

#### Hack using files

```shell
usage: vigenere_file_hack.py [-h] [-i INPUT_FILENAME] [-o OUTPUT_FILENAME]

Vigenere File Hack

options:
  -h, --help            show this help message and exit
  -i INPUT_FILENAME, --input_filename INPUT_FILENAME
                        Takes input from a file name of your choice
  -o OUTPUT_FILENAME, --output_filename OUTPUT_FILENAME
                        Directs the output to a name of your choice

Example:
            vigenere_file_hack.py -i input_filename.txt -o output_filename.txt
```
