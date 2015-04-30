class FastDfs:
	def	__init__(self, graph):
		self.graph = graph
	
	def start(self):
		self.longest = []
		self.current = []
		FastDfs.reset(self.graph)

		for vertex in self.graph.vertex.values():
			if not vertex.used: self.dfs(vertex)
		return self.longest

	def dfs(self, vertex):
		self.current.append(vertex.id)
		vertex.used = True
		for edge in vertex.edges:
			if not edge.v2.used and edge.v2 != vertex:
				self.dfs(edge.v2)
		if len(self.current) > len(self.longest):		
			self.longest = self.current[:]
		self.current.pop()

	'''
	static methods
	'''

	@staticmethod
	def reset(graph):
		for vertex in graph.vertex.values():
			vertex.used = False
