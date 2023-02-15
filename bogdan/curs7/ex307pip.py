import pytest

from bogdan.curs7.ex0107temp import c_to_f


def test_0c_to_f(self):
    c = 0
    f = c_to_f(c)
    assert f == 32


def test_100c_to_f(self):
    c = 100
    f = c_to_f(c)
    assert f == 212