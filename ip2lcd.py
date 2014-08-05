#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Stas Zykiewicz <stas.zytkiewicz@schoolsplay.org>
#
#           i[2lcd.py
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
Script to be run after a network device is set up and will display the ip
number(s) in use.
Place this script in /etc/network/if-up.d as ip2lcd (without the .py part)
and make sure it's executable (chmod a+x)
"""

from PIL import ImageFont
import subprocess
import time
__author__ = 'Stas Zytkiewicz stas@childsplay.mobi'

from ev3.ev3dev import Lcd
cmd = subprocess.Popen("/sbin/ifconfig", shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
lines = cmd.communicate()[0].split('\n')

i = 0
usb_ip = 'Not in use'
wlan_ip = 'Not in use'
for line in lines:
    if 'usb0' in line and 'inet' in lines[i + 1]:
        usb_ip = lines[i + 1].split('inet addr:')[1].split(' ')[0]
    if 'wlan0' in line and 'inet' in lines[i + 1]:
        wlan_ip = lines[i + 1].split('inet addr:')[1].split(' ')[0]
    i += 1

d = Lcd()
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
d.draw.text((10, 10), "Welcome to python-ev3.", font=font)
d.draw.text((0, 25), "USB IP: %s" % usb_ip, font=font)
d.draw.text((0, 40), "WLAN IP: %s" % wlan_ip, font=font)
d.update()

