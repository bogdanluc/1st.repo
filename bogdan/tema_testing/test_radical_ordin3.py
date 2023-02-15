import unittest

from bogdan.tema04_05ciclurirepetitive_functii.tema0405radicali3 import radicali_de_ordin_3


class RadicalOrdin3Test(unittest.TestCase):

    def test_radical3(self):
        a, b, c = 9, 18, 54
        radical = radicali_de_ordin_3(a, b, c)
        assert radical == (3,6,18)
