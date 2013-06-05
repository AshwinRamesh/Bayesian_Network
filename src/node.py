# Class definition for the Bayesian Node
# Usage #
#  All nodes should have distinct names
#
#
#
import itertools

class Node:

	def __init__(self, node_name):
		self.name = node_name
		self.children = []
		self.parents = []
		self.table = None

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
				self.parents.remove(n)
				return True
		return False

	# Remove all parents of a given node
	def remove_all_parents(self):
		self.parents = []
		return True

	# Return list of parent nodes
	def get_parents(self):
		return self.parents

	# Initialise empty dictionaries for the node to hold conditional probabilities FIX THIS SHIT
	def initialise_probability_table(self):
		num_parents = len(self.parents)
		if num_parents == 0:
			self.table = {"probability":None}
			return True
		combos =  map(''.join, itertools.product("10", repeat=num_parents)) # list of all combinations of binary results
		self.table = {}
		for i in combos:
			self.table[i] = None
		return True

	# Set the conditional probability for one set of results.
	# Head node will only take one float
	# Other nodes will take a dictionary of node names
	# containing outcome for each condition and a final probability float
	# Example (Head): {"probability":0.5}
	# Example: { 'variableA': 1, 'variableB': 0, 'probability': 0.45} <-- where variable outcomes are [0,1]
	#and probability is between 0 and 1
	# The created key will look like "01" or "111" etc. Ordering of the parents is important. If changes are made
	# to the graph. then the probability table will be reset and should be re-appended
	def set_conditional_probability(self,probability):
		if 'probability' not in probability: # a probability is defined
			print "No probability defined in data"
			print probability
			return False
		if not self.parents: # for head nodes
			self.table = {'probability':float(probability['probability'])}
			return True
		# creating a dictionary key for the specified conditions.
		key = ""
		try:
			for parent in self.parents: # for each parent. Ensure not to change the graph structure or this will break
				key = key+ str(probability[parent.name]) # append the outcome to key.
		except Exception, e:
			print "Exception: The dictionary passed does not contain all required conditions"
			print e
			return False
		#print key
		self.table[key] = float(probability['probability']) # set the conditional probability for the created key
		return True

	# Ensure that all data items are initialised in table
	def check_all_probability_initialised(self):
		for key in self.table:
			if self.table[key] == None:
				return False
		return True
