from GraphClass import *
from unit_testing import *


if __name__ == '__main__':
	unittest.main(exit=False) #runs through tests before executing any of the commands below. Tests if vertices, connections and weights are being created propperly, tests isConnected and isPath functions.
	a = Graph(6)

	a.add_vertice(1)
	a.add_vertice(2)
	a.add_vertice(3)
	a.add_vertice(4)
	a.add_vertice(5)
	a.add_vertice(6)

	a.add_connections(1, [2])
	a.add_connections(2, [3])
	a.add_connections(3, [4])
	a.add_connections(4,[5])
	a.add_connections(5,[6])
	a.add_connections(6,[1])


	a.add_weight(1,2,20)
	a.add_weight(2,3,3)
	a.add_weight(3,4,15)
	a.add_weight(4,5,10)
	a.add_weight(5,6,17)
	a.add_weight(6,1,19)
	print(a.dijsktra(6,5))