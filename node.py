# Class definition for the Bayesian Node

class Node:
	name = None
	parents = None
	children = None

	def __init__(self, node_name):
		name = node_name
		return self

	def add_child(self):
		return 0

	def get_children(self):
		return 0

	def add_parent(self):
		return 0
