from api.requests_api import RequestsApi
from graph import graph
import threading

def clean_sector(request, sector, current_graph = False):
	if not current_graph:
		current_graph = graph.make_graph(request, sector)
	print sector
	while current_graph.edges_size > 0:
		path = current_graph.search_path()
		request.send_trajectory(sector, path) 
		current_graph.update(request)
	print "Ending thread %d" % sector

threads = []

sectors = range(2, 11)
request = RequestsApi()

current_graph = graph.make_graph(request, 1)
t = threading.Thread(target=clean_sector, args=(request, 1, current_graph,))
threads.append(t)
t.start()

for sector in sectors:
	t = threading.Thread(target=clean_sector, args=(request, sector,))
	threads.append(t)
	t.start()

for thread in threads:
	thread.join()
