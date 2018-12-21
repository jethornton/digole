#!/usr/bin/env python3

import smbus as smbus

class lcd(object):
	def __init__(self, address=None):
		if address == None:
			self.address = 0x27 # Will call the setter
		else:
			self.address = address
		self.i2c = smbus.SMBus(1)
		self.namedColors = {'black':0 , 'navy':2 , 'blue':3 , 'green':24 ,
		'teal':27 , 'lime':28 , 'aqua':31 , 'maroon':192 , 'purple':195 ,
		'olive':219 , 'red':224 , 'magenta':227 , 'yellow':252 , 'white':255}

	@property
	def address(self):
		#print('called getter')
		#print('address is {0:#x}'.format(self._address))
		return self._address

	@address.setter
	def address(self, value):
		#print('called setter')
		#$print('setting the address to {0:#x}'.format(value))
		self._address = value

	@address.deleter
	def address(self):
		#print('called deleter')
		#print('Deleting...')
		del self._address


	def convert(self, text=None):
		if text == None:
			#print('No text string passed')
			return -1
		else:
			return [ord(i) for i in text]

	def clearScreen(self):
		self.i2c.write_block_data(self._address, 0x00, [0x43, 0x4c])

	def changePosition(self, x, y=None):
		if not y:
			self.i2c.write_block_data(self._address, 0x00, [0x54, 0x50, x, 0])
		else:
			self.i2c.write_block_data(self._address, 0x00, [0x54, 0x50, x, y])

	def writeLine(self, text=None):
		if not text:
			text = 'TTSamle Text'
		else:
			text = ''.join(['TT', text])
		s = [ord(i) for i in text]
		self.i2c.write_block_data(self._address, 0x00, s)


	def setForeColor(self, color=None):
		if not color: # set to white
			value = 255
		else:
			try:
				value = int(color)
			except ValueError:
				value = self.namedColors.get(color.lower())
		self.i2c.write_block_data(self._address, 0x00, [0x53, 0x43, value])

	def setBackColor(self, color=None):
		if not color: # set to black
			color = 0
		self.i2c.write_block_data(self._address, 0x00, [0x42, 0x47, 0x43, color])


