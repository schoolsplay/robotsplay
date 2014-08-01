"""
Simple file and console logger to be used inside ev3 modules.
You should import this in your start script/module and call the
'start' method only once as soon as possible.
This will configure the logger from the standard python 'logging' module.
The logger is a singelton meaning you will get always the same
logger object no matter where you import it.

Usage:
import EVELogger
EVELogger.set_level() # optional, defaults to 'debug'
EVELogger.start('myproject_name') # this should be called after the first import but BEFORE importing logging module.

# standard python module, but already configured by the above statements
import logging


class Test(object):
    def __init__(self):
        self.logger = logging.getLogger('myproject_name.Test') # name must be the same as used in start()

"""
import os
import shutil
import logging
import logging.handlers

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

LOGPATH = os.path.join(os.path.expanduser('~'), "EVE.log")
LOGPATH_OLD = os.path.join(os.path.expanduser('~'), "EVE.log.old")

if os.path.exists(LOGPATH):
    try:
        shutil.move(LOGPATH, LOGPATH_OLD)
    except Exception, info:
        print "Failed to remove old log"
        print info
    else:
        print "moved old logpath"


def set_level(level='debug'):
    """
    Set the logging level
    :param level: defaults to 'debug'
                  Possible values are 'debug', 'info', 'warning', 'error', 'exception'
    :return: None
    """
    global CONSOLELOGLEVEL, FILELOGLEVEL
    lleveldict = {'debug': logging.DEBUG,
                  'info': logging.INFO,
                  'warning': logging.WARNING,
                  'error': logging.ERROR,
                  'critical': logging.CRITICAL}
    if not lleveldict.has_key(level):
        print "Invalid loglevel: %s, setting loglevel to 'debug'" % level
        llevel = lleveldict['debug']
    else:
        llevel = lleveldict[level]
    CONSOLELOGLEVEL = llevel
    FILELOGLEVEL = llevel


def start(name='EVE'):
    """
    Start the logger configuration. This should only be called once at the start of your program
    :param name: defaults to 'EVE' but should be the name of you project.
    :return: None
    """
    global CONSOLELOGLEVEL, FILELOGLEVEL
    #create logger
    logger = logging.getLogger(name)
    logger.setLevel(CONSOLELOGLEVEL)
    #create console handler and set level
    ch = logging.StreamHandler()
    ch.setLevel(CONSOLELOGLEVEL)
    #create file handler and set level
    fh = logging.FileHandler(LOGPATH)
    fh.setLevel(FILELOGLEVEL)
    #create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    #add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    #add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.info("File logger created: %s" % LOGPATH)

    # test
    module_logger = logging.getLogger("%s.EVELogger" % name)
    module_logger.info("logger created, start logging")


