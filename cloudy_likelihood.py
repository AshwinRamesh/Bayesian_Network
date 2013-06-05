#!/usr/bin/python

from src.node import Node
from src.bayesian_network import BayesianNetwork
import sys
import numpy

TOTALRUNS = 1000 # Number of runs for each sample group

def run_likelihood(network,evidence,outcome,num):
	results = []
	for x in xrange(0,TOTALRUNS):
		results.append(network.likelihood_weighting(evidence, outcome, num))
	mean = numpy.mean(results)
	SD = numpy.std(results)
	variance = numpy.var(results)
	print "Sample Size: %d ; Iterations: %d ; Mean: %f ; Standard Deviation: %f ; Variance: %f" %(num,TOTALRUNS,mean,SD,variance)


def main(argv):
	if (len(sys.argv) == 2 and sys.argv[1].isdigit()): # one arguement passed
		num = int(sys.argv[1])
	else:
		print "Incorrect Usage: ./couldy_likelihood.py <number>"
		exit(1)
	network = BayesianNetwork() # Define the Bayesian Network

	## Add nodes to the network ##
	cloudy = network.add_node("cloudy")
	sprinkler = network.add_node("sprinkler")
	rain = network.add_node("rain")
	wetgrass = network.add_node(("wetgrass"))

	## Add connections between nodes ##
	network.connect_nodes(cloudy.name,sprinkler.name)
	network.connect_nodes(cloudy.name,rain.name)
	network.connect_nodes(sprinkler.name,wetgrass.name)
	network.connect_nodes(rain.name,wetgrass.name)

	## Add conditional probability to nodes ##
	network.init_probability_tables() # initialise the probability tables

	network.add_probability("cloudy",{'probability':0.5})

	network.add_probability("sprinkler", {'cloudy':1,'probability':0.1})
	network.add_probability("sprinkler", {'cloudy':0,'probability':0.5})

	network.add_probability("rain", {'cloudy':1,'probability':0.8})
	network.add_probability("rain", {'cloudy':0,'probability':0.2})

	network.add_probability("wetgrass", {'sprinkler':1,'rain':1,'probability':0.99})
	network.add_probability("wetgrass", {'sprinkler':0,'rain':0,'probability':0.0})
	network.add_probability("wetgrass", {'sprinkler':0,'rain':1,'probability':0.9})
	network.add_probability("wetgrass", {'sprinkler':1,'rain':0,'probability':0.9})

	## Defining paramenters for likelihood weighting ##
	evidence = {"sprinkler":1,"wetgrass":1}
	outcome = {"cloudy":1}
	run_likelihood(network,evidence, outcome, num)

if __name__ =="__main__":
	main(sys.argv)
