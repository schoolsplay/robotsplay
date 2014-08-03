"""
Special module to stop stuff and do some cleanup? in case our robot runs out of control.
Hence the name which is based on assimov's 3 laws of robotics :-)
It's now used like this:
try:
    main()
except KeyboardInterrupt, info:
    import EVE3Laws

"""

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
