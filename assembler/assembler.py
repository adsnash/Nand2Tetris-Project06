#!/usr/bin/env python3

import os
import time
from parser import Parser
from code import Code
from symbol_table import SymbolTable


class Assembler():
	"""
	Assembler to convert a .asm file to .hack
	ASSUMPTION: .asm file is error-free

	Initialization:
		Construct an empty symbol table
		Add the pre-defined symbols to the symbol table
	First Pass: 
		Scan the entire program;
		For each “instruction” of the form (xxx):
			Add the pair (xxx, address) to the symbol table, 
			where address is the number of the instruction following (xxx)
	Second Pass:
		Set n to 16
		Scan the entire program again; for each instruction:
			If the instruction is @symbol, look up symbol in the symbol table;
				If (symbol, value) is found, use value to complete the instruction’s translation;
				If not found:
					Add (symbol, n) to the symbol table, 
					Use nto complete the instruction’s translation,
					n++
			If the instruction is a C-instruction, complete the instruction’s translation
			Write the translated instruction to the output file.

	Instructions provided on pg. 44, https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/56440f_65a2d8eef0ed4e0ea2471030206269b5.pdf
	"""
	def __init__(self, debug=False):
		self.symbol_table = SymbolTable()
		self.code = Code()
		self.parser = None  # instantiated with input_file as arg in self.assemble
		self.debug = debug

	def debug_print(self, print_string):
		if self.debug:
			print(print_string)

	def assemble(self, input_file):
		"""
		Read the input file, run through pass 1 and 2, write output to disk
		"""
		start = time.time()
		assert os.path.exists(input_file)
		assert input_file.endswith('.asm')
		self.debug_print('Converting {}'.format(input_file))
		self.parser = Parser(input_file)
		check_1 = time.time()
		self.debug_print('Parsed file in {:.5f} secs'.format(round(check_1 - start, 5)))
		self.pass_1()
		check_2 = time.time()
		self.debug_print('First pass in {:.5f} secs'.format(round(check_2 - check_1, 5)))
		out_text = self.pass_2()
		check_3 = time.time()
		self.debug_print('Second pass in {:.5f} secs'.format(round(check_3 - check_2, 5)))
		out_file = self.parser.file_name.split('.asm')[0]+'.hack'
		self.write_output(out_file, out_text)
		self.debug_print('Wrote {}'.format(out_file))
		self.debug_print('Ran in {:.5f} secs'.format(round(time.time() - start, 5)))

	def pass_1(self):
		"""
		First pass of assembler, add the label symbols
		Read all commands, only paying attention to labels and updating the symbol table
		"""
		asm_line = 0
		while self.parser.has_more_commands():
			self.parser.advance()
			if self.parser.command_type() == 'L_COMMAND':
				self.symbol_table.add_entry(self.parser.symbol(), asm_line)
			else:
				asm_line +=1 

	def pass_2(self):
		"""
		Second pass of assembler, add the var. symbols
		Restart reading and translate commands
		"""
		out_text = []
		var_count = 16
		self.parser.reset_read()
		while self.parser.has_more_commands():
			self.parser.advance()
			if self.parser.command_type() == 'A_COMMAND':
				if self.parser.symbol().isdigit():
					out_text.append(self.code.a_code(self.parser.symbol()))
				else:
					if not self.symbol_table.contains(self.parser.symbol()):
						self.symbol_table.add_entry(self.parser.symbol(), var_count)
						var_count += 1
					out_text.append(self.code.a_code(self.symbol_table.get_address(self.parser.symbol())))
			elif self.parser.command_type() == 'C_COMMAND':
				out_text.append(self.code.c_code(self.parser.comp(), self.parser.dest(), self.parser.jump()))
		return out_text

	def write_output(self, out_file, out_text):
		"""
		Write file to disk, make sure to change extension to .hack
		"""
		with open(out_file, 'w') as fp:
			for item in out_text:
				fp.write("{}\n".format(item))

