import pytest
from caesar_cipher import encrypt


@pytest.mark.parametrize(
    "sentence, shift, expected_sentence",
    [
        ("AHOJ", 2, "CJQL"),
        ("super", 26, "SUPER"),
        ("sIeMeNS", 5, "XNJRJSX"),
        ("WoRkInG iS bEsT YEAH", 21, "RJMFDIB DN WZNO TZVC"),
        ("????", 2, "????"),
        ("Ů§Ú)ÉÉÁÝŽŘČ", 15, "Ů§Ú)ÉÉÁÝŽŘČ")
    ]
)
def test_caesar(sentence, shift, expected_sentence):
    assert encrypt(sentence, shift) == expected_sentence
