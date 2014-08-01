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
        Adds some extra methods to the base ev3 Motor class
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

    def run_backward_forever(self, speed=200):
        pass

    def move_forward_steps(self, steps):
        pass

    def move_backward_steps(self, steps):
        pass

if __name__ == '__main__':
    import EVELogger
    EVELogger.set_level('debug')
    EVELogger.start()

    M1 = EVEMotor()
    M1.run_forever(200, regulation_mode=True)

    M2 = EVEMotor('B')
    M2.run_forever(200, regulation_mode=True)

    M1.start()
    M2.start()
    time.sleep(5)

    M1.stop()
    M2.stop()