import json     # this library use to format json data into human readable format.
import requests # this request tha json data by the api form the internet
import sys

if len(sys.argv) != 3:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

#  code 1 : json.dumps  -> prints the entire raw JSON in a readable/formatted way

print(json.dumps(response.json(), indent=2)) # here indent use to make space of 2 atleast

# output: formatted JSON response containing song data
# output is JSON with dictionaries inside a list, formatted with 2-space indentation

# Code 2 output -> extracts only a specific field from JSON and prints it directly
trackname = response.json()
for result in trackname["results"]:
    print(result["trackName"])
