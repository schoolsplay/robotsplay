"""
Abstract calss for the IR sensor
"""
from ev3.lego import InfraredSensor

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

import logging

class EVEIRsensor(InfraredSensor):
    def __init__(self, mode='prox'):
        """
        Simplify sensor use a bit
        :param mode: In which mode we should operate
                     possible values: 'prox', 'seek', 'remote', 'remote_bin'
        :return: instance
        """
        self.logger = logging.getLogger('EVE.EVEIRsensor')
        self.logger.debug("Using mode: %s" % mode)
        self.evemode = mode
        super(EVEIRsensor, self).__init__()

    def read(self):
        """
        Read the value of the sensor (TODO: understand various other modes)
        :return: The value returned by the sensor.
                 For seek a integer between 100 (far) and 0 (close)
                 For seek a tuple
        """
        result = {'proxy': self.prox,
                'seek': self.seek,
                'remote': self.remote,
                'remote_bin': self.remote_bin}[self.evemode]
        self.logger.debug("reading mode: %s, read: %s" % result)
        return result


def test():
    import time
    IR = EVEIRsensor()
    for i in range(10):
        print "IR read", IR.read()
        time.sleep(0.5)

if __name__ == '__main__':

    import EVELogger
    EVELogger.set_level('debug')
    EVELogger.start()

    try:
        test()
    except KeyboardInterrupt, info:
        import EVE3Laws


