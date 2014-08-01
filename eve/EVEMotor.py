"""
Abstract class for the ev3 Motor class
"""
import time
from ev3.ev3dev import Motor
import logging

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

class EVEMotor(Motor):
    def __init__(self, port='A'):
        """
        Adds some extra metods to the base ev3 Motor class
        :param port: post to which this motor is connected.
                     possible values: 'A', 'B', 'C', 'D'
        :return: instance
        """
        self.logger = logging.getLogger('EVE.EVEMotor')
        self.logger.debug("Using port: %s" % port)
        port = {'A': Motor.PORT.A,
                'B': Motor.PORT.B,
                'C': Motor.PORT.C,
                'D': Motor.PORT.D}[port]
        super(EVEMotor, self).__init__(port=port)

    def turn_left(self, degrees):
        pass

    def turn_right(self, degrees):
        pass

    def backup(self, speed=200):
        pass

if __name__ == '__main__':
    import EVELogger
    EVELogger.set_level('debug')
    EVELogger.start()

    M = EVEMotor()
    M.run()
