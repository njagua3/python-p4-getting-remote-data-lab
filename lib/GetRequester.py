import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    # Method to send GET request and return the body of the response as raw bytes
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Returns the response body as bytes

    # Method to parse the response body as JSON and return a Python object (list or dictionary)
    def load_json(self):
        response_body = self.get_response_body()  # Get the raw response body as bytes
        try:
            return json.loads(response_body.decode('utf-8'))  # Convert bytes to string and then parse as JSON
        except json.JSONDecodeError:
            return None  # Return None if the response cannot be decoded as JSON
