import edge

class Vertex:

	def __init__(self, id):
		self.used = False
		self.id = id
		self.edges = set()

	def add_edge(self, edge):
		self.edges.add(edge)

	def destroy(self):
		while self.edges: self.edges.pop().remove()
