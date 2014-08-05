"""
Classic bumper car.
Wheeled verhicle is needed with the right motor on A, left motor on B and
the IR-sensor on  4 (on ev3dev we can't use 1)
"""
import logging
import thread
import time
from ev3.lego import InfraredSensor

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')

from eve import EVELogger
EVELogger.set_level('debug')
EVELogger.start('Bcar')

from eve.EVEMotor import EVEMotor, Turn
from eve.EVEApp import App

class BumperCar(App):
    def __init__(self, speed=200):
        super(BumperCar, self).__init__()
        self.logger = logging.getLogger('Bcar.BumperCar')
        self.LM = EVEMotor('A')
        self.RM = EVEMotor('B')
        self.Trn = Turn(self.LM, self.RM)

        self.IR = InfraredSensor()
        self.speed = speed

        self.run_ir_read = True
        self.proxy = 100 # distance ad read from IR

        self.register_callback(self.update)
        self.register_backspace_callback(self.stop)

    def reset(self):
        self.RM.reset()
        self.LM.reset()

    def stop(self):
        self.RM.stop()
        self.LM.stop()
        self.run_ir_read = False
        self.stoploop()

    def stop_motors(self):
        self.RM.stop()
        self.LM.stop()

    def run_motors(self):
        self.RM.run_forward_forever(self.speed)
        self.LM.run_forward_forever(self.speed)

    def _read_ir(self):
        while self.run_ir_read:
            self.proxy = self.IR.prox
            time.sleep(0.5)

    def update(self):
        """
        Called by the EVEApp eventloop
        :return:
        """
        if self.proxy < 20:
            self.stop_motors()
            self.RM.move_backward_steps(1)
            self.LM.move_backward_steps(1)
            self.Trn.leftturn(180)
            self.run_motors()
            self.proxy = 100

        self.time2live -= 1
        print "time to live", self.time2live
        if self.time2live < 1:
            self.stop()

    def start(self):
        self.logger.info("Start")

        self.wait4enter()

        thread.start_new(self._read_ir, ())
        self.run_motors()
        self.time2live = 300

        self.runloop() # eventloop from EVEApp



if __name__ == '__main__':

    try:
        BC = BumperCar()
        BC.start()
    except KeyboardInterrupt, info:
        BC.stop()
        from eve import EVE3Laws


