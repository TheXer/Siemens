import string


def is_palindrome(sentence: str) -> bool:
    stripped_sentence = sentence.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
    return stripped_sentence.lower() == stripped_sentence[::-1].lower()


if __name__ == "__main__":
    sentences = input("Input a sentence: ")
    print(is_palindrome(sentences))