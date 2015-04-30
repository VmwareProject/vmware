from api.requests_api import RequestsApi
from graph import graph
import random

sectors = range(1, 11)
random.shuffle(sectors)

request = RequestsApi()

for sector in [3]:#sectors:
	current_graph = graph.make_graph(request, sector)
	print current_graph.edges_size
	#print sector
	'''while True:
		path = current_graph.search_path()
		request.send_trajectory(sector, path) 
		#print current_graph.edges_size
		if current_graph.edges_size <= 4: 
			break		
		current_graph.update(request)'''
	print current_graph.vertex.keys()
