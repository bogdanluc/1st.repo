import pytest

from bogdan.tema04_05ciclurirepetitive_functii.string_timp import timp_secunde


def test_timp_secunde_66400():
    secunde = 66400
    timp = timp_secunde(secunde)
    assert timp == '0z, 18h, 26m, 40s'

def test_timp_secunde_78236():
    secunde = 78236
    timp = timp_secunde(secunde)
    assert timp == '0z, 21h, 43m, 56s'
