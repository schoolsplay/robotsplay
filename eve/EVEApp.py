"""
First attempts to get a eventloop thing.
You should use this as a mixing for your main class
"""
import time
import sys
import logging

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

from ev3.ev3dev import Key

class App(object):
    """
    Provides a eventloop running at 50 FPS
    The loop will wait until the 'Enter' button is pressed, that's the middle one.
    It will also catch the 'Backspace' button, that's the topleft one, and quits when it's pressed.
    """
    def __init__(self):
        self.logger = logging.getLogger('EVE.App')
        self.key = Key()
        self._cbflist = []
        self._backspace_cbf = None
        self.runme = True

    def register_callback(self, cbf, args=()):
        """
        Register a function you want to have called from the eventloop.
        You can register as many functions as you like and they will be called in the order which they
        are registered.
        :param cbf: callable function
        :param args: optional arguments for the function
        :return:
        """
        self.logger.debug("registered %s" % cbf)
        self._cbflist.append((cbf, args))

    def register_backspace_callback(self, cbf):
        """
        Register a special callback function which is called when the the backspace key is pressed.
         You can only register one function
        :param cbf:
        :return:
        """
        self.logger.debug("registered backspace cbf %s" % cbf)
        self._backspace_cbf = cbf

    def wait4enter(self):
        """
        Will wait until the enter key is pressed.
        This is a blocking call but it will check for backspace
        :return:
        """
        self.logger.info("Waiting for enter")
        while not self.key.enter:
            if self._poll_backspace():
                if self._backspace_cbf:
                    apply(self._backspace_cbf)
                    break
            time.sleep(0.02)

    def _poll_backspace(self):
        if self.key.backspace:
            return True

    def stoploop(self):
        """
        Stops the loop
        :return:
        """
        self.logger.warning("Stopping eventloop")
        self.runme = False

    def runloop(self):
        """
        Run the eventloop
        :return:
        """
        self.logger.info("Start eventloop")
        while self.runme:
            if self._poll_backspace():
                self.runme = False
                self.logger.warning("Backspace pressed, quitting")
                if self._backspace_cbf:
                    self.logger.info("calling backspace function")
                    apply(self._backspace_cbf)
            for f, arg in self._cbflist:
                apply(f, arg)

            time.sleep(0.02)


if __name__ == '__main__':

    import EVELogger
    EVELogger.set_level('debug')
    EVELogger.start()

    def back_cbf():
        print "Backspace pressed, quitting"
        sys.exit()

    def cbf(*args):
        print "cbf called with", args

    ap = App()
    ap.register_backspace_callback(back_cbf)
    ap.register_callback(cbf, "optional arg")

    ap.wait4enter()



