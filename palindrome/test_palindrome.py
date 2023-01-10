import pytest

from palindrome_program import is_palindrome


@pytest.mark.parametrize(
    "word, expected",
    [
        ("oko", True),
        ("OkO", True),
        ("OKo", True),
        ("kayAk", True),
        ("????", True),
        ("Lokomotiva", False),
        ("Liška běžela přes koleje", False),
        ("wow", True),
        ("Poor Dan is in a droop", True),
        ("Cigar? Toss it in a can. It is so tragic.", True),
        ("Palindrom je slovo, věta, číslo nebo melodie, která má tu vlastnost", False),

    ]
)
def test_palindrome(word, expected):
    assert is_palindrome(word) == expected
