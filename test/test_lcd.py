import os
import sys

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

import unittest
sys.path.insert(0, os.getcwd())

from eve.EVELcd import EVELcd

class TestSequenceFunctions(unittest.TestCase):

    def test_00_clear_lcd(self):
        result = EVELcd().clear()
        self.assertFalse(result, "Should be false")

    def test_01_write_text(self):
        result = EVELcd().write("Unittest")
        self.assertFalse(result, "Should be false")

if __name__ == '__main__':
    print "start lcd unittesting"
    unittest.main(verbosity=3)
