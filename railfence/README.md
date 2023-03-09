# Rail fence transposition ciphers

In a rail fence cipher, the plaintext letters are written diagonally in a up-down pattern from left to right. The message is then read row-by-row from top to down. The number of rows can vary, and the starting place for the first letter can vary. 

**Plaintext**: `This is a secret text.`

```text
 T           a           t
   h       s   s       e   t      .
     i   i       e   r       e   t
       s           c           x
```

**Ciphertext**: `Tat hsset. iieret scx`

## Scripts

* railfence_encrypt.py
* railfence_decrypt.py
* railfence_hack.py
* railfence_test.py

## Usages

### Encrypt

```shell
usage: railfence_encrypt.py [-h] [-t PLAINTEXT] [-k KEY]

Rail fence transposition cipher encryption

options:
  -h, --help            show this help message and exit
  -t PLAINTEXT, --plaintext PLAINTEXT
                        Plaintext to encrypt
  -k KEY, --key KEY     Number of layers

Example:
            railfence_encrypt.py -t plaintext
            railfence_encrypt.py -t plaintext -k 4
```

### Decrypt

```shell
usage: railfence_decrypt.py [-h] [-t CIPHERTEXT] [-k KEY]

Rail fence transposition cipher decryption

options:
  -h, --help            show this help message and exit
  -t CIPHERTEXT, --ciphertext CIPHERTEXT
                        Ciphertext to decrypt
  -k KEY, --key KEY     Number of layers

Example:
            railfence_decrypt.py -t ciphertext
            railfence_decrypt.py -t ciphertext -k 4
```

### Bruteforce hack

```shell
usage: railfence_hack.py [-h] [-t CIPHERTEXT]

Rail fence transposition cipher hack

options:
  -h, --help            show this help message and exit
  -t CIPHERTEXT, --ciphertext CIPHERTEXT
                        Ciphertext to hack

Example:
            railfence_hack.py -t [message]
```


