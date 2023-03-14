# One-time pad

import random


def main() -> None:
    c, k = encrypt("This is a secret message.")
    print(c, k)
    print(decrypt(c, k))


# Function to encrypt text using pseudo-random numbers
def encrypt(message: str) -> tuple[list[int], list[int]]:
    plaintext = [ord(i) for i in message]
    key = []
    cipher = []
    for i in plaintext:
        k = random.randint(1, 300)
        c = (i + k) * k
        cipher.append(c)
        key.append(k)
    return cipher, key


# Function to decrypt text using pseudo-random numbers.
def decrypt(cipher: list[int], key: list[int]) -> str:
    plaintext = []
    for i in range(len(key)):
        p = int((cipher[i] - (key[i]) ** 2) / key[i])
        plaintext.append(chr(p))
    return "".join(plaintext)


if __name__ == "__main__":
    main()
