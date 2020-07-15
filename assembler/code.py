#!/usr/bin/env python3

class Code():
	"""
	Translates Hack assembly language mnemonics into binary codes.

	API provided on pg. 64, https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/56440f_65a2d8eef0ed4e0ea2471030206269b5.pdf
	"""
	def __init__(self):
		self.dest_list = ['', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
		self.jump_list = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']
		self.comp_dict = {
		    '0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 
		    'A': '0110000', '!D': '0001101', '!A': '0110001', '-D': '0001111', 
		    '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110', 
		    'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111', 
		    'D&A': '0000000', 'D|A': '0010101', 'M': '1110000', '!M': '1110001', 
		    '-M': '1110011', 'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 
		    'D-M': '1010011', 'M-D': '1000111', 'D&M': '1000000', 'D|M': '1010101'
		    }

	def a_code(self, val):
		"""
		Create string for a-code
		"""
		return '{0:b}'.format(int(val)).zfill(16)

	def c_code(self, comp_str, dest_str, jump_str):
		"""
		Create string for c-code
		"""
		return '111' + self.comp(comp_str) + self.dest(dest_str) + self.jump(jump_str)

	def dest(self, dest_str):
		"""
		Returns the binary code of the dest mnemonic.
		"""
		return '{0:b}'.format(self.dest_list.index(dest_str)).zfill(3)

	def comp(self, comp_str):
		"""
		Returns the binary code of the comp mnemonic.
		"""
		return self.comp_dict[comp_str]

	def jump(self, jump_str):
		"""
		Returns the binary code of the jump mnemonic.
		"""
		return '{0:b}'.format(self.jump_list.index(jump_str)).zfill(3)

