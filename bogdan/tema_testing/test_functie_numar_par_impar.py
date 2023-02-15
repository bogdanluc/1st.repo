import pytest

from bogdan.tema05functii.functie_numar_par_impar import numar_par_impar

def test_numar_par_impar90():
    numar = 90
    par_impar = numar_par_impar(numar)
    assert par_impar == 0

def test_numar_par_impar33():
    numar = 33
    par_impar = numar_par_impar(numar)
    assert par_impar == 1