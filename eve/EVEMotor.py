"""
Abstract class for the ev3 Motor class
"""

import time
import thread
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
        self.reset()

    def run_forward_forever(self, speed, regulation_mode=True):
        self.run_forever(speed, regulation_mode=regulation_mode)

    def run_backward_forever(self, speed, regulation_mode=True):
        self.run_forever(-speed, regulation_mode=regulation_mode)

    def move_forward_steps(self, steps):
        pass

    def move_backward_steps(self, steps):
        pass

class Turn(object):
    def __init__(self, left_moter, right_moter):
        self.mleft = left_moter
        self.mright = right_moter

    def rightturn(self, degrees, speed=200):
        self.mright.reset()
        self.mleft.reset()
        self.turn = True
        thread.start_new(self._check_turn, (self.mleft, degrees * 6,))
        time.sleep(0.1)
        self.mleft.run_forever(speed, regulation_mode=True)


    def left(self, degrees, speed=200):
        self.mright.reset()
        self.mleft.reset()
        self.turn = True
        thread.start_new(self._check_turn, (self.mright, degrees * 6,))
        time.sleep(0.1)
        self.mright.run_forever(speed, regulation_mode=True)


    def _check_turn(self, m, degrees):
        run = True
        while run:
            print [m.position], [degrees]
            if m.position >= degrees:
                run = False
            time.sleep(0.1)
        m.stop()


def test():
    M1 = EVEMotor()
    M1.run_forever(200, regulation_mode=True)

    M2 = EVEMotor('B')
    M2.run_forever(200, regulation_mode=True)

    M1.start()
    M2.start()
    time.sleep(5)
    M1.stop()
    M2.stop()

    T = Turn(M1, M2)
    T.rightturn(180)

    time.sleep(15)

    M1.run_backward_forever(200)
    M2.run_backward_forever(200)
    time.sleep(5)

    M1.stop()
    M2.stop()

if __name__ == '__main__':
    import EVELogger
    EVELogger.set_level('debug')
    EVELogger.start()

    try:
        test()
    except KeyboardInterrupt, info:
        import EVE3Laws

