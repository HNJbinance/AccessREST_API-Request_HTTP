import requests
import os
from PIL import Image

# from IPython.display import IFrame

'''Uniform Resource Locator: URL'''

url = 'https://www.ibm.com/'
r = requests.get(url)

# see the status of the request
r.status_code

# view the request headers
print("####request headers: \n", r.request.headers)

# view the request body
print("####request body: ", r.request.body)

# view the HTTP response header using the attribute headers.
# This returns a python dictionary of HTTP response headers.
print("####response HTTP: \n", r.headers)

# The date the request was sent with Date
print("####the date the request was sent: \n", r.headers['date'])

# view the type of data we did get
print("####Type of data we got: \n", r.headers['Content-Type'])

# check the encoding
print("####Check the encoding: \n", r.encoding)

# As the context type we can dipsplay the first 100 character
print("####the 100 characters: \n", r.text[0:100])

# Use single quotation marks for defining string
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r = requests.get(url)

# View the response headers
print("####The response header: \n", print(r.headers))

# view the type of data we did get
print("####Type of data we got: \n", r.headers['Content-Type'])

# An image is a response object that contains the image as a bytes-like object.
# As a result, we must save it using a file object. First, we specify the file path and name
path = os.path.join(os.getcwd(), 'image.png')

# W e save the file, in order to access the body of the response we use the attribute content.
# then save it using the open function and write method
with open(path,'wb') as f:
    f.write(r.content)

# We can view the image
Image.open(path)

# another request
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r = requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

'''Get Request with URL Parameters'''

# The Base URL is for http://httpbin.org/ is a simple HTTP Request & Response Service.
# The URL in Python is given by:

url_get = 'http://httpbin.org/get'

# A query string is a part of a uniform resource locator (URL), this sends other information to the web server.
# The start of the query is a ?, followed by a series of parameter and value pairs, as shown in the table below.
# The first parameter name is name and the value is Joseph. The second parameter name is ID and the Value is 123.
# Each pair, parameter, and value is separated by an equals sign, =.
# The series of pairs is separated by the ampersand &.

url_get = 'http://httpbin.org/get?Name=Joseph&ID=123'
#This will return this dictionnary
'''{
  "args": {
    "ID": "123", 
    "Name": "Joseph"
  }, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-636a8a53-6f49a04205a591dd4d8c9a4d"
  }, 
  "origin": "194.199.3.13", 
  "url": "http://httpbin.org/get?Name=Joseph&ID=123"
}'''
# To create a Query string, add a dictionary.
# The keys are the parameter names and the values are the value of the Query string.

payload = {"Name" : "Joseph", "ID": "123"}

# Then passing the dictionary payload to the params parameter of the  get() function:
r = requests.get(url_get, params=payload)

# We can print out the URL and see the name and values
print("The URL and see name and values : \n", r.url)

#We can look at the 'Content-Type'.

r.headers['Content-Type']

# As the content 'Content-Type' is in the JSON format we can use the method json(),
# it returns a Python dict
r.json()

#The key args has the name and values:
r.json()['args']


