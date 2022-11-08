import requests
import os
from PIL import Image

# from IPython.display import IFrame

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

#We can view the image

Image.open(path)


