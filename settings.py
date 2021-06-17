from json import load, dump
import json

class Settings:

	def __init__(self):

		#APP CONF
		self.title = "Database App"


		#WINDOW CONF
		base = 75
		ratio = (16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+1000+400"


		#IMG CONF
		self.logo = "img/Shopeelogo.jpg"
		self.users_path = "users.json"

		#DUMMY DATA database

		#self.database = None
		self.load_data_from_json()


	def load_data_from_json(self):
		with open("data/database.json", "r") as file_json:
			self.database = load(file_json)

	def save_data_to_json(self):
		with open("data/database.json", "w") as file_json:
			dump(self.database, file_json, default=str)

	def load_userData(self, path):
		with open(path, "r") as json_data:
			data = json.load(json_data)
		return data
	
	def login(self, username, password):
		users = self.load_userData(self.users_path)
		if username in users:
			if password == users[username]["password"]:
				return True
			else:
				return False
		else:
			return False

	



