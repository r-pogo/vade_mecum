# JSON
| Python | JSON |
|--------|------|
| dict | object
| list, tuple | array
| str | string
| int, long, float | number
| True | true
| False | false
| None | null
## Loading/reading JSON file
````python
import json 
import pprint

path_to_file = "data.json"
with open(path_to_file) as file:
    data = json.load(file)
    
pprint.pprint(data)
# OR
print(json.dumps(data, indent=4, sort_keys=True))
````
Loading JSON from a string
````python
import json
import pprint
stringJSON = '''
[
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    }
]
'''
data = json.loads(stringJSON)
pprint.pprint(data)
````
___
## Converting objects to JSON
````python
import json
data = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}
jsonData = json.dumps(data, indent=4)
````
___
## Saving JSON data into a file
````python
import json
data = [
    {
        "dictionary1" : "value1"
    },
    {
        "dictionary2" : "value2"
    },
    {
        "dictionary3" : "value3"
    }
]
nameOfFile = "jsonOutput.json"
with open(nameOfFile,"w") as file:
    json.dump(data, file)
````
___
## Parsing JSON
````python
import json
'''
DATA FORMAT
{   "key1" : "value1", 
    "key2" : "value2",
    "key3" : "value3"
}
'''
with open("data.json") as file:
    jsonData = json.load(file)
for key,value in jsonData.items():
    print(key,value)
````
Parsing JSON stored as a list of dictionaries
````python
import json
'''
DATA FORMAT
[
    { "dictionary1" : "value1"},
    { "dictionary2" : "value2"},
    { "dictionary3" : "value3"}
]
'''
with open("data.json") as file:
    jsonData = json.load(file)
for item in jsonData:
    for key,value in item.items():
        print(key,value)
````
Parsing JSON stored as a dictionary of dictionaries
````python
import json
'''
DATA FORMAT
{
    "dictionary1" : {"key1" : "value1"},
    "dictionary2" : {"key2" : "value2"},
    "dictionary3" : {"key3" : "value3"}
}
'''
with open("data.json") as file:
    jsonData = json.load(file)
for jsonName,jsonObject in jsonData.items():
    print(jsonName)
    for key,value in jsonObject.items():
        print(key,value)
````
Parsing JSON stored as a list of lists
````python
import json
'''
DATA FORMAT
[
    [1,2,3,4],
    ["helo" , "world" , "python"]
]
'''
with open("data.json") as file:
    jsonData = json.load(file)
for listItem in jsonData:
    for element in listItem:
        print(element)
````
___
## JSON Data Transformation
List of Dictionaries to a Dictionary
````python
import json
with open("data.json") as file:
    jsonData = json.load(file)
result = {}
for item in jsonData:
    result[item['color']] = item['value']
with open("jsonOutput.json","w") as file:
    json.dump(result, file)
    print("Saved File")
````
Dictionary of Dictionaries to a List of Dictionaries
````python
import json
with open("data.json") as file:
    jsonData = json.load(file)
result = []
for jsonName,jsonObject in jsonData.items():
    result.append(jsonObject)
with open("jsonOutput.json","w") as file:
    json.dump(result, file)
    print("Saved File")
````
List of Dictionaries to a List of Lists
````python
import json
with open("data.json") as file:
    jsonData = json.load(file)
colors = []
colorValues = []
for item in jsonData:
    colors.append(item['color'])
    colorValues.append(item['value'])
result =[ colors , colorValues]
with open("jsonOutput.json","w") as file:
    json.dump(result, file)
    print("Saved File")
````
___
## Encoding and Decoding Custom Python Object
json module doesn't understand how to encode customized data types by default.
Instead of going straight from the custom data type to JSON, is a good idea to throw in an intermediary step.
All you need to do is represent your data in terms of the built-in types json already understands. Essentially, 
you translate the more complex object into a simpler representation, which the json module then translates into JSON. 
It’s like the transitive property in mathematics: if A = B and B = C, then A = C  
read rest on https://realpython.com/python-json/#encoding-and-decoding-custom-python-objects
___
## Sources used for the creation of this cheat sheet
- E. Matthes, Python Crash Course: A Hands-On, Project-Based Introduction to Programming, No Starch Press 2016
- R. Banerjee, Programming Tips, A cheat sheet for working with JSON Data in Python — Python and Data Science for Everyone, https://medium.com/daily-programming-tips/a-cheat-sheet-for-working-with-json-data-in-javascript-bdd8de505333
- L. Lofaro, Real Python, Working With JSON Data in Python, https://realpython.com/python-json/#encoding-and-decoding-custom-python-objects