import unittest

from bogdan.curs7.ex2curs7 import f_to_c
from testtemp0107 import c_to_f


class TemperatureConverterTests(unittest.TestCase):

    def test_0c_to_f(self):
        f = 32
        c = f_to_c(f)
    assert c == 0

    def test_100c_to_f(self):
        f = 212
        c = f_to_c(f)
    assert c == 100
