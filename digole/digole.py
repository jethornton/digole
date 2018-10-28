#!/usr/bin/env python3

#import smbus as smbus

class lcd:
	def __init__(self, address):
		self._address = address

	@property
	def address(self):
		print('address type is {}'.format(type(self._address)))
		return self._address

	@address.setter
	def address(self, value):
		print('setting the address to {}'.format(value))
		self._address = value

	@address.deleter
	def address(self):
		print('Deleting...')
		del self._address
