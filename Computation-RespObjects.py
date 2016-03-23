# Import the libraries required for running the program
import urllib.request
import json

# To ensure that this script is able to access the API url
url = ""
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

# Set the initial counter/conditional variables
globalHDCounterTrue = 0
globalHDCounterFalse = 0
checkMore = True
testVar = 1

# Store the test url for reference as a variable
urlTester = "http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page="

# Define the primary condition
while (checkMore == True):
    url = ""
    url = urlTester + str(testVar)

# Convert the JSON object returned as a response to Python
    opener = AppURLopener()
    response = opener.open(url)
    data = json.loads(response.read().decode("utf8"))

# Access the response key which is an array of more JSON objects - 'flags' and within 'flags', a key called 'hd'
    checkMore = data['more']
    checkOther = data['response']
    checkFlags = data['response'][0]['flags']
    checkHD = data['response'][0]['flags']['hd']

# Set counters and conditional statement to calculate the response objects that have flags:hd set to true and false
    i=0
    hdTrue = 0
    hdFalse = 0
    for something in data['response'][i]['flags']:
        if (data['response'][i]['flags']['hd']):
            hdTrue = hdTrue + 1
        else:
            hdFlase = hdFalse + 1
        i = i+1

# Increment page number of the test url
    testVar = testVar + 1

# A global counter to compute the value of response objects - flags:hd set to true and false
    globalHDCounterTrue = globalHDCounterTrue + hdTrue
    globalHDCounterFalse = globalHDCounterFalse + hdFalse

# Print the final results
print ("Total no. of pages parsed are")
print(testVar-1)
print ("Total no. of response objects that have the flag:hd value set to True is")
print(globalHDCounterTrue)
print("Total no. of response objects that have the flag:hd value set to False is")
print(globalHDCounterFalse)
