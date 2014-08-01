import os
import sys

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

import unittest
sys.path.insert(0, os.getcwd())

from eve import EVELogger

class TestSequenceFunctions(unittest.TestCase):

    def test_00_set_level_to_debug(self):
        result = EVELogger.set_level('debug')
        self.assertFalse(result, "Should return None")

    def test_01_start(self):
        result = EVELogger.start()
        self.assertFalse(result, "Should return None")

if __name__ == '__main__':
    print "start logger unittesting"
    unittest.main(verbosity=3)
