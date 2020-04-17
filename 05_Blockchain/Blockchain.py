import hashlib
import unittest
import numpy as np
import pdb

from datetime import datetime

class HashPointer():
	"""docstring for HashPointer"""
	def __init__(self, block):
		self.pointer = block
		self.hash = block.get_hash() if block else None

class Block():
	"""docstring for Block"""
	def __init__(self, data, previous_block):
		self.hash_pointer = HashPointer(previous_block)
		self.timestamp = datetime.now()
		self.data = data
		self.hash = self.calculate_hash()

	def has_previous_block(self):
		return (self.hash_pointer.pointer is not None)

	def get_previous_pointer(self):
		return self.hash_pointer.pointer

	def get_previous_hash(self):
		return self.hash_pointer.hash

	def get_hash(self):
		return self.hash

	def get_data(self):
		return self.data

	def previous_block_is_valid(self):
		if self.has_previous_block():
			previous_block = self.get_previous_pointer()
			previous_hash = previous_block.calculate_hash()
			return (previous_hash == self.get_previous_hash())

	def calculate_hash(self):
		sha = hashlib.sha256()
		hash_str = self.__generate_hash_string().encode('utf-8')
		sha.update(hash_str)
		return sha.hexdigest()

	def __generate_hash_string(self):
		hash_str = ''
		hash_str += str(self.get_previous_hash())
		hash_str += str(self.timestamp)
		hash_str += str(self.data)
		return hash_str

class BlockChain():
	"""docstring for BlockChain"""
	def __init__(self):
		self.head = None
		self.tail = None
		self.elements = 0

	def add(self, data):
		if self.tail is None:
			self.tail = Block(data, None)
			self.head = self.tail
			self.elements += 1
			return self.tail
		block = Block(data, self.tail)
		self.tail = block
		self.elements += 1
		return self.tail

	def get_data(self):
		data, validity = [], []
		if self.tail:
			current_block, data_valid = self.tail, True
			while current_block:
				data.insert(0,current_block.get_data())
				validity.insert(0,data_valid)
				if current_block.has_previous_block():
					data_valid = current_block.previous_block_is_valid()
					current_block = current_block.get_previous_pointer()
					continue
				current_block = None
		return data, validity


class TestBlockChain(unittest.TestCase):
	"""docstring for TestBlockChain"""
	def test_default_use_case(self):
		print(" ########## Test 1: Generate blockchain and check data ########## \n")
		input_data = ["Apple","Mango","Peach","Banana","Orange","Grapes","Watermelon","Tomato"]
		block_chain, stored_blocks = self.generate_block_chain_from(input_data)
		block_chain_data, validity = block_chain.get_data()
		self.check_data(input_data, block_chain_data, validity)

	def test_dictionary(self):
		print(" ########## Test 2: Insert dictionary and check data ########## \n")
		input_data = [{"Apples": 13,"Mangos": 5,"Bananas": 17},\
									{"Apples": 19,"Mangos": 5,"Bananas": 9},\
									{"Apples": 5,"Mangos": 5,"Bananas": 6},\
									{"Apples": 3,"Mangos": 0,"Bananas": 4},\
									{"Apples": 15,"Mangos": 5,"Bananas": 18},\
									{"Apples": 11,"Mangos": 4,"Bananas": 18}]
		block_chain, stored_blocks = self.generate_block_chain_from(input_data)
		block_chain_data, validity = block_chain.get_data()
		self.check_data(input_data, block_chain_data, validity)

	def test_integers(self):
		print(" ########## Test 3: Create large blockchain with 10.000 blocks ########## \n")
		input_data = [i for i in range(10000)]
		block_chain, stored_blocks = self.generate_block_chain_from(input_data)
		block_chain_data, validity = block_chain.get_data()
		self.check_data(input_data, block_chain_data, validity)

	def test_alter_blockchain_data(self):
		print(" ########## Test 4: Alter blockchain data and check if detected ########## \n")
		input_data = ["Apple","Mango","Peach","Banana","Orange","Grapes","Watermelon","Tomato"]
		block_chain, stored_blocks = self.generate_block_chain_from(input_data)
		peach_block = stored_blocks[2]
		peach_block.data = "Apple" # Alter data of peach block
		block_chain_data, validity = block_chain.get_data()
		self.check_data(input_data, block_chain_data, validity)

	def check_data(self, input_data, block_chain_data, validity):
		print("Input data: {}".format(input_data[:101]))
		print("Output data: {}".format(block_chain_data[:101])+'\n')
		if len(input_data) > 100:
			print("Blockchain length = {}, input/output prints shortened.\n".format(len(input_data)))
		if np.sum(validity) != len(input_data):
			for index in np.nonzero(validity)[0]:
				self.assertEqual(input_data[index], block_chain_data[index])
			invalid_blocks = np.arange(len(input_data))[np.nonzero(np.invert(validity))]
			print("Warning: Blockchain invalid, data of block(s) {} has been corrupted".format(invalid_blocks)+'\n')
		else:
			self.assertEqual(input_data, block_chain_data)
			print("Blockchain valid, no data has been corrupted.\n")

	def generate_block_chain_from(self, data):
		block_chain, stored_blocks = BlockChain(), []
		for single_data in data:
			new_block = block_chain.add(single_data)
			stored_blocks.append(new_block)
		return block_chain, stored_blocks






