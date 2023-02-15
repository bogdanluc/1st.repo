import pytest

from tema_radical_test import radicalul_unui_numar

def test_radicalul_unui_numar9():
    x = 9
    radical = radicalul_unui_numar(x)
    assert radical == 3

def test_radicalul_unui_numar16():
    x = 16
    radical = radicalul_unui_numar(x)
    assert radical == 4