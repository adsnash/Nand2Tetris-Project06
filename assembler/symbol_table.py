#!/usr/bin/env python3

class SymbolTable():
	"""
	Keeps a correspondence between symbolic labels and numeric addresses.
	
	API provided on pg. 65, https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/56440f_65a2d8eef0ed4e0ea2471030206269b5.pdf
	"""
	def __init__(self, ):
		self.table = {'R{}'.format(i): i for i in range(16)}
		self.table.update({'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 
			'THAT': 4, 'SCREEN': 16384, 'KBD': 24576})

	def add_entry(self, symbol, address):
		"""
		Adds the pair (symbol, address) to the table.
		"""
		if not self.contains(symbol):
			self.table[symbol] = address

	def contains(self, symbol):
		"""
		Does the symbol table contain the given symbol?
		"""
		return symbol in self.table.keys()

	def get_address(self, symbol):
		"""
		Returns the address associated with the symbol.
		"""
		return self.table[symbol]

