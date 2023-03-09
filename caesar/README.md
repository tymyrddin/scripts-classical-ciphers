# Caesar's cipher

![Caesar example](../assets/images/caesar.png?raw=true)

One of the most widely known historical encryption methods is the Caesar cipher. According to the Roman historian Gaius Suetonius Tranquillus (c. 70–130 CE), Julius Caesar used this cipher to encrypt military messages, shifting all letters of the plaintext three places to the right.

Although the Caesar cipher is not useful for modern cryptographic needs, it does contain all the fundamental concepts needed for a cryptography algorithm

* A plaintext message
* An algorithm: shift every letter
* A key: for example +3
* A ciphertext

This is, essentially, the same structure used by all modern symmetric algorithms. Because there are only 26 letters in the English alphabet, the original key space is 26 (in English), but that can be expanded to include some common punctuation and capital letters.

## Scripts

* caesar_cipher26.py
* caesar_hack26.py
* caesar_cipher65.py
* caesar_hack65.py

## Usages

### Keyspace = 26

`SYMBOLS = "abcdefghijklmnopqrstuvwxyz"`

#### Cipher

```shell
usage: caesar_cipher26.py [-h] [-t TEXT] [-s SHIFT] [-m {encrypt,decrypt}]

Caesar Cipher 26

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to encrypt or decrypt
  -s SHIFT, --shift SHIFT
                        Shift/Key (Number), may be negative
  -m {encrypt,decrypt}, --mode {encrypt,decrypt}
                        encrypt or decrypt

Example:
            caesar_cipher26.py -t [text]
            caesar_cipher26.py -t [text] -s 3             # shift 3 places
            caesar_cipher26.py -t [text] -s 3 -m decrypt  # decrypt
```

#### Hack

```shell
usage: caesar_hack26.py [-h] [-t TEXT]

Caesar Cipher 26

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to hack

Example:
            caesar_hack26.py -t [message]
```

### Keyspace = 65

`SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."`

#### Cipher

```shell
usage: caesar_cipher65.py [-h] [-t TEXT] [-s SHIFT] [-m {encrypt,decrypt}]

Caesar Cipher 65

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to encrypt or decrypt
  -s SHIFT, --shift SHIFT
                        Shift/Key (Number), may be negative
  -m {encrypt,decrypt}, --mode {encrypt,decrypt}
                        encrypt or decrypt

Example:
            caesar_cipher65.py -t [text]
            caesar_cipher65.py -t [text] -s 3             # shift 3 places
            caesar_cipher65.py -t [text] -s 3 -m decrypt  # decrypt
```

#### Hack

```shell
usage: caesar_hack65.py [-h] [-t TEXT]

Caesar Cipher 65

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to hack

Example:
            caesar_hack65.py -t [message]
```
