# -*- coding: utf-8 -*-
from PIL import ImageFont
import subprocess
import time

__author__ = 'stas Zytkiewicz stas@childsplay.mobi'

from ev3.ev3dev import Lcd
cmd = subprocess.Popen("ifconfig", shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
output = cmd.communicate()[0]


d = Lcd()
d.draw.ellipse((20, 20, 60, 60))
d.update()
time.sleep(2)
d.reset()
font = ImageFont.load_default()
d.draw.text((10, 10), "Using IP: %s" % ip, font=font)
d.update()



