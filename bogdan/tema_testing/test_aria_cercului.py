import pytest

from bogdan.tema03structuri_date_colectii.aria_cercului import aria_cercului

def test_aria_cercului10():
    raza = 10
    aria = aria_cercului(raza)
    assert aria == 314.159

def test_aria_cercului120():
    raza = 120
    aria = aria_cercului(raza)
    assert aria == 45238.896