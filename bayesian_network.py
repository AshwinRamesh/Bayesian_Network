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

	def get_nodes(self):
		return self.nodes

	# Check if a given node (with a specified name) already exists in the Network #
	def check_node_exists(self,name):
		for n in self.nodes:
			if n.name == name:
				return True
		return False

	# Add a node to the Network without any connections
	def add_node(self,name):
		if self.check_node_exists(self,name) is False: # Check that node name doesnt exist in list
			temp_node = Node(name)
			self.nodes.append(temp_node)
			return temp_node
		return False # Node already exists (with a given name)


