# Class for a Bayesian Network. Currently only supports binary states

# Usage #
# Always add all nodes before making any connections between them.
# If a new node has to be added, add that node. Make connections between other nodes. Add probability
#
#

from node import Node

class BayesianNetwork:

	def __init__(self):
		self.nodes = []

	def __str__(self):
		return "This is a Bayesian Network"

	def get_nodes(self):
		return self.nodes

	# Get a node with specific name
	def get_node(self,node_name):
		for n in self.nodes:
			if n.name == node_name:
				return n
		return False

	# Check if a given node (with a specified name) already exists in the Network #
	def check_node_exists(self,name):
		for n in self.nodes:
			if n.name == name:
				return True
		return False

	# Add a node to the Network without any connections
	def add_node(self,name):
		if self.check_node_exists(name) is False: # Check that node name doesnt exist in list
			temp_node = Node(name)
			self.nodes.append(temp_node)
			return temp_node
		return False # Node already exists (with a given name)

	# Connect two nodes in a parent->child and child->parent relationship
	def connect_nodes(self,parent_name,child_name):
		parent = self.get_node(parent_name)
		child = self.get_node(child_name)
		if (parent and child): # if neither is False
			parent.add_child(child)
			child.add_parent(parent)
		return False

	# TODO
	def check_cycles(self):
		return 0

	def print_network(self):
		if not self.nodes:
			print "The network is empty"
		for n in self.nodes:
			print "Node: %s ; Parents: %s ; Children: %s" %(n.name,str(n.get_parents()),str(n.get_children()))

