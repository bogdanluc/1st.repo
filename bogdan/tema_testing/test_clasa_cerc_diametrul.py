import pytest

from bogdan.tema06clase.tema06_clasa_cerc import Cerc


def test_diametrul_cercului():
    cerc = Cerc(10, 'verde')
    diametrul = cerc.diametrul_cercului()
    assert diametrul == 20
