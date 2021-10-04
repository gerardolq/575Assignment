"""
	An Doan
	Lopez Gerardo

	CECS 575 - Assignment 1
	September 17, 2021
"""

import io
import sys
import unittest
from minheap import Node, MinHeap

"""
	* Important Note*
	We chose to stick to snake_case for our methods and variables
	The methods and variables in camelCase and other cases are from the built-in python library
"""

class NodeTest(unittest.TestCase):
	def setUp(self):
		self.node1 = Node(1)
		self.node2 = Node(2)
		self.node3 = Node(3)
		self.node4 = Node(4)
		self.node5 = Node(5)

	# test accessor and mutator methods for Node's data
	def test_set_get_data(self):
		node1 = Node()
		node2 = Node()
		node3 = Node()

		self.assertEqual(0, node1.get_data())

		node1.set_data(1)
		node2.set_data(2)
		node3.set_data(3)

		self.assertEqual(1, node1.get_data())
		self.assertEqual(2, node2.get_data())
		self.assertEqual(3, node3.get_data())

	# test accessor and mutator methods for Node's left child
	def test_set_get_left_child(self):
		self.node1.set_left_child(self.node2)
		self.node2.set_left_child(self.node4)

		self.assertEqual(self.node2, self.node1.get_left_child())
		self.assertEqual(self.node4, self.node2.get_left_child())

		self.assertNotEqual(self.node1, self.node2.get_left_child())
		self.assertNotEqual(self.node3, self.node1.get_left_child())
		self.assertNotEqual(self.node5, self.node3.get_left_child())

	# test accessor and mutator methods for Node's left child
	def test_set_get_right_child(self):
		self.node1.set_right_child(self.node3)
		self.node3.set_right_child(self.node5)

		self.assertEqual(self.node3, self.node1.get_right_child())
		self.assertEqual(self.node5, self.node3.get_right_child())

		self.assertNotEqual(self.node1, self.node2.get_right_child())
		self.assertNotEqual(self.node4, self.node3.get_right_child())
		self.assertNotEqual(self.node5, self.node2.get_right_child())

	def test_swap_node_values(self):
		node1 = Node(2)
		node2 = Node(5)

		node1.swap_node_values(node2)
		self.assertEqual(node1.get_data(), 5)
		self.assertEqual(node2.get_data(), 2)

		node1 = Node(12)
		node2 = Node(53)

		node1.swap_node_values(node2)
		self.assertEqual(node1.get_data(), 53)
		self.assertEqual(node2.get_data(), 12)

class MinHeapTest(unittest.TestCase):
	def setUp(self):
		# first heap
		self.first_heap = MinHeap()
		arr = [5,4,3,6,7,2,1,8]

		for x in arr:
			self.first_heap.insert(Node(x))

		# second heap
		self.second_heap = MinHeap()

		for x in range(10, 0, -1):
			self.second_heap.insert(Node(x))

	# tests that height function
	def test_heap_height(self):
		#check first heap
		# height of the tree
		tree_height = self.first_heap.heap_height(self.first_heap.root)

		# height of left sub tree starting from the root
		left_height = self.first_heap.heap_height(self.first_heap.root.get_left_child())

		# height of right sub tree starting from the root
		right_height = self.first_heap.heap_height(self.first_heap.root.get_right_child())

		self.assertEqual(4, tree_height)
		self.assertEqual(3, left_height)
		self.assertEqual(2, right_height)

		# check condition left and right height should always be <=1
		# left height should never be less than right height
		self.assertTrue((left_height - right_height) <= 1)

		# check second heap
		tree_height = self.second_heap.heap_height(self.second_heap.root)
		left_height = self.second_heap.heap_height(self.second_heap.root.get_left_child())
		right_height = self.second_heap.heap_height(self.second_heap.root.get_right_child())

		self.assertTrue((left_height - right_height) <= 1)

	# tests find node function
	def test_find_node(self):
		# test first heap
		self.assertTrue(self.first_heap.find_node(5))
		self.assertTrue(self.first_heap.find_node(1))
		self.assertFalse(self.first_heap.find_node(9))
		self.assertFalse(self.first_heap.find_node(15))

		# test second heap
		self.assertTrue(self.second_heap.find_node(4))
		self.assertTrue(self.second_heap.find_node(10))
		self.assertFalse(self.second_heap.find_node(29))
		self.assertFalse(self.second_heap.find_node(11))

	# tests root logic when smaller value node is introduced
	def test_root_change(self):
		min_heap = MinHeap()

		for x in range(10, 0, -1):
			min_heap.insert(Node(x))
			self.assertEqual(min_heap.get_root().get_data(), x)

	# test if postorder data matches expected output 
	def test_postorder_traversal(self):
		# test first heap
		captured_output = io.StringIO()
		sys.stdout = captured_output

		self.first_heap.postorder_traversal()
		sys.stdout = sys.__stdout__

		# expected output = 6 3 5 7 8 4 1
		expected='6\n3\n5\n2\n7\n8\n4\n1\n'
		self.assertEqual(captured_output.getvalue(), expected)

		# test second heap
		captured_output = io.StringIO()
		sys.stdout = captured_output

		self.second_heap.postorder_traversal()

		# expected output = 10 6 8 5 2 9 7 3 1
		expected='10\n6\n8\n5\n2\n9\n4\n7\n3\n1\n'
		self.assertEqual(captured_output.getvalue(), expected)

	# test if odd preorder data matches expected output 
	def test_odd_preorder_traversal(self):
		# test first heap
		captured_output = io.StringIO()
		sys.stdout = captured_output
		self.first_heap.odd_preorder_traversal()
		sys.stdout = sys.__stdout__

		#expected output = 1 3 5 7
		expected='1\n3\n5\n7\n'
		self.assertEqual(captured_output.getvalue(), expected)

		# test second heap
		captured_output = io.StringIO()
		sys.stdout = captured_output

		self.second_heap.odd_preorder_traversal()
		# expected output = 1 5 3 9 7
		expected='1\n5\n3\n9\n7\n'
		self.assertEqual(captured_output.getvalue(), expected)

	# tests that an empty tree can be created
	def test_empty(self):
		min_heap = MinHeap()
		captured_output = io.StringIO()
		sys.stdout = captured_output
		min_heap.odd_preorder_traversal()
		sys.stdout = sys.__stdout__
		expected=''
		self.assertEqual(captured_output.getvalue(), expected)


if __name__ == '__main__':
	unittest.main()
