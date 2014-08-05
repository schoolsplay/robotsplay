# -*- coding: utf-8 -*-

# Copyright (c) 2014 Stas Zykiewicz <stas.zytkiewicz@schoolsplay.org>
#
#           EVEMotor.py
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 3 of the GNU General Public License
# as published by the Free Software Foundation.  A copy of this license should
# be included in the file GPL-3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.


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
        port = {'A': Motor.PORT.A,
                'B': Motor.PORT.B,
                'C': Motor.PORT.C,
                'D': Motor.PORT.D}[port]
        super(EVEMotor, self).__init__(port=port)

        self.logger = logging.getLogger('EVE.EVEMotor')
        self.logger.debug("Using port: %s" % port)

        self.reset()

    def run_forward_forever(self, speed, regulation_mode=True):
        self.run_forever(speed, regulation_mode=regulation_mode)

    def run_backward_forever(self, speed, regulation_mode=True):
        self.run_forever(-speed, regulation_mode=regulation_mode)

    def move_forward_steps(self, steps):
        self.position = 0
        self.run_position_limited(position_sp=360 * steps, speed_sp=200,
                                  stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=100, ramp_down_sp=100)

    def move_backward_steps(self, steps):
        """
        One step is one cycle of the motor (360 degrees)
        :param steps: integer
        :return:
        """
        self.position = 0
        self.run_position_limited(position_sp=360 * steps, speed_sp=-200,
                                  stop_mode=Motor.STOP_MODE.BRAKE, ramp_up_sp=100, ramp_down_sp=100)


class Turn(object):
    def __init__(self, left_moter, right_moter):
        self.mleft = left_moter
        self.mright = right_moter

    def rightturn(self, degrees, speed=200):
        self.mright.reset()
        self.mleft.reset()
        self.turn = True
        self.mleft.run_forever(speed, regulation_mode=True)
        self._check_turn(self.mleft, degrees * 6,)

    def leftturn(self, degrees, speed=200):
        self.mright.reset()
        self.mleft.reset()
        self.turn = True
        self.mright.run_forever(speed, regulation_mode=True)
        self._check_turn(self.mright, degrees * 6,)


    def _check_turn(self, m, degrees):
        while self.turn:
            print degrees, m.position
            if m.position >= degrees:
                self.turn = False
            time.sleep(0.1)
        m.stop()


def test():
    M1 = EVEMotor()
    M1.run_forever(200, regulation_mode=True)

    M2 = EVEMotor('B')
    M2.run_forever(200, regulation_mode=True)

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

