"""
	An Doan
	Lopez Gerardo

	CECS 575 - Assignment 1
	September 17, 2021
"""

# Node class
class Node:
	def __init__(self, data_value = 0):
		self.data = data_value
		self.left_child = None
		self.right_child = None

	# accessor funtions for Node class
	def get_data(self):
		return self.data

	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	# mutator functions for Node class
	def set_data(self, value):
		self.data = value

	def set_left_child(self, new_node):
		self.left_child = new_node

	def set_right_child(self, new_node):
		self.right_child = new_node

	# method to swap data inside two nodes
	def swap_node_values(self, new_node):	
		swap_value = self.data
		self.data = new_node.get_data()
		new_node.set_data(swap_value)
