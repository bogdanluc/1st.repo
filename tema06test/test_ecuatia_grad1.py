import pytest

from tema_ecuatia_grad1 import ecuatia_grad1

def test_ecuatia_grad1_36():
    a, b = 3, 6
    x = ecuatia_grad1(a,b)
    assert x == -2

def test_ecuatia_grad1_84():
    a,b = 8,4
    x = ecuatia_grad1(a,b)
    assert x == -0.5