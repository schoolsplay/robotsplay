# -*- coding: utf-8 -*-

# Copyright (c) 2014 Stas Zykiewicz <stas.zytkiewicz@schoolsplay.org>
#
#           EVELcd.py
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
Abstract class for writing text to the LCD screen.
"""
import sys

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

sys.path.insert(0, '..')
from PIL import ImageFont
from ev3.ev3dev import Lcd

class EVELcd(Lcd):
    def __init__(self, font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
                 size=15):
        super(EVELcd, self).__init__()
        self.font = ImageFont.truetype(font, size)
        self.size = size

    def write(self, text='', position=(0, 0)):
        self.draw.text(position, text, font=self.font)
        self.update()

    def clear(self):
        self.reset()
        self.update()

