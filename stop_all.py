__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

from ev3.ev3dev import Motor

for p in (Motor.PORT.A, Motor.PORT.B, Motor.PORT.C, Motor.PORT.D):
    try:
        m = Motor(port=p)
        m.stop()
        m.reset()
    except Exception, info:
        print info
    else:
        print "Motor %s stopped" % p

