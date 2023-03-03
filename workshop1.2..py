import http.client
help(http.client)

connection = http.client.HTTPConnection("www.google.com")
connection.request("GET", "/")
response = connection.getresponse()
print(response.status, response.reason)


