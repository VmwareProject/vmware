import vertex

class Edge:

	def __init__(self, v1, v2):
		self.passed = False
		self.v1 = v1
		self.v2 = v2

	def remove(self):
		self.v1.edges.discard(self)
		self.v2.edges.discard(self)
