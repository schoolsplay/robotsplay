# -*- coding: utf-8 -*-

# Copyright (c) 2014 Stas Zykiewicz <stas.zytkiewicz@schoolsplay.org>
#
#           EVE3Laws.py
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
