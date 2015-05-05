import requests
import yaml

class RequestsApi:

	def __init__(self):
		'init'
		self.config = yaml.load(open("config/request_settings.yml", "r"))

	def get_objects(self, sector):
		'request to get objects'
		objects_points = []
		url = self.config['host'] + self.config['object_path'] % sector
		response = requests.get(url)		
		if not response.status_code == 200 : return []
		for line in response.text.splitlines():
			objects_points.append([int(num) for num in line.split(' ')]) 
		return objects_points

	def get_roots(self, sector):
		'request to get roots'		
		roots = []
		url = self.config['host'] + self.config['root_path'] % sector
		response = requests.get(url)
		if not response.status_code == 200 : return []
		for line in response.text.splitlines():
			roots.append(int(line)) 			
		return roots

	def send_trajectory(self, sector, paths):
		'requets to send trajectory'
		url = self.config['host'] + self.config['trajectory_path'] % sector
		requests.post(url, params = {'trajectory' : paths})
