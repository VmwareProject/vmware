class Dfs:
	def	__init__(self, graph):
		self.graph = graph
	
	def start(self):
		self.longest = []
		self.current = []
		Dfs.reset(self.graph)

		for vertex in self.graph.vertex.values():
			if not vertex.used: self.dfs(vertex)
		return self.longest

	def dfs(self, vertex):
		self.current.append(vertex.id)
		vertex.used = True
		for edge in vertex.edges:
			if not edge.passed and edge.v2 != vertex:
				edge.passed = True
				self.dfs(edge.v2)
				edge.passed = False
		#if len(set(self.current)) > len(set(self.longest)):
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
