'''Implement a NetworkRequester class that makes network requests while preventing uncontrolled request frequency.'''
# Insecure code with uncontrolled resource consumption (network requests)
import requests

class NetworkRequester:
    def __init__(self):
        pass

    def request_data(self, url):
        while True:
            response = requests.get(url)
            print(response.content)

requester = NetworkRequester()
requester.request_data("http://example.com")