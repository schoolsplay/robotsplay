"""
Classic bumper car.
Wheeled verhicle is needed with the right motor on A, left motor on B and
the IR-sensor on  4 (on ev3dev we can't use 1)
"""
__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

import EVELogger
EVELogger.set_level('debug')
EVELogger.start()

from eve.EVEMotor import EVEMotor


class BumperCar(object):
    def __init__(self, speed=200):
        self.LM = EVEMotor('A')
        self.RM = EVEMotor('B')
        self.RM.run_forward_forever(speed)
        self.LM.run_forward_forever(speed)
        #self.IR =

        self.run = True

    def reset(self):
        self.RM.reset()
        self.LM.reset()

    def stop(self):
        self.RM.stop()
        self.LM.stop()

    def _read_ir(self):
        pass

    def start(self):
        while self.run:
            self.RM.start()
            self.LM.start()



if __name__ == '__main__':

    try:
        BC = BumperCar()
        BC.start()
    except KeyboardInterrupt, info:
        import EVE3Laws


