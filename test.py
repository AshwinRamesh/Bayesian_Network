from node import Node
from bayesian_network import BayesianNetwork

network = BayesianNetwork()

#print network.get_nodes()


cloudy = network.add_node("cloudy")
sprinkler = network.add_node("sprinkler")
rain = network.add_node("rain")
wetgrass = network.add_node(("wetgrass"))
#cyclea = network.add_node("cyclea")

network.connect_nodes(cloudy.name,sprinkler.name)
network.connect_nodes(cloudy.name,rain.name)
network.connect_nodes(sprinkler.name,wetgrass.name)
network.connect_nodes(rain.name,wetgrass.name)
#network.connect_nodes(cyclea.name,wetgrass.name)

network.init_probability_tables()

network.add_probability("cloudy",{'probability':0.5})

network.add_probability("sprinkler", {'cloudy':1,'probability':0.1})
network.add_probability("sprinkler", {'cloudy':0,'probability':0.5})

network.add_probability("rain", {'cloudy':1,'probability':0.8})
network.add_probability("rain", {'cloudy':0,'probability':0.2})

network.add_probability("wetgrass", {'sprinkler':1,'rain':1,'probability':0.99})
network.add_probability("wetgrass", {'sprinkler':0,'rain':0,'probability':0.0})
network.add_probability("wetgrass", {'sprinkler':0,'rain':1,'probability':0.9})
network.add_probability("wetgrass", {'sprinkler':1,'rain':0,'probability':0.9})

print "Data Init: %s" %(str(network.check_all_tables_init()))
#network.connect_nodes(wetgrass.name,cyclea.name)
#network.connect_nodes(cyclea.name,rain.name)


#network.print_network()
#print network.get_nodes()
#print "***********"
#a = network.copy_network()
#a.print_network()

#a = network.topological_sort()
#print "TOPOLOGICAL SORT"
#print a[0].children
evidence = {"sprinkler":1,"wetgrass":1}
outcome = {"cloudy":1}
result = network.likelihood_weighting(evidence, outcome, 5000000)
print "Likelyhood for 5000000 samples: %f" %(result)
#print "Cycles present in graph: %s" %(str(network.check_cycles()))
#network.print_network()



