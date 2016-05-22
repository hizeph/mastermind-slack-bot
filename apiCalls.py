import json
import urllib3

class ApiCalls:

	def __init__(self):
		pass

	def request(self, url, data):
		http = urllib3.PoolManager(1)
		response = http.request('POST', 
					url, headers={'Content-Type' : 'application/json'},
					body=json.dumps(data) )
		jsonObj = dict()
		try:
			jsonObj = json.loads(response.data.decode("utf-8"))
		except:
			pass
		return jsonObj

	def connect (self, user):
		data = {
			'user' : user
		}
		return self.request('http://az-mastermind.herokuapp.com/new_game', data)

	def guess(self, code, key):
		data = {
			'code' : code,
			'game_key' : key
		}
		return self.request('http://az-mastermind.herokuapp.com/guess', data)
		
