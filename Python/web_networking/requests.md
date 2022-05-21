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

response.status_code == requests.codes.ok  # if code is 2xx

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
## Writing the content
````python
import  requests

res = requests.get('https://someURL')
res.raise_for_status()

file = open('fileName', 'wb')
for chunk in res.iter_content(100000):  # bytes number
    file.write(chunk)
file.close()
````
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
## POST, PUT, PATCH, DELETE
This HTTP methods pass their data through the message body rather than through parameters in the query string.
In request use the data parameter to pass the payload to the corresponding function.
```python
import requests

requests.post(url='https://httpbin.org/post', data={'key':'value'})
# or as a list of tuples
requests.post('https://httpbin.org/post', data=[('key', 'value')])
```
Use the json parameter if you want to send JSON data.
```python
import requests

response = requests.post('https://httpbin.org/post', json={'key':'value'}, headers=headers)
response.raise_for_status())
json_response = response.json()
json_response['data']
'{"key": "value"}'
json_response['headers']['Content-Type']
'application/json'
print(response.text)

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
All the request function provide the `auth` parameter, which allows to pass credentials.
```python
import requests

requests.get('https://someURL', auth=('username', 'password'))
```
When passing username and password in a tuple to the auth parameter, requests is applying the credentials using `HTTP’s 
Basic access authentication scheme` under the hood.
You can make the same request by passing explicit Basic authentication credentials using `HTTPBasicAuth`.  
`requests` provides other methods of authentication out of the box such as `HTTPDigestAuth` and `HTTPProxyAuth`.
```python
from requests.auth import HTTPBasicAuth
import requests
requests.get('https://someURL',auth=HTTPBasicAuth('username', 'password'))
```
You can create your own authentication mechanism. To do so, you must first create a subclass of `AuthBase`.  
Then implement `__call__()`.
```python
import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
```
Another simple example of authentication. Storing auth key as environment variable.
```python
import requests
import os

SOME_APP_Endpoint = "https://someAppURL"
api_key = os.environ.get("SOME_APP_API_KEY")
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "info1": "info",
    "info2": "info",
    "appid": api_key,
    "info3": "info"
}

response = requests.get(SOME_APP_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#...some code...
# Fake AuthObject were environment variable is being used
auth_variable = AuthObject(account_sid, auth_token, http_client=proxy_client)
```
### SSL certificate verification
SSL certification allows establishing an encrypted connection with sites over HTTP.
`requests` does by default, but you can disable it:
```python
import requests
requests.get('https://someURL', verify=False)
```
___
## Performance
`timeout` parameter allows you to specify a duration for the response, `requests` by default wait indefinitely.
```python
import requests

requests.get('https://someURL', timeout=1)  # one second
requests.get('https://someURL', timeout=3.05)  # 3.05 seconds
requests.get('https://someURL', timeout=(2, 5))  # first element is a connection timeout, the second element is a read timeout  
# If the request establishes a connection within 2 seconds and receives data within 5 seconds of the connection being established, 
# then the response will be returned as it was before. If the request times out, then the function will raise a Timeout exception

import requests
from requests.exceptions import Timeout

try:
    response = requests.get('https://someURL', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')
```
___
## Session
Class called `Session` is under the hood of all the higher level abstractions like `get()` and `post()`.  
If you need more control over yor requests use the `Session` class.  
Example, if you want to use the same authentication across multiple requests, you could use a session:
````python
import requests
from getpass import getpass

# By using a context manager, you can ensure the resources used by
# the session will be released after use
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# You can inspect the response just like you did before
print(response.headers)
print(response.json())
````
___
## Retries
If you want to retry the same request you will need to implement a custom Transport Adapter.  
Transport Adapters let you define a set of configurations per service you’re interacting with.  
For example, you could try to reconnect multiple times before raising a ConnectionError.
````python
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

my_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `my_adapter` for all requests to endpoints that start with this URL
session.mount('https://someURL', my_adapter)

try:
    session.get('https://someURL')
except ConnectionError as ce:
    print(ce)
````
___
## Sources used for the creation of this cheat sheet
- A. Ronquillo, Real Python, Python’s Requests Library (Guide), https://realpython.com/python-requests/#authentication
- Requests: HTTP for Humans, https://docs.python-requests.org/en/latest/
- A. Sweigart, Automate the Boring Stuff with Python, 2st Edition:
    Practical Programming for Total Beginners, No Starch Press 2020
