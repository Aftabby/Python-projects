book = {}

book["Tom"] = {             #As the element of a dictionary named -- book --, we are declaring another dictionary as value
    "name" : "Tom",
    "address" : "1 red street, NY",
    "phone" : 365565220
}

book["Bob"] = {             #As the element of a dictionary named -- book --, we are declaring another dictionary as value
    "name" : "bob",
    "address" : "Mirpur Haha, NY",
    "phone" : 65648138
}

import json         #Importing json module

s = json.dumps(book)   #  This function taking dictionary object which is -- book -- as an input and then it is dumping it as a string, thus it is converted into a json format

print(s)





#Important Notes
# There is no object called JSON in python
