"""
	An Doan
	Lopez Gerardo

	CECS 575 - Assignment 1
	September 17, 2021
"""

from node import Node

class MinHeap:
	"""
	Initialization function. 
	This creates an empty heap and returns nothing.
	No parameters needed.
	"""
	def __init__(self):
		self.root = None

	"""
	insert function - this function gets called to insert a new node into
	our tree using recursion to properly place the new_node and maintain heap order
		: param new_node 		- this is the node to be inserted
		: param current_node 	- this is the node that is cross referenced with the new_node
	"""
	def insert(self, new_node):
		if self.root == None:
			self.root = new_node
			return

		self._insert(new_node, self.root)

	def _insert(self, new_node, current_node):
		if current_node == None:
			current_node = new_node
			return

		elif new_node.get_data() < current_node.get_data():
			current_node.swap_node_values(new_node)

		left_height = self.heap_height(current_node.get_left_child())
		right_height = self.heap_height(current_node.get_right_child())

		# compare the heights of left and right subheaps to place the new node into the heap
		if left_height <= right_height:
			if current_node.get_left_child() == None:
				current_node.set_left_child(new_node)
			
			else:
				self._insert(new_node, current_node.get_left_child())

		else:
			if current_node.get_right_child() == None:
				current_node.set_right_child(new_node)
				
			else:
				self._insert(new_node, current_node.get_right_child())

	"""
	heap_height function - recursively calls left and right child until
	None node is hit (null ptr). Then returns +1 for every other node
	will return the heighest
		: param current_node - the node we are currently pointing to
	"""
	def heap_height(self, current_node):
		if current_node is None:
			return 0

		else:
			left_height = self.heap_height(current_node.get_left_child())
			right_height = self.heap_height(current_node.get_right_child())

			if left_height > right_height:
				return left_height + 1
			else:
				return right_height + 1

	"""
	find_node function - finds a node inside the heap utilizing preorder traversal
	First, we must ensure our tree is not empty. If found, we return True, otherwise we return False
		: param key - the value that we are looking for in the tree
		: param current_node - the node currently being checked out
	"""
	def find_node(self, key):
		if self.root == None:
			print("Min Heap is empty!")

		else:
			return self._find_node(self.root, key)

	def _find_node(self, current_node, key):
		if current_node == None:
			return False

		if current_node.get_data() == key:
			return True
		
		return self._find_node(current_node.get_left_child(), key) or self._find_node(current_node.get_right_child(), key)

	"""
	postorder_traversal function - calls left child until None is hit
	then right child, until none is hit, then prints
		: param current_node - used as a pointer to the current node being used
	"""
	def postorder_traversal(self):
		if self.root != None:
			self._postorder_traversal(self.root)

	def _postorder_traversal(self, current_node):
		if current_node != None:
			self._postorder_traversal(current_node.get_left_child())
			self._postorder_traversal(current_node.get_right_child())
			print(current_node.get_data())

	"""
	odd_traverse function - prints current node if it is odd, then calls left
		child, prints if odd, and continues in this manner until None is hit. Once that
		happens, the right child is called, and the pattern repeats
		: param current_node - used as a pointer to the current node being used
	"""
	def odd_preorder_traversal(self):
		if self.root != None:
			self._odd_preorder_traversal(self.root)

	def _odd_preorder_traversal(self, current_node):
		if current_node != None:
			if current_node.get_data()%2 != 0:
				print(current_node.get_data())
			self._odd_preorder_traversal(current_node.get_left_child())
			self._odd_preorder_traversal(current_node.get_right_child())

	# return root node of the heap
	def get_root(self):
		return self.root
