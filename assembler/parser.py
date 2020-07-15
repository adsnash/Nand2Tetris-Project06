#!/usr/bin/env python3

class Parser():
	"""
	Encapsulates access to the input code. Reads an assembly language command, 
	parses it, and provides convenient access to the command’s components 
	(fields and symbols). In addition, removes all white space and comments.

	API provided on pg. 63, https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/56440f_65a2d8eef0ed4e0ea2471030206269b5.pdf
	"""
	def __init__(self, in_file):
		self.file_name = in_file
		self.prog_text = self.read_asm(in_file)
		self.prog_num = len(self.prog_text)
		self.cmd_next = 0
		self.cmd_text = ''
		return

	def read_asm(self, input_file):
		"""
		Read .asm file from disk, return list of strings for commands only
		"""
		program_text = []
		with open(input_file) as fp:
			for line in fp.readlines():
				if len(line) > 1 and not line.startswith('//'):
					program_text.append(line.split('\n')[0].lstrip(' ').split(' ')[0])
		return program_text

	def reset_read(self):
		"""
		Reset reading for second pass
		"""
		self.cmd_next = 0
		self.cmd_text = ''
		return

	def has_more_commands(self):
		"""
		Are there more commands in the input?
		"""
		return self.cmd_next < self.prog_num

	def advance(self):
		"""
		Reads the next command from the input and makes it the current command. 
		Should be called only if hasMoreCommands() is true. 
		Initially there is no current command. 
		"""
		if self.has_more_commands():
			self.cmd_text = self.prog_text[self.cmd_next]
			self.cmd_next += 1

	def command_type(self):
		"""
		Returns the type of the current command:
		m A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
		m C_COMMAND for dest=comp;jump
		m L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol.
		"""
		if self.cmd_text.startswith('('):
			return 'L_COMMAND'
		elif self.cmd_text.startswith('@'):
			return 'A_COMMAND'
		return 'C_COMMAND'

	def symbol(self):
		"""
		Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). 
		Should be called only when commandType() is A_COMMAND or L_COMMAND.
		"""
		if self.command_type() == 'L_COMMAND':
			return self.cmd_text[1:-1]
		elif self.command_type() == 'A_COMMAND':
			return self.cmd_text[1:]

	def dest(self):
		"""
		Returns the dest mnemonic in the current C-command (8 possibilities). 
		Should be called only when commandType() is C_COMMAND.
		"""
		if self.command_type() == 'C_COMMAND':
			if '=' in self.cmd_text:
				return self.cmd_text.split('=')[0]
			return ''

	def comp(self):
		"""
		Returns the comp mnemonic in the current C-command (28 possibilities). 
		Should be called only when commandType() is C_COMMAND.
		"""
		if self.command_type() == 'C_COMMAND':
			if '=' in self.cmd_text:
				return self.cmd_text.split('=')[1]
			elif ';' in self.cmd_text:
				return self.cmd_text.split(';')[0]

	def jump(self):
		"""
		Returns the jump mnemonic in the current C-command (8 possibilities). 
		Should be called only when commandType() is C_COMMAND.
		"""
		if self.command_type() == 'C_COMMAND':
			if ';' in self.cmd_text:
				return self.cmd_text.split(';')[1]
			return '' 

