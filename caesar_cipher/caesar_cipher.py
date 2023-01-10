import string

ALPHABET_VALUES = dict(zip(
    string.ascii_uppercase,
    range(0, len(string.ascii_uppercase))
))

REVERSED_ALPHABET_VALUES = {k: v for v, k in ALPHABET_VALUES.items()}


def encrypt(sentence: str, shift: int) -> str:
    encrypted_sentence = ""
    for letter in sentence:

        if letter.upper() in ALPHABET_VALUES:
            encrypted_sentence += REVERSED_ALPHABET_VALUES[
                (ALPHABET_VALUES[letter.upper()] + shift) % 26]

        else:
            encrypted_sentence += letter

    return encrypted_sentence


if __name__ == "__main__":
    sentence = input("Enter sentence: ")
    shift = int(input("Enter shift of the sentence: "))
    print(f"Encrypted: {encrypt(sentence, shift)}")
