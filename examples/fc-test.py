#!/usr/bin/env python3

"""
Prints the time and each of the 256 colors from 0 - 255 while
scrolling down the screen.
"""

from digole import lcd
import time
from datetime import datetime

timeFormat = '%I:%M %p'

s = lcd()

while True:
	s.clearScreen()
	p = 0
	for i in range(255):
		s.changePosition(0, p)
		s.setForeColor(i)
		now = datetime.now().strftime(timeFormat)
		s.writeLine(now + ' color = {}'.format(i))
		if p <= 8: p += 1
		else: p = 0
		time.sleep(2)

