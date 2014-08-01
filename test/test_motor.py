import os
import sys
import time

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

import unittest
sys.path.insert(0, os.getcwd())

from eve import EVELogger
EVELogger.set_level('debug')
EVELogger.start()

from eve.EVEMotor import EVEMotor



class TestSequenceFunctions(unittest.TestCase):
    _M = EVEMotor('A')

    def test_00_run_forever(self):
        result = TestSequenceFunctions._M.run_forever(200)
        time.sleep(5)
        TestSequenceFunctions._M.stop()
        self.assertFalse(result, "Should be false")


if __name__ == '__main__':
    print "start lcd unittesting"
    unittest.main(verbosity=3)
