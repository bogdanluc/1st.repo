import pytest

from bogdan.tema05functii.functie_nr_set import numar_set


def test_numar_set10():
    a = 10
    un_set = {3, 8, 6, 1, 9}
    verificare_set = numar_set(a, un_set)
    assert verificare_set == True


def test_numar_set6():
    a = 6
    un_set = {3, 8, 6, 1, 9}
    verificare_set = numar_set(a, un_set)
    assert verificare_set == False
