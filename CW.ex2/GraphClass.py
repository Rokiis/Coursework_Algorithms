import math
class Graph():
	def __init__(self,vertice):
		self.vertice = vertice
		self.connections = {} #dictionary to access connections of a vertice
		self.weights = {} #dictionary to acess weight between two vertices

	def add_vertice(self,vertice): #creates a vertice with empty connection list(workaround type error)
		self.connections[vertice] = []


	def add_weight(self,head,tail,weight): #adds weight between two connections
		if tail in self.connections[head]: #checks if both vertices are directly connected
			self.weights[head,tail] = weight #sets weights for both of the connections, since the graph is undirected
			self.weights[tail,head] = weight
			return True
		else:
			print("Cannot assign weight for vertices " + str(head) + " and " + str(tail) + ", check input!...") #if vertices are not directly connected, does not proceed.
			return False

	def add_connections(self, vertice ,connections): #creates connections between vertices
		for con in connections:
			if con != vertice: #checks if the vertice is not the same as the one that is being tried to connect to
				if vertice not in self.connections[con]: # checks if vertice is not yet there
					self.connections[con].append(vertice)
				if con not in self.connections[vertice]:#adds connection from both sides
					self.connections[vertice].append(con)

		for vertice in self.connections:#sorts connections in ascending order on both sides
			self.connections[vertice].sort()

		for vertice in self.connections:
			self.connections[vertice].sort()

	def isInVertice(self, vertice, key):
		if key in self.connections[vertice]:
			return True
		else:
			return False

	def print_graph(self): #prints graph of vertices with connections
		for key, connections in self.connections.items():
			print("The vertice is %s and the connections are %s" % (key, connections))


	def isPath(self,v,w):#checks is there a path between two vertices
		if v <=0:
			return False
		Q = []
		path = []
		Q += self.connections[v]
		pointer = v
		while Q:
			if w not in Q:
				if pointer in Q:
					Q.remove(pointer)
				if pointer == w: #if current pointer is the same as the one that is being looked for, prints path to file path.txt
					filename = "path.txt"
					file = open(filename, "w")
					file.write(str(path) + "-->" + str(w))
					file.close()
					return True
				elif w in Q:
					path.append(pointer)
					pointer = w
				elif pointer not in path:
					path.append(pointer)
					for x in self.connections[pointer]:
						if x not in path and x not in Q:
							Q.append(x)
							pointer = x
					if Q:
						pointer = Q[0]
					if pointer == w:
						filename = "path.txt"
						file = open(filename, "w")
						file.write(str(path) + "-->" + str(w))
						file.close()
						return True
			if w in Q:
				pointer = w
				Q.remove(pointer)
		filename = "path.txt" # if  the path was not found, prints that there is no way to acces w node from v node and prints path that was looked through.
		file = open(filename, "w")
		file.write("Not found, but here's the path: " + str(path))
		file.close()
		return False

	def isConnectedBFS(self): #checks if graph is strongly connected using Breath First Search algorithm
		visited = []
		ver = 1
		while(self.vertice>=ver):
			visited.append(ver)
			ver+=1
		for v in visited:
			x = sorted(self.BFS(v))
			if x != visited:
				return False
		return True

	def isConnectedDFS(self):# checks if graph is strongly connected using Depth First Search algorithm
		visited = []
		ver = 1
		while(self.vertice>=ver):
			visited.append(ver)
			ver+=1
		for v in visited:
			x = sorted(self.DFS(v))
			if x != visited:
				return False
		return True

	def DFS(self,v): # Depth First Search algorithm
		if v <= 0:
			return False
		Q = []
		path = []
		Q += self.connections[v]
		pointer = v
		while Q:
				if pointer in Q:
					Q.remove(pointer)
				if pointer not in path:
					path.append(pointer)
					for x in self.connections[pointer]:
						if x not in path and x not in Q:
							Q.append(x)
							pointer = x
					if Q:
						pointer = Q[0]
		return path


	def BFS(self, v): #Breath First Search algorithm
		if v == 0:
			return False
		path = []
		Q = [v]
		while Q:
			vertex = Q.pop(0)
			for w in self.connections[vertex]:
				if w not in path:
					path.append(w)
					Q.append(w)
		if path == []:
			return []
		return path


	def dijsktra(self, start,end): #dijsktra algorithm to find most efficient path from one vertice to another.
		seen = {}
		path = []
		unseen_nodes = {}
		shortest_dist = {}
		inf = math.inf
		if shortest_dist == {}:
			for vertice in range(1,self.vertice+1):
				unseen_nodes[vertice] = vertice
				shortest_dist[vertice] = inf
			shortest_dist[start] = 0
		while unseen_nodes: 
			min_node = None
			for node in unseen_nodes:
				if min_node is None:
					min_node = node
				elif shortest_dist[node] < shortest_dist[min_node]:
					min_node = node
			for con in self.connections[min_node]:
				if self.weights[con,min_node] + shortest_dist[min_node] < shortest_dist[con]:
					shortest_dist[con] = self.weights[con,min_node] + shortest_dist[min_node]
					seen[con] = min_node
			unseen_nodes.pop(min_node)
		pointer = end
		while pointer != start:
			try:
				path.insert(0,pointer)
				pointer = seen[pointer]
			except KeyError:
				print("Path not found")
				break
		if shortest_dist[end] != inf:
			return path

