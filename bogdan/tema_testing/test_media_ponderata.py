import pytest

from tema_media_ponderata import media_ponderata


def test_media_ponderata():
    val = (7, 5, 9)
    pon = (3, 2, 7)
    mp = media_ponderata(val, pon)
    assert mp == 7.833333333333333


def test_media_ponderata2():
    val = (6, 8, 2)
    pon = (1, 1, 2)
    mp = media_ponderata(val, pon)
    assert mp == 4.5
