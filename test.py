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

#network.connect_nodes(wetgrass.name,cyclea.name)
#network.connect_nodes(cyclea.name,rain.name)


#network.print_network()
#print network.get_nodes()
#print "***********"
#a = network.copy_network()
#a.print_network()
print network.check_cycles()
network.print_network()


