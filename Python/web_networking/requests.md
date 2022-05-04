|Method | Description |
|-------|-------------|
| delete(url, args) | Sends a DELETE request to the specified url `requests.delete('https://httpbin.org/delete')`
| get(url, params, args) | Sends a GET request to the specified url `requests.get('someURL')`
| head(url, args) | Sends a HEAD request to the specified url `requests.head('https://httpbin.org/get')`
| patch(url, data, args) | Sends a PATCH request to the specified url `requests.patch('https://httpbin.org/patch', data={'key':'value'})`
| post(url, data, json, args) | Sends a POST request to the specified url `requests.post('https://httpbin.org/post', data={'key':'value'})`
| put(url, data, args) | Sends a PUT request to the specified url `requests.put('https://httpbin.org/put', data={'key':'value'})`
| request(method, url, args) | Sends a request of the specified method to the specified url 
___
## Response
Status code:  
1xx Informational  
2xx Success  
3xx Redirection  
4xx Client Error  
5xx Server Error  
```python
import requests

response = requests.get('https://api.github.com')
response.raise_for_status()  # returns an HTTPError object if an error has occurred during

print(response.status_code)
200

response.content  # to see the content in bytes
response.encoding = 'utf-8'  # is optional, decoding bytes to string in .text 
# requires an encoding scheme requests will try to guess 
# the encoding based on the response’s headers, you can providing your own.
response.text  # to see the content as a string

response.headers  # can provide useful info
response.headers['Server']  # .headers returns a dictionary, can access header values by key

# Other methods responses can also be inspected in a similar way
```
___
## Parameters
```python
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
# parameters can also be passed as a list of tuples
requests.get("https://opentdb.com/api.php", params=[("amount", 10), ("type", "boolean")])
# also as bytes
requests.get("https://opentdb.com/api.php", params=b'amount=10')
```
## Headers
Headers are specified similarly to parameters
```python
import requests

headers = {
    "header1": "something",
    "header2": "something2",
}

response = requests.get("https://opentdb.com/api.php", headers=headers)
```
___
## POST, PUT, PATCH
This HTTP methods pass their data through the message body rather than through parameters in the query string.
In request use the data parameter to pass the payload to the corresponding function.
```python
import requests

requests.post('https://httpbin.org/post', data={'key':'value'})
# or as a list of tuples
requests.post('https://httpbin.org/post', data=[('key', 'value')])
```
Use the json parameter if you want to send JSON data.
```python
import requests

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
json_response['data']
'{"key": "value"}'
json_response['headers']['Content-Type']
'application/json'

# httpbin.org is a great resource created by the author of requests, Kenneth Reitz. It’s a service that accepts  
# test requests and responds with data about the requests.
```
___
## Inspecting the request
`requests` library prepares the request before actually sending it to the destination server. Request preparation   
includes things like validating headers and serializing JSON content.
You can view the `PreparedRequest` by accessing `.request`:
```python
import requests

response = requests.post('https://httpbin.org/post', json={'key':'value'})
response.request.headers['Content-Type']
'application/json'
response.request.url
'https://httpbin.org/post'
response.request.body
b'{"key": "value"}'
```
___
## Authentication
## TODO finish