from requests import Session

class Luca():
	def __init__(self) -> None:
		self.logged_in = False
		self.mute = False
		self.s = Session()
		self.s.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
								'Accept': '*/*',
								'Accept-Language': 'en-US,en;q=0.5',
								'Referer': 'https://app.luca-app.de/',
								'Content-Type': 'application/json',
								'Origin': 'https://app.luca-app.de',
								'DNT': '1',
								'Connection': 'keep-alive'
    	})


	def login(self, email: str, password: str) -> None:
		"""
		Log in to your luca account. Required for any further requests
		"""

		url = "https://app.luca-app.de/api/v3/auth/login"

		headers = {}
		headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0"
		headers["Accept"] = "*/*"
		headers["Accept-Language"] = "en-US,en;q=0.5"
		headers["Referer"] = "https://app.luca-app.de/"
		headers["Content-Type"] = "application/json"
		headers["Origin"] = "https://app.luca-app.de"
		headers["DNT"] = "1"
		headers["Connection"] = "keep-alive"

		data = "{\"username\":\"" + email + "\",\"password\":\"" + password + "\"}"
		print(data)

		r = self.s.post(url, headers=headers, data=data)

		if r.status_code == 200 and r.text == "OK":
			if not self.mute: 
				print("[+] Successfully logged into your Luca account.")
			self.logged_in = True
			return


		print(r.status_code)
		print(r.text)


	def register(self) -> None:
		print("Not implemented yet")
		# TODO

	def createLocation(self):
		if not self.logged_in:
			if not self.mute: 
				print("[!] You have to be logged in to create a location.")
			return {}

		print("Not implemented yet")
		# TODO

	def getAllLocations(self) -> dict:
		if not self.logged_in:
			if not self.mute: 
				print("[!] You have to be logged in to get all locations.")
			return {}

		url = "https://app.luca-app.de/api/v3/locationGroups"

		r = self.s.get(url)

		if r.status_code == 200:
			if not self.mute:
				print("[+] Successfully got all locations")
			return r.json()
		else:
			print(r.status_code)
			print(r.text)
			return {}


	def getAdditionalGroupData(self, group_id: str) -> dict:
		if not self.logged_in:
			if not self.mute: 
				print("[!] You have to be logged in to get additional group data.")
			return {}

		url = "https://app.luca-app.de/api/v3/locationGroups/additionalDataSchema/" + group_id

		r = self.s.get(url)

		if r.status_code == 200:
			if not self.mute:
				print("Successfully got additional group data.")
			return r.json()
		else:
			print(r.status_code)
			print(r.text)


	def getAdditionalLocationData(self, location_id: str) -> dict:
		if not self.logged_in:
			if not self.mute: 
				print("[!] You have to be logged in to get additional group data.")
			return {}

		url = "https://app.luca-app.de/api/v3/locations/additionalDataSchema/" + location_id

		r = self.s.get(url)

		if r.status_code == 200:
			if not self.mute:
				print("Successfully got additional location data.")
			return r.json()
		else:
			print(r.status_code)
			print(r.text)


	def getCheckedInCount(self, scanner_id: str) -> int:
		if not self.logged_in:
			if not self.mute: 
				print("[!] You have to be logged in to get the checked in count.")
			return -1

		url = f"https://app.luca-app.de/api/v3/scanners/{scanner_id}/traces/count/current"
		
		r = self.s.get(url)

		if r.status_code == 200:
			try:
				count = int(r.text)
				if not self.mute:
					print("[+] Successfully got the checked in count.")
				return count
			except:
				print(r.text)
				return -1
		else:
			print(r.status_code)
			print(r.text)
			return -1


