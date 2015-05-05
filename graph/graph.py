from vertex import Vertex
from edge import Edge
from algorithm.dfs import Dfs
from algorithm.fast_dfs import FastDfs
import yaml

class Graph:
	def __init__(self, sector):
		self.edges_size = 0
		self.sector = sector
		self.vertex = {}
		self.dfs_algorithm = Dfs(self)
		self.fast_dfs_algorithm = FastDfs(self)

	def update(self, request):
		objects = request.get_objects(self.sector)
		objects = set(reduce(lambda x,y: x+y, objects))
		elements = set(self.vertex.keys())
		diff = elements ^ objects
		while diff: self.remove(diff.pop())		

	def add_point(self, id):
		if not self.vertex.has_key(id): self.vertex[id] = Vertex(id)

	def search_path(self):
		result = self.fast_dfs_algorithm.start()
		return ' '.join([str(i) for i in result])

	def connect(self, id1, id2):
		v1 = self.vertex[id1]
		v2 = self.vertex[id2]
		e = Edge(v1, v2)
		v1.add_edge(e)
		v2.add_edge(e)

	def remove(self, id):
		vertex = self.vertex.get(id, False)
		if vertex:
			self.edges_size -= len(vertex.edges)
			vertex.destroy()
			del self.vertex[id]

	def remove_and_next(self, id):
		vertex = self.vertex.get(id, False)
		if vertex:
			edges = vertex.edges.copy()
			self.remove(id)
			while edges: 
				target = edges.pop().v2					
				if target != vertex: self.remove_and_next(target.id)

def make_graph(requests, sector):
	graph = Graph(sector)	
	objects = requests.get_objects(sector)
	roots = requests.get_roots(sector)
	graph.edges_size = len(objects)
	for point in objects:
		p1 = point[0]; p2 = point[1]
		graph.add_point(p1)
		graph.add_point(p2)
		graph.connect(p1, p2)
	for root in roots: graph.remove_and_next(root)

	return graph
		
