# Class for a Bayesian Network. Currently only supports binary states

# Usage #
# Always add all nodes before making any connections between them.
# If a new node has to be added, add that node. Make connections between other nodes. Add probability again
#
#

from node import Node

class BayesianNetwork:

	def __init__(self):
		self.nodes = []
		self.probabilities = []

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
			return True
		return False

	#Remove the connection between two nodes if they exist
	def deconnect_nodes(self,parent_name,child_name):
		parent = self.get_node(parent_name)
		child = self.get_node(child_name)
		if (parent and child):
			parent.remove_child(child_name)
			child.remove_parent(parent_name)
			return True
		return False


	# Copy the current network into a new network by value
	def copy_network(self):
		network = BayesianNetwork()
		for n in self.nodes: # copy all nodes to new network
			network.add_node(n.name)
		for n in self.nodes: # copy all edges
			for child in n.children:
				network.connect_nodes(n.name,child.name)
		# TODO copy all probabilities
		return network

	# get all nodes with no parent nodes
	def get_head_nodes(self):
		head_list = []
		for n in self.nodes:
			if not n.parents:
				head_list.append(n)
		return head_list

	# returns true if there are any edges otherwise false
	def check_connections(self):
		for n in self.nodes:
			if n.parents or n.children:
				return True
		return False

	# Use Topological Sort to check for cycles
	def check_cycles(self):
		sorted_list = []
		network = self.copy_network() # copy of BN
		network.print_network()
		head_nodes = network.get_head_nodes() # list of head nodes
		while head_nodes:
			temp_node = head_nodes.pop() # remove a node from list
			sorted_list.append(temp_node)
			for child in list(temp_node.children):
				network.deconnect_nodes(temp_node.name, child.name)
				if not child.parents: # child has no other parent nodes
					head_nodes.append(child)
		return network.check_connections() # returns true if connections exist -> cycles

	# Pretty printing of network
	def print_network(self):
		if not self.nodes:
			print "The network is empty"
		for n in self.nodes:
			print "Node: %s ; Parents: %s ; Children: %s" %(n.name,str(n.get_parents()),str(n.get_children()))

