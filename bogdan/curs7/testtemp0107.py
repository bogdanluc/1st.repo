import unittest

from bogdan.curs7.ex0107temp import c_to_f


class TemperatureConverterTests(unittest.TestCase):

    def test_0c_to_f(self):
        c = 0
        f = c_to_f(c)
        # assert folosind operatorul Python
        assert f == 32

    def test_100c_to_f(self):
        c = 100
        f = c_to_f(c)
        # assert folosind operatorul Python
        self.assertEquals(f, 212)