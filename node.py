# Class definition for the Bayesian Node
# Usage #
#  All nodes should have distinct names
#
#
#

class Node:

	def __init__(self, node_name):
		self.name = node_name
		self.children = []
		self.parents = []

	def add_child(self):
		return 0

	def  remove_child(self):
		return 0

	def remove_all_children(self):
		return 0

	def get_children(self):
		return self.children

	def add_parent(self):
		return 0

	def remove_parent(self):
		return 0

	def remove_all_parents(self):
		return 0

	def get_parents(self):
		return self.parents

	def set_probability(self,parents)
