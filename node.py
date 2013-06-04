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

	def __str__(self):
		return "Node: %s" %(self.name)

	def __repr__(self):
		return self.__str__()

	# Check if node already has speciified child
	def check_child_exists(self,search_name):
		for n in self.children:
			if n.name == search_name:
				return True
		return False

	# Check if node already has specified parent
	def check_parent_exists(self,search_name):
		for n in self.parents:
			if n.name == search_name:
				return True
		return False

	# Add child to a given node
	def add_child(self,child_node):
		if self.check_child_exists(child_node.name) is False:
			self.children.append(child_node) # Add child to self
			return True
		return False

	# Remove a child-parent relationship given the name of the child
	def  remove_child(self,name):
		for n in self.children:
			if n.name == name:
				self.children.remove(n)
				return True
		return False

	# Remove all children of a given node
	def remove_all_children(self):
		self.children = []
		return True

	# Get a list of all child nodes
	def get_children(self):
		return self.children

	# Add parent to a node
	def add_parent(self,parent_node):
		if self.check_parent_exists(parent_node) is False: # Try and add parent connection if it doesn't exist
			self.parents.append(parent_node) # Add parent connection
			return True
		return False

	# Remove a given parent from a node
	def remove_parent(self,name):
		for n in self.parents:
			if n.name == name:
				self.children.remove(n)
				return True
		return False

	# Remove all parents of a given node
	def remove_all_parents(self):
		self.parents = []
		return True

	# Return list of parent nodes
	def get_parents(self):
		return self.parents

	# TODO????
	def set_probability(self,parents):
		return 0
