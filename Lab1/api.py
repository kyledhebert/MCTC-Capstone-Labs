import requests
import json

# a parameter for finding earthquakes
# with a magnitude greater than 8
payload = {"min_magnitude":"8"}

try:
	r = requests.get("http://www.seismi.org/api/eqs/2011/03", params = payload)
except:
	ConnectionError
	print("There has been a connection error")
else:
	# displays the query url
	print("=" * len(r.url))
	print(r.url)
	print("=" * len(r.url))

	# displays the resulting data
	print("Earthquakes with a magnitude greater than 8 occurred in these regions in March, 2011:")

	for region in r.json().get("earthquakes"):
		print(region.get("region"))


