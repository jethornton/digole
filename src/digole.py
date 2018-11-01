#!/usr/bin/env python3

import smbus as smbus

class lcd(object):
	def __init__(self, address=None):
		if address == None:
			self.address = 0x27 # Will call the setter
		else:
			self.address = address
		self.i2c = smbus.SMBus(1)

	@property
	def address(self):
		print('called getter')
		print('address is {0:#x}'.format(self._address))
		return self._address

	@address.setter
	def address(self, value):
		print('called setter')
		print('setting the address to {0:#x}'.format(value))
		self._address = value

	@address.deleter
	def address(self):
		print('called deleter')
		print('Deleting...')
		del self._address


	def convert(self, text=None):
		if text == None:
			print('No text string passed')
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

