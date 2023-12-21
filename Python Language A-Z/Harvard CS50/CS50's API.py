# Using API with -- requests -- package

import requests #To make HTTP request to 3rd party APIs (iTunes - apple)
import sys
import json #THis module helps to manupulate json data type and format it in different way

if len(sys.argv) != 2:
    sys.exit("You should provide the name of the artist or band")   #To terminate the programme


#Now the code to make HTTP request to connect to the iTunes server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1]) #Change the limit=20 to limit=1, so to understand better for the first time  #The link is the API link provided by the iTunes
print(response.json())
print("\n\n\n")
json_format_response = response.json()

print(json.dumps(json_format_response, indent =2)) #Formatting json into a string, with the function dumps which is in json module -- dumps -- means dump sting ## Indent argument indents block with 2
print("\n\n")



for result in json_format_response["results"]:  #You'll get the idea once you see the raw JSON file
    print(result["trackName"])  #We are just printing the song name of the artist from the result, that we got as a response
