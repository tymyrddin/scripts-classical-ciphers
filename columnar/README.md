# Columnar transposition ciphers

In a columnar transposition cipher, the message is written in a grid of equal length rows, and then read out column by column. The columns are chosen in a scrambled order. 

**Plaintext**: `This is a secret text`
**Key**: `4`

| 3   | 1   | 2   | 4   |
|:----|:----|:----|:----|
| T   | h   | i   | s   |
| -   | i   | s   | -   |
| a   | -   | s   | e   |
| c   | r   | e   | t   |
| -   | t   | e   | x   |
| t   | -   | -   | -   |


**Ciphertext**: `hi rt issee T ac ts etx `

## Scripts

* columnar_encrypt.py
* columnar_decrypt.py
* columnar_hack.py
* columnar_file_cipher.py
* columnar_file_hack.py
* columnar_test.py

## Usages

### Encrypt

```shell
usage: columnar_encrypt.py [-h] [-t TEXT] [-k KEY]

Columnar transposition cipher encryption

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to encrypt
  -k KEY, --key KEY     Key (Number)

Example:
            columnar_encrypt.py -t sometext
            columnar_encrypt.py -t sometext -k 13 
```

### Decrypt

```shell
usage: columnar_decrypt.py [-h] [-t TEXT] [-k KEY]

Columnar transposition cipher decryption

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to decrypt
  -k KEY, --key KEY     Key (Number)

Example:
            columnar_decrypt.py -t sometext
            columnar_decrypt.py -t sometext -k 13
```

### Hack

```shell
usage: columnar_hack.py [-h] [-t TEXT]

Columnar transposition cipher hack

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Message to hack

Example:
            columnar_hack.py -t [message]
```

### File encrypt/decrypt

```shell
usage: columnar_file_cipher.py [-h] [-i INPUT_FILENAME] [-o OUTPUT_FILENAME] [-k KEY] [-m {encrypt,decrypt}]

Columnar transposition cipher encrypt/decrypt file

options:
  -h, --help            show this help message and exit
  -i INPUT_FILENAME, --input_filename INPUT_FILENAME
                        Takes input from a file name of your choice
  -o OUTPUT_FILENAME, --output_filename OUTPUT_FILENAME
                        Directs the output to a name of your choice
  -k KEY, --key KEY     Key (Number)
  -m {encrypt,decrypt}, --mode {encrypt,decrypt}
                        encrypt or decrypt

Example:
            columnar_file_cipher.py -i input_filename.txt -o output_filename.txt -k 13 -m encrypt
```


