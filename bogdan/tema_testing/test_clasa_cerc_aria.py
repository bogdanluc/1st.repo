import pytest

from bogdan.tema06clase.tema06_clasa_cerc import Cerc


def test_aria_cercului():
    cerc = Cerc(8, 'rosu')
    aria = cerc.aria_cercului()
    assert round(aria, 13) == 201.0619298297468
