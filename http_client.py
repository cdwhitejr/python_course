import http.client

#create a connection
connection = http.client.HTTPConnection('www.google.com')

#What method we want to use and the information we are looking for
connection.request('GET','/')

#Handles the response from server
response = connection.getresponse()

#Print the response
print(f'\nResponse:',response)
print(f'\nStatus: {response.status} \nReason: {response.reason}')

#Reads the data
data = response.read()

#Prints the data
#print('\n\nData:',data)

connection.close()