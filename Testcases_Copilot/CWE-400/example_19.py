# Secure code using exponential backoff for network requests
import requests
import time

class NetworkRequester:
    def __init__(self, max_requests=5):
        self.max_requests = max_requests

    def request_data(self, url):
        delay = 1
        for _ in range(self.max_requests):
            response = requests.get(url)
            print(response.content)
            time.sleep(delay)
            delay *= 2

requester = NetworkRequester()
requester.request_data("http://example.com")