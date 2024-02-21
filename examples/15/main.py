# This file will show you how to use requests in Python
#
# Requests is a simple way to make HTTP requests in Python
#
# For example:

# You will need to import the requests library using pipenv
# For example:
# pipenv install requests
# Then you can use requests to make a request
import requests



response = requests.get('https://api.github.com')
print(response.json())
# This will output the following:
# {'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': '

# You can also use requests to make a POST request
# For example:
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(response.json())
# This will output the following:
# {'args': {}, 'data': '', 'files': {}, 'form': {'key': 'value'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '9', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root

# You can also use requests to make a PUT request
# For example:
response = requests.put('https://httpbin.org/put', data = {'key':'value'})
print(response.json())

# This will output the following:
# {'args': {}, 'data': '', 'files': {}, 'form': {'key': 'value'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '9', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.1', 'X-Amzn-Trace-Id': 'Root
