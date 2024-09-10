'''Implement a NetworkRequester class that makes network requests while preventing uncontrolled request frequency.'''
# Secure code with controlled network requests (limiting retries)
import requests

class NetworkRequester:
    def __init__(self, max_requests=5):
        self.max_requests = max_requests

    def request_data(self, url):
        for _ in range(self.max_requests):
            response = requests.get(url)
            print(response.content)

requester = NetworkRequester()
requester.request_data("http://example.com")