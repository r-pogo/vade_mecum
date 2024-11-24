# HTTP, HTTP2, HTTPS
Hypertext Transfer Protocol:
 - Protocol: system of rules that allow communication of information between different entities, like computers.

 - Hypertext: Hypertext is a somewhat outdated word for text that is displayed on a computer screen that contains hyperlinks to other text.  
web document.

Hypertext transfer protocol is the set of rules, servers and browsers used to transfer web documents back and forth.

This why every URL you type into a web browser starts with http.

### HTTP principles:
1. ```Plain language and human readable```: HTTP request methods: GET, POST, PUT, DELETE, CONNECT itp.  
2. ```Stateless protocol```: each individual request sent over the protocol is unique, and no request is connected to another request - has no memory of previous requests.  
3. ```Sessions```: Are stored states shared between the browser and the server.
The browser and server can exchange information about where you are in the sequence by passing back and forth information in form of cookies.  
In other words:  
Reload the page, and the browser sends along a cookie to the server saying, "Hey, last time we spoke we were looking at the third picture, start there."  
4. ```HTTP Headers```: That passing of cookies that allows HTTP to preserve sessions is made possible by the extensibility of HTTP.
When request and responses are sent over HTTP we can include headers, they carry information about everything from  
type of client sent the requests, server configuration, time and dates, duration of data storage, data format, cookies used to track sessions etc.  
5. ```HTTP works based on request/response pairs```: Every action performed over HTTP starts with a request using one of the HTTP methods
and ends with a response containing an HTTP status code saying what happened to the request along with the data like headers and content.  

```Some terminology```:
Browser: application used to access and navigate between HTML documents.  
User Agent: Application acting on behalf of the user - typically a browser.  
URL: Uniform Resource Locator
Proxy: Software or hardware service acting as a middle person between clients and servers.
Cache: Method of storing data on the client or server to speed up  performance.  

## Request/Response

When we access a website, your browser will need to make requests to a web server for assets such as HTML, Images, and download the responses. Before that, you need to tell the browser specifically how and where to access these resources, this is where URLs will help

### Anatomy of URL

![img.png](img/img_18.png)

URL: Human readable address describing where on the web a particular resources i s located.  

![img.png](img/img.png)

`URN` provides the location of the resource and is made up of several pieces:  

![img_1.png](img/img_1.png)


Scheme: This instructs on what protocol to use for accessing the resource such as HTTP, HTTPS, FTP (File Transfer Protocol).

User: Some services require authentication to log in, you can put a username and password into the URL to log in.

Host: The domain name or IP address of the server you wish to access.

Port: The Port that you are going to connect to, usually 80 for HTTP and 443 for HTTPS, but this can be hosted on any port between 1 - 65535.

Path: The file name or location of the resource you are trying to access.

Query String: Extra bits of information that can be sent to the requested path. For example, /blog?id=1 would tell the blog path that you wish to receive the blog article with the id of 1.

Fragment: This is a reference to a location on the actual page requested. This is commonly used for pages with long content and can have a certain part of the page directly linked to it, so it is viewable to the user as soon as they access the page


`Host`: this is the domain which is registered at a domain name service - DNS. And this domain points to a dedicated server IP address, somewhere on the web.  
`Port number`: Implied and usually invisible connection port, stating which port we want to access on the server. For http is  80 for https is 443.  
If the server uses another port or we want to access another port, say 8080, that port can be declared using a colon, localhost:8080.  
`Resource path`: This is the file location within the server. The default names for web documents are index.html and default.html, or just htm, or something like that.
If we request a folder without a file specification, the server and browser automatically look for files named either index.html or default.html or index.php or similar and returns that file to us.
If the file is called anything else, like about.html or contact.php, etc., the resource path needs to list the filename specifically, so mysite.com/folder/about.html.  
`URL query`: This is one or more queries added to the end of the resource path that can perform further actions on the server.
In some cases, such queries are used to track a user's ID, in others they're used to filter content or perform other actions.
URL queries start with a question mark and then each query comprises an argument and a value like u=1234. These queries can be strung together, using the ampersand symbol.  

### Methods
For standard web transactions we use typically 3: GET, POST, DELETE.
Other examples:
PUT
PATCH
HEAD
OPTIONS
TRACE

`GET`: Get the specified resources, if available.
A GET request for a public resource only needs the method and the URL to work.
If this resource sits behind a security layer, the request typically also needs an authorization header
containing an encrypted username and password pair and may require a cookie containing an authentication token

![img_2.png](img/img_2.png)

To send the data from the client to the server we use: POST, PUT, PATCH

`POST`: Create a new resources and add it to a collection
A POST request asks the server to create a new resource and give it an ID for future retrieval.
Because POST requests make changes to the server, they typically need an authorization header.

![img_3.png](img/img_3.png)

`PUT`: Update an existing singleton resources based on ID.
PUT is used to update an existing resource by replacing some or all of its contents with the contents of the request.
Like POST, PUT typically requires an authorization header.
Unlike POST, which just contains the contents, a PUT request contains the ID of a resource and the new content to be added to that resource.
If the resource already exists, the existing content is replaced with the contents in the PUT request.
If no resource with this ID exists, the server will in some cases allow the new resource to be created
with the user defined ID or you'll get an error message.

![img_4.png](img/img_4.png)

`PATCH`: Modify an existing singleton resource based on ID.
PATCH is used to modify an existing resource. Where PUT updates the resource by replacing content, Patch can carry along instructions on how to modify
the existing resource without necessarily replacing data.
PATCH also typically requires an authorization header and returns the same status as PUT.

![img_5.png](img/img_5.png)

`DELETE`: Delete a singleton resources based on ID.
It deletes a specified resource. A DELETE request must contain the ID for the resource and an authorization header.

![img_6.png](img/img_6.png)

`Methods to get infomration from  server`:  
`HEAD`: Get just the response headers from the resources

![img_7.png](img/img_7.png)

`OPTIONS`: Get the options available from this resources

![img_8.png](img/img_8.png)

`TRACE`: Create a loopback for the request message.

![img_9.png](img/img_9.png)

## HTTP status messages

1xx - Information: These are sent to tell the client the first part of their request has been accepted and they should continue sending the rest of their request
2xx - Success: This range of status codes is used to tell the client their request was successful.
3xx - Redirection: These are used to redirect the client's request to another resource. This can be either to a different webpage or a different website altogether.
4xx - Client error: Used to inform the client that there was an error with their request.
5xx - Server error: This is reserved for errors happening on the server-side and usually indicate quite a major problem with the server handling the request.
___
## HTTP headers
An HTTP header is a human readable name value pair separated by a colon, added to the HTTP request or response,  
which can be used to pass standard or custom information back and forth between the client and the server.
A request can hold as many headers as are needed, each separated by a line break.

E.g:
Say you want to send a POST request to a content management system to create a new resource.  
To make this work, you first have to authenticate yourself to prove to the server you have the correct authorization to create new resources.
In it's most basic form, this type of authentication
is done by sending an authentication header with basic authentication information, a username and a password.
In the real world, the username password combo is Base64 encoded, to ensure it doesn't get misunderstood as a text string  when passed to the server.

If a server wants, or needs, the client to remember where it has been or what state it is in, it can use a set cookie header,
to give the client a cookie, a small piece of data.
The next time the client visits the server, it sends the cookie back, and the server brings the client to the right state.

If a server wants the client to cache, so effectively save some data for specific period of time,
it can send one or several cache headers.
These headers tell the browser what files to save, whether cached files should be updated,
and for how long they should be kept.

Caching files can dramatically improve performance cause you're not sending as many files
back and forth every time you're reloading a page, but when files are cached in the browser,
the browser will not receive any new versions of those files until the cached files are either cleared or have expired.  
Headers are also often used to provide information about the client or the server.  
This can be anything from date and time information about the request response pair,
to a user agent header identifying the client, a server header identifying the software used by the server,
proxy information, security information, cross origin resource sharing information,
and much more.
With HTTP2 and other modern technologies, we're also seeing new headers come online including Link,
which allows us to use server Push, to push files to the client before they are requested.

### Anatomy of a request header

Common Request Headers

﻿These are headers that are sent from the client (usually your browser) to the server.

Host: Some web servers host multiple websites so by providing the host headers you can tell it which one you require, otherwise you'll just receive the default website for the server.

User-Agent: This is your browser software and version number, telling the web server your browser software helps it format the website properly for your browser and also some elements of HTML, JavaScript and CSS are only available in certain browsers.

Content-Length: When sending data to a web server such as in a form, the content length tells the web server how much data to expect in the web request. This way the server can ensure it isn't missing any data.

Accept-Encoding: Tells the web server what types of compression methods the browser supports so the data can be made smaller for transmitting over the internet.

Example:

First the client states what method is using and what resources it's requesting using a regular URL.

![img_10.png](img/img_10.png)

Next, the client adds in a user-agent header to identify itself, lists out what file types, language types and encoding types it accepts,  

![img_11.png](img/img_11.png)

tells the server where it came from, using the refer header,

![img_12.png](img/img_12.png)

tells it to keep the connection alive for future requests

![img_13.png](img/img_13.png)

and sets the cache-control of the current file to zero seconds, meaning it will not be saved when it arrives.

![img_14.png](img/img_14.png)

### Anatomy of a response header

ommon Response Headers

These are the headers that are returned to the client from the server after a request.

Set-Cookie: Information to store which gets sent back to the web server on each request (see cookies task for more information).

Cache-Control: How long to store the content of the response in the browser's cache before it requests it again.

Content-Type: This tells the client what type of data is being returned, i.e., HTML, CSS, JavaScript, Images, PDF, Video, etc. Using the content-type header the browser then knows how to process the data.

Content-Encoding: What method has been used to compress the data to make it smaller when sending it over the internet.

Example:

This response header declares the status of the response 200 OK, the server type, the date and time of the response  
message, the content type of the return data, and other information.

![img_15.png](img/img_15.png)


In addition comes the entire payload which in this case is html document.

![img_16.png](img/img_16.png)

The client in our case, the Firefox browser, receives this header and processes whatever data  
is returned in the payload according to the header content.  
In this example that is to render the content of the return of the html document.

![img_17.png](img/img_17.png)
___
## Analyzing traffic logs example
Example of log file (access.log):

```
192.168.1.1 - alice [10/Nov/2024:13:01:15 -0500] "GET /index.html HTTP/1.1" 200 2456 "http://example.com/home" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
203.0.113.25 - bob [10/Nov/2024:13:01:50 -0500] "POST /login HTTP/1.1" 302 512 "http://example.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
198.51.100.42 - charlie [10/Nov/2024:13:02:15 -0500] "OPTIONS /api/ HTTP/1.1" 204 0 "http://example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
192.168.1.3 - dave [10/Nov/2024:13:03:00 -0500] "PATCH /profile HTTP/1.1" 200 1024 "http://example.com/settings" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/92.0"
203.0.113.20 - eve [10/Nov/2024:13:03:30 -0500] "PUT /settings/update HTTP/1.1" 200 512 "http://example.com/settings" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/95.0"
198.51.100.55 - frank [10/Nov/2024:13:04:10 -0500] "DELETE /account HTTP/1.1" 204 0 "http://example.com/settings" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
192.168.1.1 - alice [10/Nov/2024:13:05:00 -0500] "GET /assets/js/main.js HTTP/1.1" 304 - "http://example.com/index.html" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
203.0.113.25 - bob [10/Nov/2024:13:06:05 -0500] "POST /api/submit HTTP/1.1" 200 4321 "http://example.com/form" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
198.51.100.42 - charlie [10/Nov/2024:13:07:12 -0500] "OPTIONS /api/items HTTP/1.1" 204 0 "http://example.com/items" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
192.168.1.3 - dave [10/Nov/2024:13:07:40 -0500] "GET /contact HTTP/1.1" 200 1723 "http://example.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/92.0"
203.0.113.20 - eve [10/Nov/2024:13:08:25 -0500] "PUT /api/update-item HTTP/1.1" 200 2134 "http://example.com/items" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/95.0"
198.51.100.55 - frank [10/Nov/2024:13:09:15 -0500] "PATCH /items/1234 HTTP/1.1" 200 1298 "http://example.com/items/1234" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
192.168.1.1 - alice [10/Nov/2024:13:09:45 -0500] "GET /about HTTP/1.1" 200 1950 "http://example.com/contact" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
...
```
Each individual line represents a request.
Analysis:
```
cat access.log | cut -f 6 -d " " | sort | uniq -c | sort -n
7 "OPTIONS
12 "CONNECT
21 "-"
51 "HEAD
235 "POST
2997 "GET --> maybe a web scraping was searching for info?
```
```
cat access.log | grep "OPTIONS 

OTPIONS lists all teh method the the server supports
this can be an indicator on attacker trying to do an enumeration

POST to check is somone is uploading data
```
To check teh requested resource (after the HTTP method):
```
cat access.log | cut -f 7 -d " " | sort | uniq -c | sort -n

...
118 robots.txt
898 / --> root level of web page

robots.txt: resource to tell bots and web crawlers what part of the page you don't want them to be indexed
attacker use it so look for sensitive info and restricted areas.
```
Extract response status:
```
cat access.log | cut -f 9 -d " " | sort | uniq -c | sort -n
to see a t what file are pointing
cat access.log | cut -f 7,9 -d " " | sort | uniq -c | sort -n | grep "404"
```
___
## Cookies
You've probably heard of cookies before, they're just a small piece of data that is stored on your computer. Cookies are saved when you receive a "Set-Cookie" header from a web server. Then every further request you make, you'll send the cookie data back to the web server. Because HTTP is stateless (doesn't keep track of your previous requests), cookies can be used to remind the web server who you are, some personal settings for the website or whether you've been to the website before. Let's take a look at this as an example HTTP request:

![img_1.png](img/img_19.png)

___
## Sources
- M. Rand-Hendriksen, HTTP Essential Training, https://www.linkedin.com/learning/http-essential-training
- B. DeVault, Network Protocols for Security: HTTP, https://app.pluralsight.com/
- https://tryhackme.com/