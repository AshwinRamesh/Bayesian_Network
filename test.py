from node import Node
from bayesian_network import BayesianNetwork

network = BayesianNetwork()

print network.get_nodes()


cloudy = network.add_node("cloudy")
sprinkler = network.add_node("sprinkler")
rain = network.add_node("rain")
wetgrass = network.add_node(("wetgrass"))

network.connect_nodes(cloudy.name,sprinkler.name)
network.connect_nodes(cloudy.name,rain.name)
network.connect_nodes(sprinkler.name,wetgrass.name)
network.connect_nodes(rain.name,wetgrass.name)

network.print_network()
print network.get_nodes()


