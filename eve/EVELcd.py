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

